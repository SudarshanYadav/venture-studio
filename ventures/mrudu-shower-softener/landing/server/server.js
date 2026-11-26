// Mrudu pre-order server: Razorpay order creation, signature verification, Meta CAPI Purchase.
// Zero dependencies. Node 18+ (uses global fetch and built-in crypto).
//
//   Local:  set env vars (see ../env.example), then `node server/server.js` from landing/
//           -> serves index.html + policies.html and /api/* on http://localhost:3000
//   Vercel: api/create-order.js and api/verify-payment.js re-export this handler.
//
// The order record lives in Razorpay (order notes hold name, phone, pincode). No database.
'use strict';
const crypto = require('crypto');

const PRICE_PAISE = 199900;          // ₹1,999 incl. all taxes. Server is the source of truth for price.
const CURRENCY = 'INR';
const CONTENT_ID = 'mrudu-preorder';

const env = (k, d) => process.env[k] || d;
const cfg = () => ({
  keyId: env('RAZORPAY_KEY_ID', ''),
  keySecret: env('RAZORPAY_KEY_SECRET', ''),
  allowLive: env('ALLOW_LIVE_PAYMENTS', 'false') === 'true',
  pixelId: env('META_PIXEL_ID', ''),
  capiToken: env('META_CAPI_TOKEN', ''),
  testEventCode: env('META_TEST_EVENT_CODE', ''),
  graphVersion: env('META_GRAPH_VERSION', 'v23.0'),
});

function json(res, status, body) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Cache-Control', 'no-store');
  res.end(JSON.stringify(body));
}

async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;   // Vercel pre-parses JSON
  const chunks = [];
  let size = 0;
  for await (const c of req) { size += c.length; if (size > 10000) throw new Error('body_too_large'); chunks.push(c); }
  try { return JSON.parse(Buffer.concat(chunks).toString('utf8') || '{}'); } catch { return {}; }
}

function keysReady(c) {
  if (!c.keyId || !c.keySecret || c.keyId.startsWith('[')) return 'razorpay_keys_missing';
  // Guardrail: live keys need an explicit founder-approved switch.
  if (c.keyId.startsWith('rzp_live_') && !c.allowLive) return 'live_keys_blocked';
  return null;
}

function rzpAuth(c) { return 'Basic ' + Buffer.from(c.keyId + ':' + c.keySecret).toString('base64'); }

const sha256 = (s) => crypto.createHash('sha256').update(String(s).trim().toLowerCase()).digest('hex');
function clientIp(req) {
  const xf = req.headers['x-forwarded-for'];
  return (xf ? String(xf).split(',')[0] : req.socket && req.socket.remoteAddress || '').trim();
}

// POST /api/create-order  {name, phone, pincode}
async function createOrder(req, res) {
  const c = cfg();
  const notReady = keysReady(c);
  if (notReady) return json(res, 503, { error: notReady });

  const b = await readBody(req);
  const name = String(b.name || '').trim().slice(0, 80);
  const phone = String(b.phone || '').replace(/\D/g, '');
  const pincode = String(b.pincode || '').replace(/\D/g, '');
  if (name.length < 2 || !/^[6-9]\d{9}$/.test(phone) || !/^560\d{3}$/.test(pincode)) {
    return json(res, 400, { error: 'invalid_input' });
  }

  const r = await fetch('https://api.razorpay.com/v1/orders', {
    method: 'POST',
    headers: { Authorization: rzpAuth(c), 'Content-Type': 'application/json' },
    body: JSON.stringify({
      amount: PRICE_PAISE, currency: CURRENCY,
      receipt: 'mrudu_' + Date.now(),
      notes: { product: CONTENT_ID, name, phone, pincode, preorder: 'refundable' },
    }),
  });
  if (!r.ok) return json(res, 502, { error: 'razorpay_order_failed' });
  const order = await r.json();
  return json(res, 200, { order_id: order.id, amount: order.amount, currency: order.currency, key_id: c.keyId });
}

// POST /api/verify-payment  {razorpay_order_id, razorpay_payment_id, razorpay_signature, fbp, fbc, source_url}
async function verifyPayment(req, res) {
  const c = cfg();
  const notReady = keysReady(c);
  if (notReady) return json(res, 503, { error: notReady });

  const b = await readBody(req);
  const orderId = String(b.razorpay_order_id || '');
  const paymentId = String(b.razorpay_payment_id || '');
  const sig = String(b.razorpay_signature || '');
  const expected = crypto.createHmac('sha256', c.keySecret).update(orderId + '|' + paymentId).digest('hex');
  const valid = sig.length === expected.length && crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(expected));
  if (!valid) return json(res, 400, { ok: false, error: 'bad_signature' });

  // Deterministic event_id: browser Pixel and CAPI send the same one, so Meta counts the sale once.
  const eventId = 'purchase_' + orderId;

  // Read the order notes back from Razorpay (trusted copy of name/phone/pincode) for CAPI matching.
  let notes = {};
  try {
    const o = await fetch('https://api.razorpay.com/v1/orders/' + encodeURIComponent(orderId), { headers: { Authorization: rzpAuth(c) } });
    if (o.ok) notes = (await o.json()).notes || {};
  } catch { /* matching data is optional */ }

  await sendCapiPurchase(c, {
    eventId, orderId,
    sourceUrl: String(b.source_url || '').slice(0, 500),
    fbp: String(b.fbp || ''), fbc: String(b.fbc || ''),
    ip: clientIp(req), ua: String(req.headers['user-agent'] || ''),
    notes,
  });

  return json(res, 200, { ok: true, order_id: orderId, event_id: eventId });
}

async function sendCapiPurchase(c, d) {
  if (!c.pixelId || !c.capiToken || c.pixelId.startsWith('[')) { console.log('[capi stub] Purchase', d.eventId); return; }
  const user = { country: [sha256('in')], client_ip_address: d.ip || undefined, client_user_agent: d.ua || undefined };
  if (d.notes.phone) user.ph = [sha256('91' + d.notes.phone)];
  if (d.notes.name) user.fn = [sha256(String(d.notes.name).split(/\s+/)[0])];
  if (d.notes.pincode) user.zp = [sha256(d.notes.pincode)];
  if (d.fbp) user.fbp = d.fbp;
  if (d.fbc) user.fbc = d.fbc;
  const payload = {
    data: [{
      event_name: 'Purchase', event_time: Math.floor(Date.now() / 1000), event_id: d.eventId,
      action_source: 'website', event_source_url: d.sourceUrl || undefined, user_data: user,
      custom_data: { currency: CURRENCY, value: PRICE_PAISE / 100, content_ids: [CONTENT_ID], content_type: 'product', order_id: d.orderId },
    }],
  };
  if (c.testEventCode) payload.test_event_code = c.testEventCode;
  try {
    const r = await fetch(`https://graph.facebook.com/${c.graphVersion}/${c.pixelId}/events?access_token=${encodeURIComponent(c.capiToken)}`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
      signal: AbortSignal.timeout(3000),
    });
    if (!r.ok) console.error('[capi] failed', r.status, await r.text());
  } catch (e) { console.error('[capi] error', e.message); }   // never block the customer's confirmation on CAPI
}

async function handler(req, res) {
  try {
    const path = (req.url || '').split('?')[0];
    if (req.method !== 'POST') return json(res, 405, { error: 'method_not_allowed' });
    if (path.endsWith('/create-order')) return await createOrder(req, res);
    if (path.endsWith('/verify-payment')) return await verifyPayment(req, res);
    return json(res, 404, { error: 'not_found' });
  } catch (e) {
    console.error(e);
    return json(res, 500, { error: 'server_error' });
  }
}

module.exports = handler;

// Local dev server: serves the static page and the API on one port.
if (require.main === module) {
  const http = require('http');
  const fs = require('fs');
  const pathMod = require('path');
  const root = pathMod.join(__dirname, '..');
  const types = { '.html': 'text/html; charset=utf-8', '.png': 'image/png', '.svg': 'image/svg+xml' };
  http.createServer((req, res) => {
    const p = (req.url || '/').split('?')[0];
    if (p.startsWith('/api/')) return handler(req, res);
    const file = p === '/' ? 'index.html' : pathMod.basename(p);
    const full = pathMod.join(root, file);
    if (!['index.html', 'policies.html'].includes(file) || !fs.existsSync(full)) { res.statusCode = 404; return res.end('Not found'); }
    res.setHeader('Content-Type', types[pathMod.extname(full)] || 'application/octet-stream');
    fs.createReadStream(full).pipe(res);
  }).listen(Number(env('PORT', 3000)), () => console.log('Mrudu on http://localhost:' + env('PORT', 3000)));
}

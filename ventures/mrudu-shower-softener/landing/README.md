# Mrudu landing page: refundable paid pre-order (Bangalore)

Status: built and checked locally with stubbed payment and tracking. **Not deployed. No real keys. No accounts created.**

## What's here

| Path | What |
|---|---|
| `index.html` | The page. One file, inline CSS/JS, no framework, no build step, no images or web fonts (~26 KB). One offer, one CTA ("Pre-order for ₹1,999"). |
| `policies.html` | Seller details, refund/cancellation, terms and privacy. **Drafts with placeholders; get a lawyer to review them.** |
| `server/server.js` | The one server file (Node 18+, no dependencies): `POST /api/create-order` (creates a Razorpay order for ₹1,999, with the price set on the server) and `POST /api/verify-payment` (checks the Razorpay signature, then sends Meta CAPI `Purchase`). Run it directly and it also serves the page locally. |
| `api/create-order.js`, `api/verify-payment.js` | One-line Vercel entry points that re-export `server/server.js`. |
| `env.example` | Environment variables the server needs. Copy to `.env` (git-ignored) or set them in the host. Not named `.env.example` because the repo's `.gitignore` ignores `.env*`. |
| `screenshots/` | Final verified state: mobile 390px and desktop 1366px. The confirmation screenshot came from a stubbed payment. |

## How the flow works

1. Page load: Pixel `ViewContent`.
2. Visitor fills in name, mobile and pincode (must start with 560). The page creates an order at `/api/create-order`, loads Razorpay Checkout (only at this point, to keep the first load fast) and opens it. Pixel `InitiateCheckout` fires when checkout opens.
3. On success, Razorpay returns the payment ID and signature, and the page sends them to `/api/verify-payment`. The server checks the HMAC signature with the key secret. It then sends CAPI `Purchase` with `event_id = purchase_<order_id>`, hashed phone, first name and pincode, plus `fbp`, `fbc`, IP and user agent.
4. Only after the server confirms does the browser fire Pixel `Purchase` with the **same** `eventID`, so Meta counts the sale once. A closed checkout, a failed payment or a rejected signature never fires `Purchase`.
5. The order record lives in the Razorpay dashboard: the order notes hold name, phone and pincode. There is no database. Collect the full delivery address by phone or WhatsApp before shipping.

## Placeholders to fill (find and replace in `index.html` and `policies.html`)

| Placeholder | Who | Notes |
|---|---|---|
| `[SHIP DATE — founder to set]` | Founder | Pick a date you can definitely hit, and allow for the smoke test plus manufacturing. Missing it triggers automatic refunds. |
| `[CONTACT EMAIL]`, `[CONTACT NUMBER]` | Founder | Needed for cancellations. These must be monitored. |
| `[SELLER LEGAL NAME / ADDRESS / GRIEVANCE OFFICER]` and the seller block in `policies.html` | Founder | Required by the E-Commerce Rules 2020 before going public. |
| `[TO BE MEASURED]` (hardness before/after) | Product | Replace with real strip or ppm readings on Bangalore borewell water, or keep the placeholder wording. |
| `[CARTRIDGE LIFE — TO BE MEASURED]` | Product | Tested litres per cartridge. Do not replace this with "2–3 months" unless testing shows it. |
| `[QUANTITY — confirm]`, `[CONFIRM thread size]`, `[CONFIRM]` | Product | How many test strips are in the box, and shower-arm compatibility. |
| `[RETURNS / DEFECTIVE PRODUCT POLICY AFTER DELIVERY]`, `[COUNTRY OF ORIGIN]`, privacy and terms text | Founder or lawyer | In `policies.html`. |
| `CONFIG.pixelId = '[META_PIXEL_ID]'` | Marketing | In the `<script>` at the bottom of `index.html`. While it is a placeholder the Pixel does not load; events go to the console as `[pixel stub]` and to `window.__mruduEvents`. |
| Env vars in `env.example` | Developer, with founder OK | `RAZORPAY_KEY_ID`/`SECRET` (**test keys**), `META_PIXEL_ID`, `META_CAPI_TOKEN`, `META_TEST_EVENT_CODE`, `META_GRAPH_VERSION` (check the current Graph API version). Live keys (`rzp_live_`) are refused unless `ALLOW_LIVE_PAYMENTS=true`. |

Also confirm: delivery within Bangalore is included in the ₹1,999. Finance's unit economics include ₹150 for shipping, packaging and fees, so the page says it is included.

## Run locally (needs Node 18+; Node is not installed on this machine)

```
cd ventures/mrudu-shower-softener/landing
node --env-file=.env server/server.js      # Node 20.6+; or set the env vars in your shell first
# open http://localhost:3000
```
Pay with Razorpay's published test cards or test UPI. Then check:
- Razorpay dashboard (Test mode) shows the order and payment.
- Meta Events Manager > Test Events, with `META_TEST_EVENT_CODE` set, shows one `Purchase` **marked deduplicated** (browser + server), and `ViewContent` / `InitiateCheckout` before it.

Opening `index.html` directly from disk works for viewing. Checkout shows "Checkout is not available right now" because there is no `/api`.

## Deploy (do not do this without founder OK via the CEO)

**Vercel (free Hobby tier):** import the `landing/` folder as the project root. Vercel serves `index.html`/`policies.html` statically and turns `api/*.js` into Node functions. Set the env vars in Project Settings > Environment Variables. No build command. *Unverified: not deployed from here.* Note that Vercel's Hobby tier terms restrict commercial use; check them, or use the Pro tier or Netlify.

**Netlify:** add `netlify/functions/create-order.js` and `verify-payment.js` that wrap the handler. Netlify's function signature differs, so this needs about 10 lines of adapter code that is not written yet. Vercel is the shorter path.

Before going live:
1. Set Razorpay to **auto-capture** payments (Dashboard > Settings > Payment capture). Otherwise authorised payments auto-refund after a few days.
2. Recommended: add a Razorpay `payment.captured` webhook as a back-up record, for customers who close the tab before verification. Not built, to keep things simple. Reconcile against the Razorpay dashboard daily during the test.
3. Fill every placeholder, then search both HTML files for `[` to confirm none are left.
4. Remove `META_TEST_EVENT_CODE`.

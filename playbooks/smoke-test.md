# Playbook: smoke test (validate CAC before inventory)

The studio's reusable method for deciding whether a product idea can acquire customers profitably **before** we buy inventory. Owners: Finance Analyst (steps 1, 5, 6), Developer (step 2), Marketing Lead (steps 3–4). CEO reviews each step; founder approves spend and launch.

## 1. Compute max affordable CAC (Finance)
From the unit economics:
- Profit per first order (P1) = net price (ex-GST if prices include GST) − landed cost − shipping/packaging/payment fees − returns/RTO allowance.
- Max CAC = P1 + (12-month repeat profit × share counted). Count 0% of unproven repeat for durables; a small share (e.g. 25%) for consumables.
- GO threshold = **70% of max CAC** (headroom because CPMs rise at scale).
- Run sensitivities: GST-inclusive pricing, COD/RTO 20–30% vs prepaid-only, CPC and CVR ranges.
- Output: `ventures/<venture>/finance/`.

## 2. Build a refundable paid pre-order landing page (Developer)
- One product, one offer, one clear CTA. Real payment (Razorpay) for a **refundable pre-order**, because paid intent beats email sign-ups.
- Honest terms on the page and at checkout: expected ship date, full refund on request before shipping, automatic refund if we miss the date, refund timeline.
- Only true, substantiable claims; no fake reviews; no medical claims; prices inclusive of taxes.
- Meta Pixel + Conversions API firing `Purchase` on confirmed payment (not button click), with deduplication. Verify a test event arrives.
- Verify with Playwright (mobile + desktop screenshots, checkout in test mode).
- Output: `ventures/<venture>/landing/`.

## 3. Plan and run a small Meta test (Marketing Lead; founder approves spend)
- Budget **~₹25k per product**, **~10 days**, target **≥25 paid pre-orders**.
- Run **at least 1 week and include a payday** (1st of the month / salary week) to avoid day-of-week and cash-cycle bias.
- 3–5 creative angles from customer research; broad targeting in the venture's geography; one optimisation event (Purchase).
- Creatives and copy pass the compliance checklist (CLAUDE.md §6, Meta ad policy, ASCI).
- Tracking sheet: daily spend, impressions, CPM, clicks, CPC, landing CVR, pre-orders, refunds.
- Output: `ventures/<venture>/marketing/`.

## 4. Optional offline test (Marketing Lead)
Cheap local check before or alongside ads (e.g. test-strip demo to residents' associations, a stall). Record pitch, people reached, paid pre-orders.

## 5. Measure CPO (Finance)
- Estimate during the test: **CPO = CPC ÷ CVR**.
- Actual: **CPO = ad spend ÷ paid pre-orders**, counting pre-orders **net of refunds**.

## 6. Decide (Finance recommends, CEO reports, founder decides)
| CPO vs max CAC | Verdict |
|---|---|
| ≤ 70% | **GO**: proceed to small inventory order |
| 70–100% | **ITERATE**: fix page/offer/creative, retest |
| > 100% | **KILL** (or rethink price/cost) |

**Small-sample rule:** at ~25 orders the CPO estimate is noisy. Only trust **GO if CPO ≤ ~65%** of max CAC and **KILL if CPO ≥ ~150%**. Anything in between: extend the test to **~50 orders** before deciding. If spend exceeds max CAC with zero orders, it is KILL.

Pre-orders overstate real demand (some people won't convert at ship time); treat a borderline GO as ITERATE.

## 7. Record
Chief of Staff logs the result in `decisions/YYYY-MM-DD-<venture>-smoke-test-result.md` and updates `ORG.md` and `ventures/README.md`.

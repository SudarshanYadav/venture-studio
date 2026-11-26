# Mrudu: shower softener (Bangalore)

Status: smoke-test ready to prepare, **ad spend blocked until cartridge capacity is measured** ([decision](../../decisions/2026-11-25-mrudu-cartridge-capacity-blocker.md)) · Priority: 1 (lead venture) · Brand name **Mrudu is a placeholder** pending trademark check.

## Product
- Resin-based (ion-exchange) shower softener that fits a standard shower arm.
- Target: Bangalore households on **hard borewell water** (scale on taps/tiles, dry-feeling skin and hair, soap that won't lather).
- Price: **₹1,999 including GST and the first cartridge**, prepaid only. Replacement cartridge price (₹599) is a **placeholder**; cartridge life is **unmeasured** and shown as `[TO BE MEASURED]` everywhere (see the [capacity decision](../../decisions/2026-11-25-mrudu-cartridge-capacity-blocker.md)).
- Bangalore-only for the test (local delivery, local proof, easy offline tests).

## Key insight
Most shower filters sold in India remove **chlorine**, not **hardness**. Bangalore borewell water problems are mostly hardness. We sell **hardness reduction**, and prove it in the box and in ads with a **hardness test strip** (before vs after the filter).

## Claims rules
- Say what we can measure: hardness (ppm / test-strip colour) before and after; cartridge life in litres/months as tested.
- **No medical claims** (hair fall, eczema, skin disease, dandruff). Avoid implying health outcomes.
- No fake reviews or testimonials. No "No.1 / best" claims without evidence.
- Honest pre-order terms: ship date, refund on request, auto-refund if we miss the date.

## Economics (finance section 0: GST-inclusive, prepaid only; assumptions until tested)
- CPO bars (per paid pre-order, net of refunds): **max CAC ₹730**, **GO ₹511**, trusted GO at ~25 orders **₹475**, trusted KILL at ~25 orders **₹1,096**.
- Old placeholder CPO ₹800 is now KILL. ₹25k / 25 orders = ₹1,000 CPO (KILL); a trusted GO needs ≥53 orders from ₹25k; extending to ~50 orders costs ~₹36–50k.
- Bars assume GST on Meta spend is reclaimed; if not, max ₹619, GO ₹433.
- See `finance/unit-economics.md` section 0, `finance/calculator.html` and the [launch-bars decision](../../decisions/2026-11-25-mrudu-launch-bars-gst-prepaid.md).

## Folders
- `finance/`: unit economics + calculator, incl. GST/prepaid scenario (DONE).
- `landing/`: refundable pre-order page (DONE; not deployed, no keys, server never run).
- `marketing/`: Meta test plan, creatives, tracking sheet, offline test (DONE); `brand/` brand kit (IN PROGRESS).

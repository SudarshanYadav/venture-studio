# Unit economics and go/no-go model: Mrudu and Lavan smoke tests

Owner: Finance · Status: planning model, nothing measured yet · Calculator: `finance/calculator.html`

Every number below is an **assumption** unless marked "measured". The calculator has the same logic, and every input can be edited.

## 0. Launch scenario: GST-inclusive, prepaid only (Mrudu) — USE THESE BARS

Added 2026-11-25. This replaces the default (0% GST, COD-style 10% allowance) numbers in sections 3–4 for the Mrudu smoke-test decision. Nothing here is measured; all inputs are **assumptions**.

### Numbers for the ad plan

| | |
|---|---|
| **Max CAC (KILL above)** | **₹730** per paid pre-order, net of refunds |
| **GO bar (70%)** | **₹511** (trust at ~25 orders only if ≤ **₹475**; KILL is certain only at ≥ **₹1,096**; in between, extend to ~50 orders) |
| **Kill-per-ad rule** | Pause an ad once it has spent **~₹730 (1× max CAC) with zero purchases**; judge ad sets on CPO only after ~3 purchases each |

CPO = Ads Manager spend ÷ paid pre-orders net of refunds. These bars assume GST on Meta spend is reclaimed as input tax credit (GSTIN on the ad account). If it is not, compare against the bars ÷ 1.18: max ₹619, GO ₹433.

### Inputs (all assumptions)

| Input | Value | Note |
|---|---|---|
| Price shown | ₹1,999 incl. all taxes | MRP rule |
| GST rate | 18% | HSN 8421 21 (water filtering/purifying apparatus) assumed; **confirm with CA**. Cartridges/resin likely also 18%. |
| Landed product cost (ex-GST) | ₹600 | Placeholder; **needs a supplier quote at our real first-batch MOQ** |
| Outbound shipping (Bangalore intra-city) | ₹70 | |
| Packaging incl. box insert + test strip | ₹40 | |
| Payment gateway (Razorpay standard) | 2% of ₹1,999 + 18% GST on fee | GST on the fee is reclaimable if GST-registered; included anyway (conservative, ₹7) |
| Pre-orders refunded later, before shipping | 10% of counted pre-orders | Razorpay keeps its fee on refunds |
| Prepaid RTO (undeliverable) | 3% | vs 20–30% typical for COD; product returns to stock |
| Post-delivery returns / defects | 5% | Loses two-way shipping, packaging, fee, and 50% of landed cost as write-off |
| Return shipping | ₹70 | |
| Repeat (cartridge) profit counted | 0% | Playbook rule for unproven durables |

### Working (formulas, ₹)

```
Net price ex-GST          = 1,999 ÷ 1.18                                   = 1,694.07
Gateway fee               = 1,999 × 2% × 1.18                              =    47.18
Margin on a kept order M  = 1,694.07 − 600 − 70 − 40 − 47.18               =   936.89

Loss per refunded pre-order (before ship) = fee                            =    47.18
Loss per prepaid RTO      = fee + 70 out + 70 back + 40 packaging          =   227.18
Loss per post-delivery return = RTO loss + 50% × 600 write-off             =   527.18
Kept share                = 1 − 10% − 3% − 5%                              =    82%

P1 per counted pre-order  = 82% × M − 10% × 47.18 − 3% × 227.18 − 5% × 527.18
                          = 768.25 − 4.72 − 6.82 − 26.36                    =   730.36
Max CAC                   = P1 + 0 (repeat counted)                        =   730.36
GO (70%)                  = 0.70 × 730.36                                  =   511.25
Trusted GO at 25 orders   = 0.65 × 730.36                                  =   474.73
KILL (100%)               = 730.36
Trusted KILL at 25 orders = 1.50 × 730.36                                  = 1,095.54
```

**Reconciliation with the earlier ≈ ₹744 (18% GST, everything else default):** ₹744.17 = 1,694.07 − 600 − 150 − 10% × 1,999. The new figure is ₹13.81 lower: fees/shipping are ₹157.18 itemised instead of ₹150 (−₹7.18), and the itemised refund/RTO/return losses total ₹206.53 instead of the flat ₹199.90 (−₹6.63). Prepaid-only cuts the RTO cost sharply, but it is offset by explicitly allowing for later pre-order refunds and post-delivery returns, which the old 10% also had to cover. In the calculator, entering GST 18, shipping/fees 157.18 and returns 10.33% reproduces ₹730 (defaults left unchanged).

### Sensitivity: landed cost ±20% and CPC × CVR

Bars by landed cost:

| Landed cost | Max CAC | GO (70%) | Trusted GO (65%) | Trusted KILL (150%) |
|---|---|---|---|---|
| ₹480 (−20%) | ₹832 | ₹582 | ₹541 | ₹1,248 |
| **₹600 (base)** | **₹730** | **₹511** | **₹475** | **₹1,096** |
| ₹720 (+20%) | ₹629 | ₹440 | ₹409 | ₹943 |

Implied CPO = CPC ÷ CVR, with the verdict at landed ₹480 / ₹600 / ₹720. G = trusted GO (≤65%), g = GO but extend to confirm (65–70%), I = ITERATE, K = KILL (extend to confirm if <150%), K! = trusted KILL.

| CPC \ CVR | 1% | 1.5% | 2% | 3% |
|---|---|---|---|---|
| ₹8 | 800 I/K/K | 533 G/I/I | 400 G/G/G | 267 G/G/G |
| ₹12 | 1,200 K/K!/K! | 800 I/K/K | 600 I/I/I | 400 G/G/G |
| ₹15 | 1,500 K!/K!/K! | 1,000 K/K/K! | 750 I/K/K | 500 G/g/I |
| ₹20 | 2,000 K!/K!/K! | 1,333 K!/K!/K! | 1,000 K/K/K! | 667 I/I/K |

Rule of thumb at base cost: GO needs **CPC ≤ ~5.1 × CVR(%)** (for example ₹10 at 2%, ₹15 at 3%). At the old placeholder (₹12 CPC, 1.5% CVR) the verdict is now **KILL**, not ITERATE.

### Cartridge repeat (information only, not in the bars)

Counted at 0%, per the playbook for an unproven durable. If 25% of 12-month repeat were counted (2 cartridges/yr at ₹599 incl. GST, 60% margin on the ex-GST price), max CAC would rise by about **₹152** (to ≈ ₹883), or only about **₹90** if each cartridge order carries its own ₹110 shipping/packaging and gateway fee.

### Budget check

25 orders cost ₹12,781 at the GO bar and ₹18,259 at max CAC. ₹25,000 buys 25 orders only if CPO ≤ ₹1,000, so the ~₹25k budget is enough to reach either a GO or a clear KILL, but a result in the 65–150% band needs ~50 orders (up to ~₹36–50k) to decide.

## 1. Assumptions

| Input | Mrudu (shower softener, Bangalore) | Lavan (electrolyte mix, 20 sachets) |
|---|---|---|
| Selling price | ₹1,999 | ₹599 |
| Landed product cost | ₹600 | ₹180 |
| Shipping + packaging + payment fees | ₹150 | ₹90 |
| Returns / undelivered-COD allowance | 10% of price (₹199.90) | 10% of price (₹59.90) |
| GST included in price | 0% (not modelled by default, see risk 1) | 0% (see risk 1) |
| Repeat order | Replacement cartridge ₹599 at 60% margin = ₹359.40 profit | Another pack at the same profit as the first order |
| Repeat frequency | 2 per year | 2.5 per year (midpoint of 2–3) |
| Repeat window counted | 12 months | 12 months |
| Share of repeat profit counted in max CAC | **0%** (repeat unproven) | **25%** (repeat unproven, but consumable) |
| Test CPC (Meta, placeholder) | ₹12 | ₹12 |
| Landing pre-order conversion rate (placeholder) | 1.5% (higher price) | 2.5% |

The CPC and CVR values are placeholders to make the model run. They are not forecasts. The test exists to replace them with measured values.

## 2. Formulas

```
Net price               = price ÷ (1 + GST%)                 (= price when GST input is 0)
Profit per order (P1)   = net price − landed cost − shipping/fees − returns% × price
Repeat profit / order   = Mrudu: cartridge price × margin%   Lavan: = P1
Repeat profit (window)  = repeat profit/order × repeats per year × (months ÷ 12)
Max affordable CAC      = P1 + repeat profit (window) × share counted%
GO threshold            = 70% × max CAC                       (headroom because CPMs rise at scale)
Test CPO                = CPC ÷ CVR                           (estimate)
                        = ad spend ÷ paid pre-orders          (actuals; overrides the estimate)
Verdict                 = CPO ≤ 70% of max → GO · 70–100% → ITERATE · > 100% → KILL
Max CPC for GO          = GO threshold × CVR
Clicks for N orders     = N ÷ CVR;   budget = clicks × CPC   (≈ N × CPO)
Payback (months)        = 0 if CPO ≤ P1, else (CPO − P1) ÷ (repeat profit/order × repeats per year ÷ 12)
```

With actuals, if spend is above zero and there are no orders, the verdict is KILL once spend exceeds max CAC (the true CPO is already higher than the spend), and NO DATA before that.

Payback follows the gross-margin payback approach in the payback-period guide. Its inputs are already profit figures, so it is not revenue-based. It counts all expected repeat profit, not just the conservative share, and assumes steady repeat orders with no churn. It is a best case. The guide warns that churn is front-loaded, so treat payback as a best case until we have cohort data.

## 3. Default outputs (checked by script and in the rendered page)

| | Mrudu | Lavan |
|---|---|---|
| Profit per order before marketing | **₹1,049.10** | **₹269.10** |
| Repeat profit in 12 months (full) | ₹718.80 | ₹672.75 |
| Repeat profit counted | ₹0 (0%) | ₹168.19 (25%) |
| **Max affordable CAC** | **₹1,049.10** | **₹437.29** |
| **GO threshold (70%)** | **₹734.37** | **₹306.10** |
| Test CPO at placeholder CPC/CVR | ₹800 (76% of max) | ₹480 (110% of max) |
| Verdict at placeholders | ITERATE | KILL |
| Max CPC that still hits GO | ₹11.02 at 1.5% CVR | ₹7.65 at 2.5% CVR |
| Clicks / budget for 25 orders | 1,667 clicks / ₹20,004 | 1,000 clicks / ₹12,000 |
| Payback incl. repeat | Paid back on the first order | 3.8 months |

## 4. Sensitivity: which CPC × CVR combinations hit GO

The cells show CPO in ₹ and the verdict: **G** = GO, I = ITERATE, K = KILL.

**Mrudu** (GO ≤ ₹734, KILL > ₹1,049)

| CPC \ CVR | 1% | 1.5% | 2% | 3% | 4% | 5% |
|---|---|---|---|---|---|---|
| ₹6 | 600 G | 400 G | 300 G | 200 G | 150 G | 120 G |
| ₹8 | 800 I | 533 G | 400 G | 267 G | 200 G | 160 G |
| ₹10 | 1,000 I | 667 G | 500 G | 333 G | 250 G | 200 G |
| ₹12 | 1,200 K | 800 I | 600 G | 400 G | 300 G | 240 G |
| ₹15 | 1,500 K | 1,000 I | 750 I | 500 G | 375 G | 300 G |
| ₹20 | 2,000 K | 1,333 K | 1,000 I | 667 G | 500 G | 400 G |
| ₹25 | 2,500 K | 1,667 K | 1,250 K | 833 I | 625 G | 500 G |

Rule of thumb: Mrudu hits GO when **CPC ≤ ~7.3 × CVR(%)**, for example ₹11 at 1.5% or ₹22 at 3%.

**Lavan** (GO ≤ ₹306, KILL > ₹437)

| CPC \ CVR | 1% | 1.5% | 2% | 3% | 4% | 5% |
|---|---|---|---|---|---|---|
| ₹6 | 600 K | 400 I | 300 G | 200 G | 150 G | 120 G |
| ₹8 | 800 K | 533 K | 400 I | 267 G | 200 G | 160 G |
| ₹10 | 1,000 K | 667 K | 500 K | 333 I | 250 G | 200 G |
| ₹12 | 1,200 K | 800 K | 600 K | 400 I | 300 G | 240 G |
| ₹15 | 1,500 K | 1,000 K | 750 K | 500 K | 375 I | 300 G |
| ₹20 | 2,000 K | 1,333 K | 1,000 K | 667 K | 500 K | 400 I |
| ₹25 | 2,500 K | 1,667 K | 1,250 K | 833 K | 625 K | 500 K |

Rule of thumb: Lavan hits GO when **CPC ≤ ~3.1 × CVR(%)**, for example ₹6 at 2% or ₹9 at 3%. Lavan needs cheap clicks *and* a strong page. At India Meta CPCs of ₹8–15 it needs a CVR of 3–5%, which is high for a cold-traffic pre-order from an unknown brand.

## 5. Sample size: is 25 orders enough?

The sample-size guide covers A/B comparisons between two arms. A smoke test is different: it measures one rate against a fixed threshold. The guide's logic still holds, though. The precision of the read depends on how many **conversions** we collect, and small samples give wide ranges.

With *n* orders, the count has a Poisson-style 95% interval. That turns into this range on the true CPO, as a multiple of the measured CPO:

| Orders collected | True CPO range (× measured) | Mrudu budget at ₹800 CPO | Lavan budget at ₹480 CPO |
|---|---|---|---|
| 25 | 0.68× – 1.55× | ₹20,000 | ₹12,000 |
| 50 | 0.76× – 1.35× | ₹40,000 | ₹24,000 |
| 100 | 0.82× – 1.23× | ₹80,000 | ₹48,000 |

How to use it:
- **25 orders per product is the minimum for a directional read, not a precise one.** At 25 orders the range is about −32% to +55%.
- **A GO at 25 orders is robust only if the measured CPO is ≤ ~65% of max CAC.** At that point even the pessimistic end (1.55×) stays below breakeven. This is close to the 70% GO line, so the 70% rule and the 25-order sample fit together well.
- **A KILL at 25 orders is robust if the measured CPO is ≥ ~150% of max CAC.**
- **If the result lands between those (roughly 65–150% of max), extend to ~50 orders** before committing inventory money.
- If ad sets or creatives are split, the 25 orders apply to the **product total**, not to each variant. Comparing variants needs far more (guide: hundreds per arm even for 50–100% lifts).
- Also from the guide: run for at least **one full week** to cover day-of-week effects, ideally through a **payday** (month start), whatever the order count.

The calculator shows this range live, on placeholders or on actuals.

## 6. Key risks to the numbers

1. **GST is probably missing, and it is the biggest swing.** If ₹1,999 / ₹599 are consumer prices that include GST (18% is likely for both; confirm the HSN codes), the defaults overstate profit. At 18% GST included:
   - Mrudu P1 is ₹744, so max CAC is ₹744 and GO is ₹521. The placeholder verdict flips ITERATE → **KILL**.
   - Lavan P1 is ₹178, so max CAC is ₹289 and GO is ₹202. Lavan then needs roughly CPC ≤ 2 × CVR(%).
   - Set the "GST included in price" input to 18 if prices are GST-inclusive. Also, GST on Meta ad spend is only recoverable if the business is GST-registered.
2. **The 10% returns/RTO allowance looks light for India COD.** COD return-to-origin often runs at 20–30%. Each RTO also costs two-way shipping, not just a share of the price. If launch orders are prepaid only, 10% is plausible. If COD is offered, model 15–20% and add reverse-logistics cost.
3. **Refundable pre-orders overstate real demand.** A refundable deposit is a weaker commitment than a delivered purchase. Expect some pre-orders to refund or cancel before shipping, so count only *paid* pre-orders net of refunds when entering actuals. Launch CVR could be lower, because a real price without the pre-order framing behaves differently, or higher, because there is no wait.
4. **Test CPMs are not scale CPMs.** Small-budget tests often get cheap early delivery to the most responsive audience. The 30% headroom is meant to absorb that. If test CPC is unusually low (below ₹6), be sceptical.
5. **Repeat is unproven and assumes 100% of buyers repeat.** "2 cartridges per year" and "2–3 packs per year" are per-customer assumptions with no churn. The max-CAC logic protects us (0% / 25% counted), but the payback figure does not: it is a best case. Mrudu's 60% cartridge margin may also not include shipping on a ₹599 order (₹90–150 shipping would cut its profit by 25–40%).
6. **Mrudu is a Bangalore-only test.** Bangalore's hard-water problem makes it a natural best-case market. National CPC and CVR could be worse.
7. **The placeholder CPC/CVR values carry no information.** Today's ITERATE/KILL verdicts come from guessed inputs. Only measured spend and orders should drive the decision.
8. **Landed cost at MOQ.** ₹600 / ₹180 assume a production-scale price. Small first batches usually cost more per unit. Check the quote at the quantity we would actually buy.

## 7. Bottom line before data

- **Mrudu has room.** About ₹1,049 per order (₹744 if GST is inside the price) supports realistic Meta CPCs at 1.5–3% CVR.
- **Lavan is tight.** ₹269 per order means paid Meta acquisition works only with cheap clicks and a strong page, or if we count much more repeat value. Counting more repeat should wait until repeat is shown in data. Consider a higher price or a bundle (for example 2 packs for the first order) so that first-order profit carries more of the CAC.

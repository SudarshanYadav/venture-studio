# Mrudu: Meta smoke-test plan (Bangalore)

Owner: Marketing Lead · Status: **draft, ready for CEO review, NOT launched** · Method: `playbooks/smoke-test.md` steps 3–4.
Brand name "Mrudu" is a placeholder pending trademark check. Nothing here has been launched, spent or published.

## 0. Blocking risk: cartridge capacity

Finance estimates a shower-sized resin cartridge may soften only **~20–60 L** of Bangalore borewell water before it is exhausted (one shower ≈ 40–80 L). If true, the product does not do the job and **every angle (A–D) is unsubstantiated**, because all of them say Mrudu "reduces hardness"; A and C (strip and lather demos) depend on it most directly, since a fresh cartridge would show a result that disappears within one shower. **Do not shoot or launch until we have measured hardness at intervals (e.g. every 50 L up to 1,000 L) on a real unit.** No copy states or implies lasting softening or a cartridge life in months. Proof figures stay `[TO BE MEASURED]` and must state the litres passed.

## 1. Thresholds (final, GST-inclusive, prepaid-only; from Finance)

| | % of max CAC | ₹ |
|---|---|---|
| Trusted GO at ~25 orders | 65% | **₹475** |
| GO bar | 70% | **₹511** |
| Max CAC | 100% | **₹730** |
| Trusted KILL at ~25 orders | 150% | **₹1,096** |

## 2. Pre-launch gates (all must be true; CEO checks, founder approves)

1. Landing page live with honest terms: price ₹1,999 incl. all taxes and first cartridge, replacement cartridge ₹599 incl. taxes, ship-by date, full refund on request before shipping, auto-refund if not shipped by that date, refund timeline, seller name/address and grievance contact (E-Commerce Rules 2020). Ad wording below must match the page exactly (`[SHIP DATE]`, refund days).
2. Razorpay live, prepaid only. Meta Pixel + Conversions API send `Purchase` on confirmed payment only, deduplicated by `event_id`; seen in Events Manager > Test Events. One real ₹1,999 test order placed and refunded end to end (exclude it from results).
3. Our own measured hardness curve on Bangalore borewell water exists (ppm vs litres passed, raw photos + video kept) **and shows softening over a realistic volume** (§0). Demos are filmed after that volume has passed, and the litres are stated in the ad. Without it, no angle can run.
4. Creatives shot and every text in §8 passes; CEO signs off.
5. Founder OK on: ₹25k spend, public landing page, trademark check on "Mrudu", start date.

## 3. Campaign setup (one campaign, one ad set)

| Setting | Value |
|---|---|
| Name | `META_Sales_BLR-Broad_Mrudu-Preorder_2026-11` |
| Objective | Sales. Conversion location: Website. Optimisation event: **Purchase**. Attribution 7-day click / 1-day view. |
| Budget | Campaign budget **₹2,500/day**. Account spending limit **₹25,000** as a hard cap. Do not change the budget mid-test (it resets learning). |
| Location | Bengaluru, "people living in this location", limited to the pincodes we deliver to (match landing checkout). |
| Audience | Broad: age 25–65+, all genders, Advantage+ audience on, **no interests**, no lookalikes (no customer data yet). |
| Placements | **Advantage+ placements**: cheapest reach on a small budget; creatives ship in 4:5 and 9:16 so every placement has a fitting asset. |
| Ads | 4 ads, one per angle (A–D). Each ad carries 2 primary texts + 2 headlines as text options (see `creatives.md`). CTA button: **Pre-order** (or **Shop now** if unavailable). Link description: "Ships by [SHIP DATE]. Full refund before shipping." |
| UTMs | `utm_source=meta&utm_medium=paid&utm_campaign=mrudu-smoke&utm_content={{ad.name}}` |

Expect "Learning limited" (about 3 purchases/day is far below Meta's ~50/week). That is fine for a test; do not restructure because of it.

## 4. Schedule and pacing (includes a payday)

₹2,500/day × 10 days = **₹25,000**.

| Day | Default date | Note |
|---|---|---|
| 1–4 | Fri 27 Nov – Mon 30 Nov | Learning; no per-ad changes before day 3 |
| 5 | **Tue 1 Dec (payday)** | Salary week runs ~30 Nov – 5 Dec |
| 6–10 | Wed 2 Dec – Sun 6 Dec | Decision after day 10 |

Default start Fri 27 Nov **if all gates pass**; latest start that still covers payday week is **Mon 30 Nov**. If gates slip past that, founder chooses: wait for the next payday (late Dec, holiday-distorted) or a clean late-January window. Never end before day 7 or before payday has passed, except the zero-order KILL rule in §6.

## 5. Budget maths (reconciles with Finance)

- Spend ≈ orders × CPO; clicks needed = orders ÷ CVR. Finance placeholders: CPC ₹12, landing CVR 1.5%.
- ₹25,000 ÷ ₹12 = **2,083 clicks** × 1.5% = **31 orders** → CPO ₹800 (matches Finance placeholder; 110% of max CAC, i.e. the "extend" zone).
- 25 orders needs 25 ÷ 1.5% = 1,667 clicks × ₹12 = **₹20,000**, inside the ₹25k.
- To hit the ₹511 GO bar: at CPC ₹12 we need CVR ≥ **2.35%**; at CVR 1.5% we need CPC ≤ **₹7.67**.
- **GST on ad spend:** Meta bills Indian advertisers 18% GST on top. Without a GSTIN to claim input credit, ₹25,000 of spend costs ₹29,500 cash. Founder decides: (a) ₹25k spend + GST, or (b) ₹21,200 spend so cash out = ₹25k. CPO uses spend ex-GST only if the GST is recoverable.

## 6. Decision rules

**Source of truth for orders = Razorpay, net of refunds**, not Ads Manager. Decision CPO = cumulative spend ÷ cumulative net pre-orders.

### Test-level (playbook step 6, exact)
| Net pre-orders | Rule |
|---|---|
| 0 and spend > ₹730 (max CAC) | **KILL** (after confirming tracking and checkout work, §7). See risk note below. |
| < 25 at end of budget | CPO > ₹1,000 already. KILL if CPO ≥ ₹1,096; otherwise extend toward ~50 orders (founder OK on extra spend). |
| ~25–49 | **GO only if CPO ≤ ₹475**; **KILL only if CPO ≥ ₹1,096**; anything between → **extend to ~50 orders**. |
| ~50+ | **GO ≤ ₹511** (≤70%) · **ITERATE ₹511–730** (70–100%) · **KILL > ₹730** (>100%). A borderline GO is treated as ITERATE (pre-orders overstate demand). |

Quick lookup at the full ₹25,000: **≥53 net orders → GO** (CPO ≤ ₹472) · **23–52 → extend** (50–52 is a borderline GO, treat as ITERATE) · **≤22 → KILL** (CPO ≥ ₹1,136).
Extending to ~50 orders costs **~₹36–50k in total** (Finance), i.e. ₹11–25k beyond this budget. Needs founder OK before spending.

**Risk note on the zero-order rule:** if true CPO were at the GO bar (₹511), seeing zero orders by ₹730 of spend happens ~24% of the time (Poisson, e^-1.43). Applying it at 2× max CAC (₹1,460) cuts that to ~6%. Proposed amendment for CEO/founder before launch; until then the playbook rule stands.

### Per ad (in ₹ spend, tied to max CAC ₹730)
| Condition | Action |
|---|---|
| Ad spend < ₹730 or day < 3 | Leave it. |
| Ad spend ≥ **₹1,460** (2× max CAC) and 0 purchases | Pause. |
| Ad spend ≥ **₹2,190** (3× max CAC) and ad CPO ≥ ₹1,096 | Pause. |
| Ad CPO ≤ ₹730 | Keep. |
| Meta barely spends on an ad (< ₹500 by day 4) | Leave it; Meta has de-prioritised it, it costs little. Note it as "no read". |

Always keep ≥ 2 ads live. Never edit a live ad (resets learning); to replace, add a new ad with a new hook on the best angle. With ~₹6k per ad, angle comparisons are **directional only**; the verdict is on blended CPO.

## 7. If Pixel / CAPI isn't firing

- **Razorpay has orders, Meta shows 0 Purchases:** tracking broken. Do not judge ads on Meta numbers. Fix within 24h (Developer: Events Manager diagnostics, CAPI token, `event_id` dedup). If not fixed within 24h, **pause the campaign**: Meta is optimising blind.
- **Meta shows Purchases, Razorpay doesn't:** event firing on click or page load, or duplicating. Pause, fix, re-verify with Test Events.
- **Meta Purchases ≈ 2× Razorpay:** deduplication broken; fix before trusting per-ad CPO.
- After any fix, place one test order and refund it. Log the outage dates in `tracking.csv`.

## 8. Daily check (10 minutes, same time each morning)

1. Spend yesterday vs ₹2,500; any disapproved or limited ads.
2. Razorpay orders and refunds vs Meta Purchases (§7 if they diverge by > 1).
3. Fill one row of `tracking.csv` (yesterday).
4. Apply per-ad rules (§6). Frequency > 2.5 on an ad: watch; > 4: pause.
5. Comments: hide spam; answer questions only with facts already on the landing page (price, ship date, refund terms). No new claims.
6. Cumulative CPO vs §6 bars. Send CEO a one-line update.

## 9. Compliance review (every ad text)

Checks: **C1** no personal-attribute phrasing ("Do you have…", "your hair/skin") · **C2** no health/medical or implied body outcome (hair fall, skin, eczema, dandruff) · **C3** no before/after body imagery · **C4** only measurable claims (hardness, strip, lather demo) · **C5** no fake reviews, ratings, counts, "No.1/best" · **C6** no fake urgency/scarcity (CCPA dark patterns) · **C7** price shown incl. taxes · **C8** ASCI substantiation on file.
P = pass. P* = pass **only once** the bracketed placeholder is filled from our own measured test/source. N/A = no price in a headline (price is in every primary text of the same ad).

| ID | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
|---|---|---|---|---|---|---|---|---|
| A-PT1 strip proof | P | P | P | P* | P | P | P | P* |
| A-PT2 strip ppm | P | P | P | P* | P | P | P | P* |
| A-HL1 "See the hardness drop on a strip" | P | P | P | P* | P | P | N/A | P* |
| A-HL2 "A shower softener you can test" | P | P | P | P | P | P | N/A | P |
| B-PT1 chlorine vs hardness | P | P | P | P | P | P | P | P* |
| B-PT2 which filter | P | P | P | P | P | P | P | P |
| B-HL1 "Built for hardness, not chlorine" | P | P | P | P | P | P | N/A | P |
| B-HL2 "For hard borewell water in Bangalore" | P | P | P | P | P | P | N/A | P |
| C-PT1 shake test | P | P | P | P* | P | P | P | P* |
| C-PT2 lather | P | P | P | P | P | P | P | P |
| C-HL1 "The 10-shake lather test" | P | P | P | P* | P | P | N/A | P* |
| C-HL2 "Same soap. Softer water." | P | P | P | P* | P | P | N/A | P* |
| D-PT1 white crust | P | P | P | P | P | P | P | P |
| D-PT2 scale on fittings | P | P | P | P | P | P | P | P* |
| D-HL1 "White crust on the shower head?" | P | P | P | P | P | P | N/A | P |
| D-HL2 "Tackle hardness at the shower" | P | P | P | P | P | P | N/A | P |
| Link description | P | P | P | P | P | P | N/A | P* |

**Result: 0 fails; 9 items conditional (P*) on evidence we do not have yet.** Every "reduces hardness" line (all primary texts) is also conditional on the cartridge-capacity result in §0; no text states or implies lasting softening or cartridge life. Imagery: strips, bottles, taps and shower heads only; no people's skin or hair, no before/after of bodies.

### Claims register (evidence needed before launch)
| Claim | Evidence | Status |
|---|---|---|
| Mrudu reduces hardness; "[TO BE MEASURED] ppm before/after, after [TO BE MEASURED] litres" | Hardness vs litres curve on a real unit, Bangalore borewell water, dated, raw photo/video kept. Finance flags capacity may be only ~20–60 L (§0) | **MISSING; blocks all angles** |
| Cartridge life (litres/months) | Same curve. Not claimed anywhere in ads; no "2–3 months" | Not claimed |
| "Unedited" / "same tap, same day" | Raw footage files saved in `marketing/evidence/` | MISSING (shoot) |
| Shake-test result shown in video | Raw footage, same soap and volume, filmed in one take | MISSING (shoot) |
| Bangalore borewell water is often hard (B-PT1) | Public groundwater-quality source (e.g. CGWB/KSPCB report for Bengaluru Urban) | **MISSING**; else delete that sentence |
| Ion-exchange resin is the method used in home softeners | Standard water-treatment chemistry; supplier spec sheet | Supplier spec needed |
| Hard water reduces soap lather; limescale = calcium/magnesium | Standard chemistry (textbook reference) | OK |
| Fits a standard ½-inch shower arm | Supplier spec + our fit test | MISSING |
| ₹1,999 incl. taxes and first cartridge; cartridge ₹599 incl. taxes | Price list / landing page | OK (matches brief) |
| Ships by [SHIP DATE]; full refund before shipping; auto-refund if late | Landing terms | Fill from landing |
| Many shower filters target chlorine (B) | Screenshot log of 10 top shower-filter listings on Amazon.in showing what each claims to remove | MISSING (30 min) |

Phrases rejected while drafting (do not reintroduce): "Do you have hard water damage?", "softer hair/skin", "stops hair fall", "No.1 shower softener", "only a few left", "X families already switched", "no more scale", "lasts 2–3 months", "soft water every day".

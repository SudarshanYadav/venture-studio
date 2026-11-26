# Mrudu (resin shower softener): market research, India and UAE
Date: 2026-11-26 | Researcher: Market Researcher (opus, CEO exception for a foundational go/no-go) | Stage: **deep dive (Stage 2)**, replacing the snippet-only screen of the same date | Currency: INR and AED; ₹85/USD (studio), AED 3.6725/USD peg, so ₹23.14 per AED (2026-11-26). Indian shelf prices are tax-inclusive (MRP rule); Amazon.ae prices as listed (VAT-inclusive assumed).
Companion files: `competitors.md`, `customer-voice.md`, `bench-test-spec.md`, `sources.md`, `calc/stage2_calc.py` (+ `_output.txt`), `research/countries/india.md`, `research/countries/uae.md`.

## 0. Verdict
**NO-GO for Mrudu as specified** (a ₹1,999 shower-arm resin cartridge plus ₹599 refills, sold on "hardness reduction, proven with a test strip"). **Country: neither** for this product. Confidence: **Medium-High** on the physics, Medium on the market.
- **Deciding number: a shower-arm cartridge would be pushing water through its resin 26 to 150 times faster than softening resin is rated for** (6 to 10 L/min through 0.1 to 0.35 L of resin = 1,000 to 6,000 bed volumes per hour, against a rated 8 to 40). Even ignoring flow, it would hold enough capacity for only **12 to 166 L** at Bengaluru borewell hardness (200 to 600 mg/L), which is **0.2 to 3 showers**. Full-flow softening needs about **12 L of resin**, a small softener tank, not a cartridge. (Purolite datasheet and Pure Water Products table, opened; arithmetic in `calc/stage2_calc.py`.)
- **Market confirms it, unprompted:** every Indian brand checked (WaterScience, RiverSoft, Purifit) calls its product a "conditioner" on its own pages. RiverSoft's DIVA-01 page says it "does not chemically soften water". No resin shower product was found in India.
- **SOM (12 months, Bangalore) if the product worked: 330 to 1,330 orders (₹6.6 to 26.7 lakh)**, channel-limited. At the GO bar (CPO ₹511), ₹50k/month net needs **about 228 orders a month**, 2 to 8 times that SOM, with zero honest cartridge repeat. The provisional income target fails even before the physics.
- **Kill-criteria scorecard:** must-pass #1 (income) FAIL, #8 (claim risk) FAIL; #6 (wedge) FAIL. Rule: any must-pass FAIL = NO-GO.
- **The one assumption that would change this:** that a shower-arm resin cartridge softens at least about 1,500 L at full flow. Physics says no. Cheapest honest check: the loose-resin column run in `bench-test-spec.md` (about ₹1 to 1.5k: resin plus a titration kit; needs founder OK). The full ₹3.5 to 6k test is no longer needed to kill; it is needed only to reopen.
- **What survives:** the demand and the insight. Buyers in Bengaluru are angry that hard-water filters "do nothing" and try to prove it with TDS meters. A product that really softens a bathroom's water, proven with a strip, is an open position. It needs a different product: a **bathroom-scale, salt-regenerated softener (about 5 to 15 L of resin) for owner-occupied Bengaluru borewell homes**, priced between the ₹2.8k conditioners and the ₹15k to ₹1.4L installed softeners. That is a new venture idea and needs its own Stage 1 screen before any spend (§13).

## Changed since the snippet screen
| Stage 1 item | Stage 1 value | Now | Status | Source (opened unless noted) |
|---|---|---|---|---|
| Verdict | PARK, India; UAE KILL | **NO-GO** for this product; UAE KILL stands for this product | Changed | This report |
| Cartridge capacity | Finance estimate 20 to 60 L ("about one shower"), unmeasured | 12 to 166 L, and flow 26 to 150x over the resin rating, so softening at full flow is unlikely from the first minutes | Confirmed and worsened | Purolite C100E; Pure Water Products; BV/h ranges (snippets) |
| Competitors' mechanism | "mostly chlorine removal" (inferred) | Brands say "conditions hard water"; media KDF, calcium sulphite, polyphosphate; "does not chemically soften water" (RiverSoft) | Changed (now observed) | waterscience.in, theriversoft.com, purifit.in feeds |
| Bengaluru hardness range | 48 to 1,540 mg/L (DMG) | 48 to 1,540 mg/L Urban, 72 to 1,416 Rural | Confirmed | Deccan Herald 2011-05-13 |
| Samples above 600 mg/L | "51 samples" | **8.5% of 2,209** samples (pre-monsoon 2010) | Changed | India Water Portal (DMG 2011 report) |
| Share above 200 mg/L | 40 to 60% (assumption) | 45 to 60% (DMG: 45% within desirable, so about 55% above) | Changed, still snippet for the 45% | Search snippet of DMG figure |
| Borewell dependence | 45% (DH) | 45% confirmed, but from **2016**; Cauvery V (Oct 2024) now reaches 104 of 110 peripheral villages, with 89,000 connections vs a 3 lakh target (Apr 2025) | Confirmed, dated; trend down | DH 2016-04-24; Citizen Matters 2025-04-07; DH 2026-04-28 |
| Mixed Cauvery + borewell above 200 mg/L | 24% of households (2018) | Same | Confirmed | Citizen Matters 2025-05-05 |
| SEI water-source split 26% / 36% | snippet | snippet | Still unsourced (not reopened) | |
| Bengaluru households 3.0 to 3.8M | my assumption | still assumption; BBMP 20 to 22 lakh properties is a floor (snippet) | Still unsourced | |
| CLEO price | ₹2,139 to 2,795 | ₹1,390 to 2,795 (Flipkart, site); cartridge **₹845** (₹1,595 for 2), life "4-6 months" | Changed | Flipkart, waterscience.in |
| CLEO hair-fall claim | "claims reduce hair fall" | Site badges "Reduces Hairfall", "Protects Skin" | Confirmed | waterscience.in |
| RiverSoft price | ₹1,318 to 1,449 (MRP 4,999) | ₹1,440 to 1,799 on Flipkart; cartridge about ₹684 | Changed | Flipkart; theriversoft.com |
| SNIX and generics | ₹678 to about 1,500 | Snix ₹943; generics ₹400 to 950 | Changed | Flipkart |
| Hello Klean FAQ "no shower filter removes calcium" | snippet | still snippet (helloklean.com, waterfilterguru.com unreachable from this session) | Still unverified | |
| India Meta CPC / CPM | ₹8 to 25 / ₹50 to 120 | Same (agency client data, Low) | Confirmed (page opened) | owlclaw.com |
| UAE shelf prices | AED 35 to 99 | Generic AED 17 to 157; **premium AED 229 to 380 exists and sells** (blu Ionic AED 339, "1K+ bought in past month") | Changed | Amazon.ae search |
| UAE Meta CPC | $0.70 to 2.15 | about $1.0 (Dec 2025) to $1.65 (Sep to Nov 2025) | Narrowed | superads.ai UAE |
| Dubai hardness | 150 to 250 mg/L (vendor) | still vendor; EGA (not DEWA) potable water 25 to 70 mg/L; no DEWA figure | Still Unknown | ThisDayLive (snippet), ega.ae |
| GST | 18%, HSN 8421 (assumed) | **18%**: heading 8421 is in Schedule II of Notification 9/2025-IT(Rate) as amended to 30-04-2026 | Confirmed | ICAI consolidated notification |
| BIS QCO | none found (search) | none on the BIS compulsory list; only RO point-of-use (IS 16240) | Confirmed (observed) | bis.gov.in |
| UAE trade licence | AED 10 to 30k | AED 6.5 to 10k licence + AED 15 to 25k office (vendor), TDRA NOC; advertiser permit regime from Feb 2026 | Changed, still Low | snippets |
| India softener market USD 114 to 128M | abstracts | not reopened | Still abstract-only | |

## 1. Market definition
Bengaluru households on hard borewell, tanker or mixed water who want to reduce hardness in bathing water, buying a no-plumber, tax-inclusive shower-arm product at ₹1,400 to 2,800 with refills. Out of scope: drinking water (RO), whole-house installed softeners (except as substitutes), health outcomes, UAE (§8).

## 2. Market potential
| | India (Bengaluru) | UAE | Method | Confidence | Source |
|---|---|---|---|---|---|
| TAM (households with the problem) | **0.61 to 1.41M** households; ₹121 to 283 crore one-time at ₹1,999 | Not sized (no hardness distribution; product fails physics anyway) | Bottom-up | Low-Medium | DH 2016; DMG 2011; household count assumed |
| SAM (has a shower arm, no softener, reachable) | **0.36 to 1.13M** households | | TAM x 60 to 80% (assumption) | Low | |
| Category flow, India (all cities) | top-9 Flipkart listings: **6,879 ratings = about 1.4 to 6.9 lakh units lifetime** (at 1 to 5% ratings per unit); WaterScience's own "1.5 million customers" claim implies ₹38 to 75 crore a year for that brand if spread over 4 to 8 years | | Competitor-led | Low | Flipkart; waterscience.in |
| SOM, 12 months, if the product worked | **330 to 1,330 orders, ₹6.6 to 26.7 lakh** | not sized | Channel-led: ₹2 to 4 lakh ad spend / CPO ₹450 to 730 x 1.2 to 1.5 organic | Low | finance §0 |
| SOM, honest, product as specified | **about 0** | 0 | Claim cannot be made (§3a) | Medium-High | |

**Arithmetic** (script output in `calc/stage2_calc_output.txt`): TAM = 3.0 to 3.8M households x 45 to 62% groundwater-dependent x 45 to 60% above 200 mg/L. SAM = TAM x 0.6 to 0.8. SOM = 2,00,000 / 730 x 1.2 = 329 up to 4,00,000 / 450 x 1.5 = 1,333.
**Methods compared:** bottom-up (potential stock, 0.36 to 1.13M SAM households) and competitor-led (actual national flow, about 1.4 to 6.9 lakh lifetime units on nine Flipkart listings) measure different things; they agree that the category is real and large relative to our goal. The penetration cross-check (0.3 to 1% of SAM = 1,100 to 11,300 orders) is 3 to 9 times the channel-led SOM. That gap is explained, not an error: our ad budget, not demand, caps the SOM. **Biggest swing factor:** whether the product works at all; then CPO.
**Market attractiveness (/50):** India **27** (demand 4, budget 4, competitive weakness 3, reach 3, channel 3, urgency 2, proof 1, execution risk 2, speed 3, fit 2) = "validate first", and proof scores 1 because the shower form cannot prove what it would sell. UAE **22** (demand 3, budget 4, weakness 2, reach 3, channel 2, urgency 2, proof 1, risk 2, speed 2, fit 1).

## 3. Customers and demand
**Who buys (observed in 181 Flipkart reviews and 5 on-site reviews):** a national buyer base. Bengaluru is the largest single city (28 of 181, 15%). Reasons to buy are hair and skin (27 of 82 positive reviews), lather and scale. Renters and PG residents appear. Full quotes, verbatim with links: `customer-voice.md`.
**The pain in their words:** "No change to water after usage. Hardness remains the samw" (Bengaluru, 1 star). "The TDS before this 600, after this 600. Don't buy it" (Hyderabad). "It requires a very slow water flow to work properly" (Pune). "If you are in Bengaluru ..you need to have it" (5 stars).
**What they do today:** buy a ₹400 to 2,800 conditioner; use liquid "instant softener" in a bucket (₹209 to 575, Flipkart); clean scale with sprays; or, if owners and well-off, buy an installed softener (WaterScience RENO from ₹34,995; Kent, snippet ₹14,949 to 30,500).
**Search demand:** not measured (no keyword tool; Google Trends not opened). Flipkart shows 13,079 results for "shower filter for hard water" and 3,478 for "water softener for bathroom resin".
**Unprompted demand for proof (High confidence, 5+ independent reviewers):** buyers measure with TDS meters and conclude the product fails. Brands answer with "filters do not reduce TDS". Nobody shows a hardness number.

### 3a. Does a shower resin softener actually work? (brief item 4)
| Evidence | Says | Confidence |
|---|---|---|
| Resin chemistry: 1.9 eq/L total capacity = 95 g CaCO3 per L resin (Purolite C100E, opened); working 73 g/L (Pure Water Products, opened) | Capacity is fixed by resin volume | High |
| Cartridge resin volume 0.1 to 0.35 L | **Assumption**; no supplier spec found. Bench test measures it | Low |
| Litres softened = volume x capacity / hardness | 12 to 166 L at 200 to 600 mg/L, so 0.2 to 3 showers (script §2) | Medium |
| Service flow rating 8 to 40 BV/h (Purolite C100, Resinex KW-8, Lewatit S1567; Amberlite SR1L 5 to 50) | Shower flow is 26 to 150x over the rating; hardness leaks from the start | Medium-High (snippets, four sheets agree) |
| Larger real cartridge (2.5 x 9.75 in, about 0.6 L): 57 L at 684 mg/L, 170 L at 256 mg/L (Pure Water Products, opened) | Even 2 to 3 times a shower cartridge's resin gives 1 to 3 showers | Medium-High |
| Indian brands' own wording: "conditions", "does not chemically soften water" | Market players do not claim softening | High (observed) |
| Independent lab tests (waterfilterguru) | KDF filters left hardness unchanged; a resin "Shower Stick" softened (single tests) | Low (snippet only; site unreachable) |
**Conclusion:** a shower-arm resin cartridge can soften, at best, the first litres of a shower at Bengaluru hardness, and the strip demo would show exactly that. Selling it on "hardness reduction" with a ₹599 refill every few months would be a claim we cannot substantiate (ASCI Chapter I) and a refill model that cannot work. This is consistent with why no Indian brand sells one.

## 4. Competition
Full table: `competitors.md`. Summary:
| Player | Price (₹, incl. tax) | Cartridge | Claim | Ratings (Flipkart) |
|---|---|---|---|---|
| WaterScience CLEO (Bengaluru) | 1,390 to 2,795 | 845; 4 to 6 months | "conditions hard water"; badges "Reduces Hairfall" | 4,381 (3.83); 226 (3.88) |
| RiverSoft SF-15, DIVA | 1,440 to 2,049 | about 684; 4 to 6 months | "does not chemically soften water" (DIVA-01) | 924 (3.93); 442 (3.97) |
| Purifit | 999 to 1,899 | 699 to 849 | polyphosphate conditioning; "98.1% scale reduction" | 356 (4.36) |
| Snix | 943 | not observed | "Hard Water Softener" | 308 (3.70) |
| Generics | 400 to 950 | | "softener", "reduces hair fall" | under 50 each |
| Installed softeners | 14,949 (snippet) to 1,39,995 | salt | real softening | |
**Whitespace:** measured, honest hardness reduction for bathing water. **Their strengths we cannot match:** WaterScience's Bengaluru base, borewell SKU, store network, installed-softener line and salt delivery in Bengaluru. **Copy threat:** high for any cartridge. **Defensibility:** low (shower form); medium at best for a bathroom-scale unit.
**Substantiation check (brief item 2):** none of the three brands publishes a hardness before/after number. Purifit publishes a scale-reduction lab result (report not opened). WaterScience suggests a "lather test". 1 to 2-star share is 9 to 23% across six listings.

## 5. Pricing benchmarks
Ladder (India, tax-incl.): liquid softener ₹209 to 575; generic heads ₹400 to 950; branded conditioners ₹943 to 1,899; premium conditioners ₹2,295 to 4,695; installed softeners ₹14,949 to 1,39,995. Cartridges ₹684 to 849, claimed life 2 to 6 months. MRP anchoring with 30 to 88% "off" is universal. Mrudu's ₹1,999 + ₹599 is inside the band; WTP for a conditioner is proven at ₹1.4k to 2.8k. **WTP for real softening at ₹5k to 15k is Unknown**: it is the first question for the pivot.
UAE (Amazon.ae): generic AED 17 to 157; premium AED 229 to 380 (₹5,300 to 8,800); cartridges AED 79 to 149.

## 6. Channels and acquisition cost
| | India (Bengaluru) | UAE |
|---|---|---|
| CPC | ₹8 to 25 all-industry; Instagram feed ₹14 to 28, Reels ₹8 to 18 (owlclaw, agency data, Low) | about $1.0 to 1.65 = AED 3.7 to 6.1 (superads, Low) |
| CPM | ₹50 to 120 (Low); superads shows a +540% month jump into Jul 2026 (volatile) | not re-checked |
| CVR | 1 to 3% (assumption) | 1 to 3% (assumption) |
| Implied CPO | ₹267 to 2,800; central ₹12 / 1.5% = ₹800 (KILL) | AED 122 to 606 |
| Max CAC (finance §0) | ₹730; GO ₹511 | not modelled; at AED 229 price a CPO of AED 122 to 200 might fit, Unknown |
Marketplaces: Flipkart and Amazon.in dominate and carry the incumbents' rating moats; D2C via Meta is the only test route that does not compete on ratings from day one. Communities (Bengaluru apartment and RWA groups) are the cheapest reach but need founder OK to post.

## 7. Regulatory and compliance snapshot (verify with a professional before launch; I am not a lawyer)
| Item | India | Source, date | Blocker? |
|---|---|---|---|
| BIS compulsory certification | Not on the BIS Scheme-I compulsory list (observed 2026-11-26); only RO drinking systems (IS 16240) | bis.gov.in, opened | No |
| GST / HSN | 18% (heading 8421 in Schedule II, Notification 9/2025-IT(Rate) as amended to 30-04-2026); cartridges as parts of 8421 assumed 18% | ICAI compilation, opened | No; confirm HSN with CA |
| Legal Metrology | Rule 6(1) label: maker/packer/importer name and address, generic name, count, month/year of manufacture, MRP "inclusive of all taxes", consumer care; 6(10) same on the website; 6(10-A) country of origin for imports; Rule 27 registration as packer/importer, ₹500, within 90 days | Khaitan consolidated rules to 13-02-2026, opened | No (days, ₹500) |
| E-Commerce Rules 2020; CCPA misleading-ads (2022) and dark-patterns (2023) guidelines | Grievance officer, seller details, no false urgency or fake "MRP off" | consumeraffairs.nic.in **not reachable**; from prior knowledge, unverified | No, if followed |
| ASCI Code Chapter I | Claims "capable of substantiation" | ascionline.in, opened | **Yes for "softens water" on a shower cartridge**: we could not substantiate it beyond the first litres |
| Health claims | Not allowed (CLAUDE.md §7). UK ASA upheld complaints against a real softener's "glossier hair" and "softer skin" (A19-565203) and a conditioner's "improve certain skin conditions" (A25-1314135) | asa.org.uk, opened (UK, persuasive) | Avoid entirely |
| Trademark "Mrudu" | Not searched | | Open |
UAE: see `research/countries/uae.md` (trade licence, VAT 5%, Media Council advertiser permit from about 1 Feb 2026; MOIAT conformity not checked).

## 8. India vs UAE
| Dimension | India (Bengaluru) | UAE | Winner |
|---|---|---|---|
| Problem size | Borewell hardness 48 to 1,540 mg/L; 8.5% of samples above 600 | Desalinated, remineralised; hardness Unknown, likely lower | India |
| Customer value per order | ₹1.4 to 2.8k conditioners | Premium AED 229 to 380 (₹5.3 to 8.8k) sells | UAE |
| Competition | Dense, Bengaluru incumbent | Dense, global brands (blu, Philips, Hello Klean) | Neither |
| Paid CAC | CPO central ₹800 vs max ₹730 | CPO AED 122 to 606 | Unclear |
| Physics | Fails worst (high hardness) | Fails on flow; capacity 2 to 4x better at lower hardness | Neither |
| Setup | No entity change | Licence AED 6.5 to 10k + office; permit rules | India |
| Founder fit | Local tests in Bengaluru | Remote | India |
| **Overall for this product** | **NO-GO** | **NO-GO** | Neither |
UAE re-check (brief item 7): the KILL stands for this product, but the reason changed. It is no longer "the price ceiling is AED 99": a premium tier exists. It is that the product cannot do what it would claim, and setup costs and permits add risk. If the studio ever builds a working bathroom-scale softener, the UAE is still a poor fit (villas own the plumbing but have lower hardness; apartments are rented).

## 9. Launch plan (first 90 days): not a launch, a decision path
| Days | Step | Cost | Founder OK? |
|---|---|---|---|
| 0 to 7 | Founder decides: accept NO-GO on the shower form, or run the loose-resin column check first (bench spec Run C) | ₹1 to 1.5k | Yes (spend) |
| 0 to 7 | Stop all Mrudu landing, brand and ad work (quality-audit rework is no longer needed for this form) | ₹0 | CEO |
| 7 to 21 | Stage 1 screen of the pivot: bathroom-scale regenerable softener for owner-occupied Bengaluru borewell homes (supplier landed cost, install model, WTP evidence, competitors Kent/WaterScience/Pentair/local) | ₹0 | CEO confirms |
| 21 to 45 | If the screen passes: supplier quotes and 1 sample unit; bench test at full flow (bench spec runs A and B) | ₹8 to 15k (sample, Low) | Yes |
| 45 to 90 | If it passes: refundable pre-order smoke test, Bengaluru borewell zones, ₹25k ad cap (playbooks/smoke-test.md) | ₹25k | Yes |
Kill checkpoints: day 7 (founder decision), day 21 (pivot screen), day 45 (unit fails 1,500 L or landed cost leaves no margin at ₹6 to 12k), day 90 (CPO vs new bars).

## 10. Growth potential
- Shower form: no honest repeat (a cartridge that lasts a shower cannot be refilled at ₹599 profitably or honestly). Ceiling: 0.
- If a working product existed at ₹1,999: Bengaluru month-12 net about ₹10 to 26k/month from showers at CPO ₹511 to 600 (screen arithmetic, unchanged), far below ₹50k.
- Second cities (brief item 6): Hyderabad is harder still (hardness above the permissible limit in 75 to 84% of 44 samples, 2023; TNM 2026-09-14). Pune PCMC basalt groundwater 220 to 360 mg/L (MPCB 2014). Chennai coastal mean about 286 mg/L, Perungudi 610 to 675 (snippets, 2011). The problem is national, and so are the incumbents. Multi-city does not rescue the shower form; for the pivot, Hyderabad is the natural second city (worse hardness, borewell and tanker reliance, snippet).
- Pivot ceiling (illustrative only, all assumptions): at ₹2 to 4k contribution after CAC per installed unit, ₹50k/month needs 13 to 25 units a month. Plausible only if WTP and install logistics hold.

## 11. Economics fit
Finance bars (section 0 of `finance/unit-economics.md`): max CAC ₹730, GO ₹511 per paid pre-order; contribution per kept order ₹937 before refunds; landed cost ₹600 is still a placeholder. For ₹50k/month net at CPO ₹450 / 511 / 600 the shower product needs 178 / 228 / 384 orders a month (script §9) against a Bengaluru channel SOM of 27 to 111 a month. Hand-off to Finance Analyst only if the pivot passes its screen: new bars for a ₹6 to 15k installed product.

## 12. Kill-criteria scorecard
| # | Criterion | Result | Number and source |
|---|---|---|---|
| 1 | Side-income size (must) | **FAIL** | Needs about 228 orders/month at GO CPO; SOM 27 to 111/month (script §9); no honest cartridge repeat |
| 2 | Test affordability (must) | PASS (moot) | ₹25k ad cap; inventory MOQ unknown |
| 3 | CAC feasibility (must) | India PASS at optimistic end only (₹267 vs ₹730); UAE UNKNOWN at premium price | owlclaw, superads; finance §0 |
| 4 | Regulatory blocker (must) | PASS (India) | No BIS QCO; LM registration ₹500; GST 18% |
| 5 | Margin ≥35% | PASS (model) | Finance §0, 47% before refunds |
| 6 | Competition wedge | **FAIL** | Wedge depends on a claim the product cannot back; incumbents at same price with 4,381-rating listings |
| 7 | Demand evidence | PASS | 181 verbatim reviews; 13,079 Flipkart results; Bengaluru 15% of sample |
| 8 | Claim risk (must) | **FAIL** (Medium-High) | Capacity 12 to 166 L, flow 26 to 150x over rating; ASCI Chapter I |
| 9 | Concentration | PASS | Not applicable at this stage |
Result: 2 must-pass FAIL (1, 8) and 1 non-must-pass FAIL (6). **NO-GO.**

## 13. Recommendation
**NO-GO on the shower-arm resin product. Do not spend the ~₹25k ad test or rework the landing page, brand or ads for it.** Keep the insight and the research. Next step: CEO decides whether to commission a **Stage 1 screen of a bathroom-scale regenerable softener** for Bengaluru owner-occupied borewell homes (cost ₹0, about 1 hour). The ₹3 to 5k bench test as originally scoped is no longer the right next spend; if the founder wants physical confirmation first, the loose-resin run is about ₹1 to 1.5k.

**Persona recommendation:**
- For the shower product: none. The best-fit persona from the screen (Bengaluru renter on borewell water) is exactly who cannot be served honestly by a shower-arm cartridge, and who cannot plumb in a real softener.
- For the pivot (to test in its screen): **owner-occupier households in Bengaluru's borewell and tanker zones, age about 30 to 50, independent house or villa or an apartment with its own bathroom plumbing control, who have already bought a ₹1.5 to 2.8k "hard water filter" and seen no change.** Areas to target first (hypothesis, Low-Medium: dated, vendor-commissioned or zone-level data): the Cauvery Stage V zones with low connection uptake (Mahadevapura incl. Whitefield, Hagadur, Panathur, Gunjur; Bommanahalli incl. HSR, Electronic City; Rajarajeshwari Nagar; Dasarahalli incl. Peenya; Byatarayanapura; Yelahanka) and Brita's high-hardness list (RT Nagar, Yeshwantpur, Peenya, Kammanahalli, Ramamurthy Nagar). Measured ranges: Electronic City 8 to 580 ppm, Whitefield 96 to 492, HSR 68 to 276 (DrinkPrime, 2022). **Pin-code-level hardness: not found**; CGWB and NAQUIM reports that would have it could not be opened. Ad geo-targeting should use these localities by radius, not pin-code lists, until better data exists.

## 14. Unknowns and validation tasks (cheapest first)
1. Founder: accept NO-GO, or run the loose-resin column check (₹1 to 1.5k).
2. Area-level hardness from CGWB/NAQUIM Bangalore Urban reports (free; needs a network that can reach cgwb.gov.in).
3. Reddit, Quora and apartment-group voice (blocked here; a human can read them in a browser, free).
4. Census 2011 HL-04 owner/renter split and current household count for Bengaluru (free).
5. Pivot: landed cost of 5 to 15 L manual-regeneration softener units at small MOQ (supplier quote, founder OK).
6. Pivot: WTP at ₹6 to 15k (pre-order smoke test, later).
7. CCPA guideline text and E-Commerce Rules check (CA or lawyer; consumeraffairs.nic.in unreachable here).
8. Trademark search for "Mrudu" only if the name is kept for a pivot.

## 15. Source ledger
`sources.md` (every URL, date, what it supports, opened / snippet / blocked). Read in full: brand product feeds (WaterScience, RiverSoft, Purifit), Flipkart search and 6 review sets, Purolite datasheet, Pure Water Products table, DMG excerpts (IWP), Deccan Herald (4 articles), Citizen Matters (2), BIS list, GST notification compilation, Legal Metrology rules, ASCI code, 2 UK ASA rulings, Amazon.ae search, MPCB report, TNM. Snippet only: SEI, resin BV/h ranges, Kent prices, Chennai studies, UAE licence and permit, DMG 45% figure. Blocked: Reddit, Quora, TechEnclave, Amazon.in, CGWB, OpenCity, Springer, core.ac.uk, consumeraffairs.nic.in, egazette, DEWA, helloklean.com, waterfilterguru.com.

## 16. Pushback raised / what we're missing
See the report to the CEO. Short form: the studio built a landing page, brand kit and ad plan for a product whose core claim fails on a datasheet check that takes an hour. Research must come before build (the new playbook already says so). The founder's "not yet" on the bench test was the right instinct for the wrong reason: the test is not needed to kill this form.

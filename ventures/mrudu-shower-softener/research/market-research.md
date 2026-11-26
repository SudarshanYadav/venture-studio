# Mrudu (resin shower softener): Stage 1 screen, India and UAE
Date: 2026-11-26 | Researcher: Market Researcher | Stage: **screen (Stage 1)** | Currency: INR and AED; Rs 85/USD (studio), AED 3.6725/USD, so Rs 23.14 per AED (2026-11-26). Country facts: `research/countries/india.md`, `research/countries/uae.md`.

**Read this first: every WebFetch failed (hosts not in the session's network allowlist, e.g. gulfnews.com, helloklean.com, superads.ai, techenclave.com). All evidence is search snippets. No page was read in full. Customer quotes are not verbatim.**

## 0. Verdict
**PARK. Lead country if it proceeds: India (Bangalore). UAE: KILL as a first market at a Rs 1,999-equivalent price.** Confidence: Low-Medium.
- Park, not kill, because the only must-pass items that fail or are unknown are ones a Rs 3 to 5k bench test and a CA/compliance check settle: cartridge capacity (claim risk, repeat revenue) and the Rs 50k/month target.
- SOM (12 months, Bangalore): **about 350 to 1,300 shower orders (Rs 7 to 26 lakh revenue)**, Low confidence. Month-12 net run-rate **about Rs 15k to 65k/month, base about Rs 25 to 35k**, mostly dependent on cartridge repeat that is unmeasured.
- Deciding number: **month-12 net vs the provisional Rs 50k/month target (unconfirmed by founder)**. Base case misses it with Bangalore alone.
- Assumption that changes the verdict: **cartridge life and repeat rate**. Test: bench test (capacity in litres at borewell hardness) plus a 25-order pre-order read of repeat intent.
- Scorecard: 3 pass, 1 fail-leaning-unknown on must-pass (income), 2 must-pass unknown (regulatory, claim), 0 hard must-pass fails in India; UAE fails must-pass 3.

## 1. Market definition
Bangalore households on hard borewell or mixed borewell/Cauvery water, buying a Rs 1,999 resin shower-arm softener plus Rs 599 cartridges, prepaid. Out of scope: whole-house softeners, drinking water, health outcomes, other cities (second wave), UAE (see below).

## 2. Sizing (one method per country for the screen, plus a cross-check for India)
| | India (Bangalore) | UAE | Method | Conf. |
|---|---|---|---|---|
| TAM (households) | 0.54 to 1.41M hard-water groundwater households = Rs 108 to 283 crore at Rs 1,999 | Not sized (no source for household count or hardness distribution) | Bottom-up | Low |
| SAM | 0.32 to 1.13M = Rs 65 to 226 crore | Unknown | TAM x 60 to 80% reachable (shower arm, no softener already) | Low |
| SOM 12m | 350 to 1,300 orders, Rs 7 to 26 lakh | Not sized: killed on CAC | Channel-led (below) | Low |

Arithmetic (script `scratchpad/calc.py`, rechecked):
- TAM = 3.0 to 3.8M households (**my assumption, unsourced; verify with Census/BBMP**) x 45 to 62% using groundwater (Deccan Herald 45%; SEI 26% + 36% = 62%) x 40 to 60% above 200 mg/L (assumption; DMG samples range 48 to 1,540 mg/L; an unattributed survey said 45% within desirable limit) = 0.54M to 1.41M.
- SAM = TAM x 60 to 80% = 0.32M to 1.13M.
- Channel-led SOM = Rs 2 to 4 lakh ad spend over 12 months (the ceiling inside the budget: ~Rs 3L = 35%) / CPO Rs 450 to 730 (finance bars) x 1.2 to 1.5 for organic/referral = 330 to 1,330 orders; reported 350 to 1,300.
- Cross-check, penetration method: 0.3% to 1% of SAM = 970 to 11,300 orders. That is 12x apart from channel-led. Explanation: penetration is a demand ceiling; the channel method is the binding limit because ad budget and CPO bars cap what we can reach. SOM uses the channel figure. Biggest swing factor: CPO (CVR) and ad budget.
- Month-12 net: shower orders 80 to 120/month x (Rs 730 minus CPO Rs 511 to 600) = Rs 10k to 26k. Cartridges: Rs 599 / 1.18 = Rs 508 ex-GST; cartridge cost Rs 150 to 250 (**assumption, no quote**); margin Rs 258 to 358; installed base 500 to 1,300 x 30 to 50% repeat x 2 per year = Rs 6k to 39k/month. Total Rs 16k to 65k.
- Market-report cross-check (not a method): India softener market about USD 114 to 128M (IMARC, MarkNtel; abstracts only; Low; scope unclear).

## 3. Competition (snippets only; Observed unless marked)
| Player | Country | Price (incl. tax, assumed) | Claim / note | Source |
|---|---|---|---|---|
| WaterScience CLEO (incl. "High Hardness cartridge" for borewell/tanker) | IN | Rs 2,139 to 2,795 | Sells borewell-specific cartridge; claims reduce hair fall (a health claim, not ours to copy); cartridge up to 6 months | Flipkart, 1mg |
| RiverSoft SF-15 Pro / Diva Pro | IN | Rs 1,318 to 1,449 (MRP 4,999) | "15-stage water softener"; one listing states it does not reduce TDS | dealsmagnet |
| SNIX 15-stage, Alton, Purifit, Ruhe | IN | Rs 678 to about 1,500 | Cheap generic "hard water" filters | Flipkart/dealsmagnet |
| Hello Klean | global (UK, US, AU, GCC listings) | about 55 GBP / 75 USD | Own FAQ: no shower filter removes calcium and magnesium; independent test saw hardness not fall (WaterFilterGuru, 1 sample) | helloklean FAQ, waterfilterguru (snippets) |
| Generic imports (Carrefour UAE, Amazon.ae) | UAE | AED 35 to 99; cartridges AED 123 per 2-pack | "hard water softener" wording; mostly chlorine removal | Carrefour UAE, pricena |
| Status quo | both | Rs 0; whole-house softener (Rs 15k+ **not sourced**); bottled/RO water for hair wash; tolerate | Techenclave: users call shower filters a "gimmick" for borewell water (paraphrase) | techenclave (snippet) |
Culligan and Delta: **no Indian listings found in search; not verified.** The quality audit's claim stands only for Hello Klean (FAQ via snippet).
Inferred: "softener" is already a crowded keyword at Rs 700 to 2,800 in India with deep MRP discounting. Whitespace is **measured, test-strip-proven hardness reduction at borewell hardness**, which nobody observed does. Defensibility: low (generics can copy the wording); medium only if proof is real and capacity holds.

## 4. Gross margin and CAC sanity
- India: finance model max CAC Rs 730, GO Rs 511 (landed cost Rs 600 is a placeholder). CPO = CPC / CVR. CPC Rs 8 to 25 (Low), CVR 1 to 3% (assumption): CPO Rs 267 to 2,500; central Rs 12 / 1.5% = Rs 800 (KILL), optimistic Rs 8 / 3% = Rs 267 (GO). **Optimistic end beats the max, so not a fail, but the central case sits above the bar.** Rule: CPC <= about 5.1 x CVR(%).
- UAE: CPC Rs 60 to 183 ($0.70 to 2.15); at 3% CVR CPO = Rs 1,983 to 6,092 (AED 86 to 263). Contribution at AED 86 is roughly Rs 800 to 900 (landed UAE cost unknown). Needs 8 to 13% CVR to hit Rs 730 CPO. **Fails even at the optimistic end.** Price would need to roughly double (Rs 4k, about AED 175) with no WTP evidence, against AED 35 to 99 shelf prices.

## 5. Regulatory flags (verify with a professional before launch; no licence applied for)
- India: **needs check**. No BIS compulsory order for shower filters found (search negative, not proof). GST 18% HSN 8421 assumed (finance). Legal Metrology declarations and E-Commerce Rules 2020 (grievance officer) apply. ASCI/CCPA: no health claims, substantiate hardness claim. Not a known blocker.
- UAE: mainland e-commerce licence about AED 10 to 30k (vendor blogs conflict), VAT 5%; MOIAT and advertiser permits **not researched**. Setup cost is below 10% of budget; time unknown.
- Claim risk: marketing "softens water" is lawful only if measured. Hardness reduction is defensible; hair/skin outcomes are not. Brand name "Mrudu": no trademark search done.

## 6. Kill-criteria scorecard (playbook section 5)
| # | Criterion | Result | Number and source |
|---|---|---|---|
| 1 | Side-income size (must) | **UNKNOWN, leans FAIL** | Base month-12 Rs 25 to 35k vs Rs 50k provisional; range Rs 16 to 65k hinges on unmeasured cartridge repeat. Founder has not confirmed Rs 50k |
| 2 | Test affordability (must) | **PASS (provisional)** | Test Rs 25k ad spend is at the limit; inventory MOQ and quote **unknown**; at Rs 600 landed, 30 units = Rs 18k |
| 3 | CAC feasibility (must) | India **PASS (optimistic end only)**; UAE **FAIL** | India optimistic CPO Rs 267 vs max Rs 730; UAE optimistic Rs 1,983 |
| 4 | Regulatory blocker (must) | **UNKNOWN** | No blocker seen; BIS/Legal Metrology unverified |
| 5 | Margin >= 35% | **PASS** | Rs 937 on Rs 1,999 kept order before refunds = 47%; max CAC bars leave about 37% after refunds at CAC 0 (finance section 0) |
| 6 | Competition wedge | **PASS (conditional)** | Wedge is proof; generics cheaper; wedge needs measurement |
| 7 | Demand evidence | **PASS (weak)** | Vendor blogs, paraphrased Reddit/forum posts, India hardness data; no verbatim customer quotes |
| 8 | Claim risk (must) | **UNKNOWN** | Hardness claim unproven until bench test; Hello Klean FAQ says filters do not soften |
| 9 | Concentration | **PASS** | Meta-dependent for tests; not >50% locked yet. Unverified |
Rule result: no must-pass hard FAIL in India; two UNKNOWN must-pass plus one leaning-FAIL = **PARK** with named validation tasks. UAE: must-pass 3 FAIL = KILL for now.

## 7. Candidate segments (ranked)
| # | Segment | Problem in their words (all paraphrase, not verbatim; pages not opened) | Size (Low conf.) | WTP at Rs 1,999 / AED 86 | Cheapest reach | Conf. |
|---|---|---|---|---|---|---|
| 1 | **Bangalore renters and young professionals on borewell/tanker water** (25 to 40, cannot plumb a whole-house unit) | Forum users call generic filters a gimmick for borewell water; scale on taps/tiles, soap will not lather; sellers say borewell TDS 700 to 1,500 ppm | SAM share maybe 30 to 50% of 0.32 to 1.13M = 100k to 560k households | Medium: competitors sell at Rs 2.1 to 2.8k, so Rs 1,999 is within band | Meta geo-targeted (Bangalore), r/bangalore, apartment/RWA WhatsApp groups (needs founder OK to post) | Low-Med |
| 2 | **Bangalore owners (apartments/villas) fighting scale on glass, fittings** | White scale on tiles and taps; high hardness vendors cite 300 to 500+ ppm | 40 to 60% of SAM | Medium-High (own the fixtures) but shower filter does not protect geysers; many already have softener/RO | Meta lookalikes, Google search "hard water shower", Nextdoor-type groups | Low |
| 3 | **Other Indian metro borewell households (Hyderabad, Chennai, Pune)** | Same problem; hardness not sourced here | Unknown | Unknown | Same funnel, second wave | Low |
| 4 | **UAE expat households (Dubai/Sharjah/Abu Dhabi), apartments and villas** | Reddit user via Harper's Bazaar Arabia (paraphrase): Dubai water hard, minerals stay in hair | Unknown | **Low at AED 86**: shelf AED 35 to 99, filters seen as chlorine tools; CAC fails | Meta at CPC Rs 60 to 183; Instagram | Low |
| 5 | **Hair-care motivated buyers (cross-cutting)** | Hair fall and dry hair is the dominant complaint in vendor content | Large but a health-claim zone | High intent, high claim risk | Instagram, creators | Low |
**Ranking rationale:** 1 beats 2 on need-to-fit (shower-arm product, no plumber, renters cannot buy whole-house) and on reachability; 3 is the growth path to the Rs 50k goal; 4 fails CAC; 5 is a claim-risk trap (Meta/ASCI, CLAUDE.md section 7) and should be a message to avoid, not a persona.
**Recommended starting persona: segment 1, Bangalore renter/young professional on borewell water,** reached via Meta in 560xxx pin areas with known borewell dependence (area hardness data to be gathered in Stage 2).

## 8. Open questions (cheapest first)
1. Cartridge capacity at borewell hardness (Rs 3 to 5k bench test; blocks claim, repeat, and criteria 1 and 8). Needs founder OK.
2. Landed cost at the first-batch MOQ (supplier quote; needs founder OK to contact).
3. Founder confirmation of the Rs 50k/month target and whether a second city is acceptable.
Also: BIS/Legal Metrology/GST check with a CA; trademark search for Mrudu.

## 9. Source ledger
Search snippets only (about 14 searches): see `research/sources.md`. Full page reads: none (fetch blocked). Blocked hosts: gulfnews.com, waterscience.in, helloklean.com, superads.ai, redlib.reallyaweso.me, techenclave.com.

## 10. Pushback / what I'd do differently
See report. Short form: the Rs 50k/month target cannot be met from a Rs 1,999 Bangalore-only shower product unless cartridges repeat; do the bench test before any more design or ad work; drop UAE for now.

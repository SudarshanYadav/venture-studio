# Mrudu: market research report (India)
Date: 2026-11-26 | Researcher: Market Researcher | Stage: deep dive (consolidated) | Currency: INR; ₹85/USD (studio rate, 2026-11-26) | Shelf prices are tax-inclusive as displayed (Legal Metrology Rule 2(m)) unless stated.
Evidence tags: **O** observed (page opened 2026-11-26), **S** search snippet only, **I** inferred. Confidence: H / M / L / Unknown. Every number below traces to `sources.md`, `customer-voice.md` or `calc/` (see Appendices). Not a lawyer; verify regulatory items with a professional before launch.

## 1. Verdict and the decisions the founder needs to make
**NO-GO on the shower-arm resin cartridge (₹1,999 + ₹599 refills, sold on "hardness reduction, proven with a test strip"). Country: India (Bengaluru) is the only market in scope; the product fails the physics wherever it is sold.** Confidence: Medium-High on the physics, Medium on the market.
- **Deciding number:** a shower-arm cartridge pushes water through its resin 26 to 150 times faster than softening resin is rated for, and holds capacity for only **12 to 166 L** at Bengaluru borewell hardness (0.2 to 3 showers).
- **Market confirms it unprompted:** every Indian brand checked calls its product a "conditioner"; no resin shower product was found in India.
- **Scorecard:** shower form has 2 must-pass FAILs (side income, claim risk) and 1 other FAIL (wedge). Rule: any must-pass FAIL = NO-GO (section 13).
- **What survives:** real demand, and an open position on proof. A bathroom-scale salt-regenerated softener is not a free price band (three branded incumbents at ₹9.9k to 14.9k) but is empty of online reviews and published running costs. Status of both pivots: **PARK** until three cheap facts are in (section 11).

**Decisions for the founder**
| # | Decision | Options | Cost | Recommendation |
|---|---|---|---|---|
| 1 | Accept the NO-GO on the shower form | Accept / run the loose-resin column check first (Appendix C) | ₹0 / about ₹1,000 to 1,500 (spend, needs OK) | Accept. The check is only needed to reopen the form, not to kill it |
| 2 | Stop all Mrudu landing, brand and ad work | Stop / continue | ₹0 | Stop (CEO call, no spend) |
| 3 | Commission a Stage 1 screen of the pivots | Bathroom softener, salt/service subscription, hardness-test lead-gen | ₹0, about 1 hour | Yes, and screen the subscription first (lowest capex, section 11) |
| 4 | Confirm the side-income target that drives the kill criteria | ₹50k/month net by month 12 is provisional | none | Confirm or change; it decides criterion 1 |
| 5 | Later, if a pivot passes its screen | Supplier quotes, one sample unit, hardness tests in 5 to 10 homes, owner interviews | about ₹8 to 15k sample (Low), ₹2 to 5k tests | Not yet; each needs OK at the time |

## 2. Key numbers
| Number | Value | Source | Confidence |
|---|---|---|---|
| Resin capacity | 95 g CaCO3 per L resin total (1.9 eq/L); 73 g/L working | Purolite C100E datasheet; Pure Water Products table (both O) | High |
| Shower cartridge resin volume | 0.1 to 0.35 L (assumption; no supplier spec) | `calc/stage2_calc.py` | Low |
| Litres softened per cartridge | 12 to 166 L at 200 to 600 mg/L = 0.2 to 3 showers | `calc/stage2_calc_output.txt` §2 | Medium |
| Flow vs rating | 26 to 150x over the 8 to 40 BV/h rating | calc §3; four datasheets (S) | Medium-High |
| Resin needed at full flow | about 12 L | calc §3 | Medium |
| Bengaluru hardness | 48 to 1,540 mg/L urban; 8.5% of 2,209 samples above 600 | DMG 2011 via Deccan Herald, India Water Portal (O) | Medium (2010 samples) |
| Share of households above 200 mg/L | 45 to 60% of borewell-dependent | DMG (S for the 45%) | Low-Medium |
| Households dependent on borewell | 45% (2016); trend down with Cauvery V | Deccan Herald 2016-04-24; Citizen Matters 2025-04-07 (O) | Medium |
| TAM (shower form, Bengaluru) | 0.61 to 1.41M households; ₹121 to 283 crore one-time at ₹1,999 | calc §6 | Low-Medium |
| SOM, 12 months, if the product worked | 330 to 1,330 orders = ₹6.6 to 26.7 lakh | calc §9 | Low |
| SOM, honest, product as specified | about 0 | section 8 | Medium-High |
| Orders per month for ₹50k net | 178 / 228 / 384 at CPO ₹450 / 511 / 600 vs SOM 27 to 111 a month | calc §9 | Low |
| Finance CPO bars | max CAC ₹730; GO ₹511 | `finance/unit-economics.md` §0 | Medium |
| Implied CPO (Meta) | ₹267 to 2,800; central ₹800 (KILL) | owlclaw CPC ₹8 to 25, CVR 1 to 3% assumed | Low |
| Players found | 21 named + about 20 white-labels | section 4 | Observed |
| Conditioner ladder | ₹195 to 4,695; installed softeners ₹9,891 to 2,49,000 | section 5 | Observed |
| Real bathroom softener, 12-month cost | about ₹13k to 36k (unit + salt) | section 5 | Low-Medium |
| 1 to 2 star share, conditioners | 9.0 to 22.7% across six Flipkart listings; D'Cal tank media 22.2%; Avimee liquid 10.0% | calc §8, `landscape_calc_output.txt` | High |

## 3. The problem and the market
**Market definition:** Bengaluru households on hard borewell, tanker or mixed water who want softer bathing water, buying a no-plumber, tax-inclusive shower-arm product at ₹1,400 to 2,800 with refills. Out of scope: drinking water (RO), health outcomes, other countries (founder decision 2026-11-26).

**Hardness and water source (Bengaluru)**
| Fact | Value | Source, date | Confidence |
|---|---|---|---|
| Groundwater hardness, Bangalore Urban | 48 to 1,540 mg/L (Rural 72 to 1,416) | Deccan Herald 2011-05-13 (O) | Medium |
| Samples above 600 mg/L | 8.5% of 2,209 (pre-monsoon 2010) | India Water Portal, DMG report Mar 2011 (O) | Medium |
| Within desirable limit (200) | 45% of samples, so about 55% above | DMG (S) | Low-Medium |
| Borewell dependence | 45% of Bengaluru, 110 villages without Cauvery pipes (2016) | Deccan Herald 2016-04-24 (O) | Medium, dated |
| Cauvery Stage V | Inaugurated 2024-10-16; 104 of 110 villages "received water", 89,000 connections vs 3 lakh target (2025-04); residents report pipes laid but no supply (2026-04-28) | Citizen Matters 2025-04-07; Deccan Herald 2026-04-28 (O) | Medium |
| Mixed Cauvery + borewell above 200 mg/L | 24% of 1,423 households (2018) | Deccan Herald 2018-08-01; Citizen Matters 2025-05-05 (O) | Medium |
| Area readings (DrinkPrime Jan to May 2022) | Electronic City 8 to 580 ppm, Whitefield 96 to 492, HSR 68 to 276 | Deccan Herald 2022-07-20 (O) | Medium (vendor sample) |
| Pin-code-level hardness | **Not found.** CGWB/NAQUIM reports could not be opened | | Unknown |

**Target areas (hypothesis, Low-Medium; dated or vendor-commissioned data).** Cauvery Stage V zones with low connection uptake: Mahadevapura incl. Whitefield, Hagadur, Panathur, Gunjur; Bommanahalli incl. HSR and Electronic City; Rajarajeshwari Nagar; Dasarahalli incl. Peenya; Byatarayanapura; Yelahanka. Brita's 2018 high-hardness list: RT Nagar, Yeshwantpur, Peenya, Kammanahalli, Ramamurthy Nagar. Geo-target by locality radius, not pin-code lists, until better data exists.

**Market size (India = Bengaluru)**
| | Value | Method | Confidence |
|---|---|---|---|
| TAM | 0.61 to 1.41M households | Bottom-up: 3.0 to 3.8M households x 45 to 62% groundwater-dependent x 45 to 60% above 200 mg/L | Low-Medium |
| SAM | 0.36 to 1.13M households | TAM x 60 to 80% (has a shower arm, no softener; assumption) | Low |
| SAM, owner-occupier (pivot) | 128k to 565k households | SAM x 35 to 50% owners (assumption; Census HL-04 not opened) | Low |
| Category flow, all India | Top-9 Flipkart listings: 6,879 ratings = about 1.4 to 6.9 lakh lifetime units at 1 to 5% ratings per unit. WaterScience's own "1.5 million customers" claim implies ₹38 to 75 crore a year over 4 to 8 years | Competitor-led | Low |
| SOM, 12 months | 330 to 1,330 orders, ₹6.6 to 26.7 lakh | Channel-led: ₹2 to 4 lakh ads / CPO ₹730 to 450 x 1.2 to 1.5 organic | Low |

**Arithmetic** (`calc/stage2_calc_output.txt` §6, §7, §9): SOM low = 2,00,000 / 730 x 1.2 = 329; high = 4,00,000 / 450 x 1.5 = 1,333. **Methods compared:** bottom-up (potential stock) and competitor-led (actual flow) measure different things and agree that the category is real and large against our goal. A penetration cross-check (0.3 to 1% of SAM = 1,100 to 11,300 orders) is 3 to 9x the channel-led SOM; the gap is explained, because our ad budget, not demand, caps SOM. **Swing factors:** whether the product works at all, then CPO. **Attractiveness (/50): 27** (demand 4, budget 4, competitive weakness 3, reach 3, channel 3, urgency 2, proof 1, execution risk 2, speed 3, fit 2) = "validate first"; proof scores 1 because the shower form cannot prove what it would sell.

## 4. Current players
21 named players, six categories. **12-month cost** = unit + replacement media or salt for one household (ranges; assumptions in section 5). Rating counts are Flipkart on 2026-11-26 unless stated. All rows O unless tagged.
| Player | Category | Mechanism (its own words) / does it soften? | Price ₹ (unit; media) | 12-month cost ₹ | Where sold | Rating count (mean) | Claim and proof | Link |
|---|---|---|---|---|---|---|---|---|
| WaterScience (Bengaluru, est. 2014) | Shower/tap conditioner | KDF; "converts hard water salts into harmless forms"; conditions, "does not reduce TDS" | CLEO SFM-419 2,795 (MRP 3,495); tap 1,495; cartridge 845 (2 for 1,595), "4 to 6 months" | 3,640 to 4,485 | Own Shopify, Flipkart, Amazon (S), 1mg (S); "more than 1,000 offline retailers" (S) | CLEO tap 4,381 (3.8); 717: 156 (3.8); SFU-423: 226 (3.9) | "Reduces the effects of hardness"; badges "Reduces Hairfall", "Protects Skin"; no hardness number | [CLEO SFM-419](https://www.waterscience.in/products/multi-flow-shower-filter-cleo-sfm-419-fits-standard-shower-arms-with-free-self-installation-kit) · [Tap filter](https://www.waterscience.in/products/tap-filter-for-hard-water) · [Cartridge](https://www.waterscience.in/products/replacement-cartridge-filter) · [Cartridge x2](https://www.waterscience.in/products/replacement-cartridge-filter-cleo-shower-tap-filters-pack-of-2) · [Flipkart: CLEO tap](https://www.flipkart.com/water-science-cleo-tap-filter-hard-municipal-metro-water-mount/p/itme09021f5b2d0e?pid=TWFGU3TCDNYQNDXR) · [Flipkart: 717](https://www.flipkart.com/water-science-cleo-717-shower-tap-filter-standard-cartridge-head/p/itm5b95ef3e784a0?pid=SHDFGS42PUHSCRS4) · [Flipkart: SFU-423](https://www.flipkart.com/water-science-cleo-sfu-423-shower-tap-filter-hhc-mount/p/itm65d1d13ee259f?pid=TWFHAH58PWJ5APWU) |
| RiverSoft (Bengaluru, est. 2019) | Shower/tap conditioner | KDF, calcium sulphite, carbon, vitamin C; DIVA-01: "does not chemically soften water" | SF-15 1,549 (MRP 4,999); DIVA PRO 1,440; DIVA-01 1,699; up to 2,049; cartridge about 684 | 2,233 to 2,917 | Own site, Flipkart, Amazon (S) | SF-15 924 (3.9); DIVA PRO 442 (4.0); DIVA-01 87 (4.1) | "helps reduce hardness"; none proven | [SF-15](https://theriversoft.com/products/bathroom-water-softener-sf15) · [DIVA PRO](https://theriversoft.com/products/riversoft-diva-pro-shower-and-tap-filter-for-hard-water-with-15-stage-water-softener-for-bathroom-hard-water-filter-chrome-pack-of-1) · [DIVA-01](https://theriversoft.com/products/bathroom-shower-water-softener-diva-01) · [DIVA Elite](https://theriversoft.com/products/riversoft-diva-elite-shower-and-tap-filter-for-hard-water) · [Cartridge SFC-15](https://theriversoft.com/products/shower-tap-replacement-filter-cartridge-sfc15) · [Flipkart: SF-15](https://www.flipkart.com/riversoft-sf-15-tap-filter-hard-water-water-softener-bathroom-chrome-mount/p/itma847ecc649b85?pid=SHSGYPZZTHHUUS9K) · [Flipkart: DIVA PRO](https://www.flipkart.com/riversoft-diva-pro-shower-tap-filter-hard-water-15-stage-mount/p/itm6ee4353abb29c?pid=TWFHAF9A4TPGF7CZ) · [Flipkart: DIVA-01](https://www.flipkart.com/riversoft-diva-01-shower-filter-hard-water-15-stages-softener-bathroom-head/p/itmb8fd4b34a3fe9?pid=SHDH4YF25EUPKZDK) |
| Purifit | Shower/tap conditioner | KDF-55, carbon, polyphosphate; "non-RO, non-softener" | Head 999 (MRP 1,999); Atom 1,719; Ultra 1,499; cartridge 699 to 849 | 1,698 to 3,197 | Own site, Flipkart | 356 (4.4); Atom 75 (14.7% 1 to 2 star) | "98.1% scale reduction" lab claim (report not opened) | [Head (own site)](https://purifit.in/products/classic-all-rounder-hard-water-shower-tap-filter) · [Atom](https://purifit.in/products/atom-compact-hard-water-shower-tap-filter) · [Ultra](https://purifit.in/products/purifit-ultra-hard-water-shower-tap-filter) · [Ultra cartridge](https://purifit.in/products/purifit-ultra-hard-water-filter-replacement-cartridge) · [Flipkart: head](https://www.flipkart.com/purifit-filter-hard-water-softens-removes-chlorine-silver-colour-shower-head/p/itmda464760bc92a?pid=SHDFNWHBHBCVYFQB) · [Flipkart: Atom](https://www.flipkart.com/purifit-atom-shower-tap-filter-hard-water-reduces-hair-fall-softens-mount/p/itm1a024872ab832?pid=TWFHDGEFFHHDVWV6) |
| Snix | Shower/tap conditioner | "Hard Water Softener" in title; media not stated | 857 to 943 | Unknown | Flipkart only | 308 (3.7) | None | [Snix (Flipkart)](https://www.flipkart.com/snix-hard-water-softener-bathroom-shower-filter-tap-adaptors-included-mount/p/itme514dcf65261f?pid=TWFH9TFUPZPHZH9E) |
| Wevora, Flaner, WaterLabs, Wallberrie, Suicune, Poolcraft, Eshva, TruQual (about 20 white-labels) | Marketplace private label | KDF, vitamin C, "15 to 22 stages" | 448 to 1,199 (MRP up to 5,999; 50 to 88% "off") | 900 to 2,400 | Flipkart | Mostly under 150; WaterLabs HL-40 66 (4.1) | "Softener", "Reduces Hair Fall" in titles; none proven | [Wevora 20-stage](https://www.flipkart.com/wevora-20-stage-shower-filter-hard-water-hair-skin-protection-universal-fit-tap-mount/p/itm65d80d9105cb3) · others (Flaner, WaterLabs, Wallberrie, Suicune, Poolcraft, Eshva, TruQual): not found |
| gvantikA, DEAGAN, Rainflow | Tap mesh filter (not a hardness product) | Sediment mesh | 130 to 380 | n/a | Flipkart | 3,473 / 427 / 1,562 | Sediment only | not found |
| Avimee | Liquid "instant softener" | Sodium gluconate + apple cider vinegar (label per reviewer) | 410 per 400 ml; larger 742 to 1,000 | About 4,900 if one bottle a month (assumption) | Flipkart, own site | 4,805 (4.2); 10.0% 1 to 2 star | "Hairfall control" in title | [Avimee (Flipkart)](https://www.flipkart.com/avimee-herbal-instant-water-softener-hairfall-control-maintains-ph-hair-skin-friendly/p/itmc0f973ba43433?pid=HTTH7GGY5DXHGGZG) |
| Swoffy, Kidzelo, Khubee, Ramiloo, others | Liquid softener | Same format | 195 to 575 | Same | Flipkart | Swoffy 5 to 42; others under 40 | "Instant water softener", "Hair fall control" | not found (no standalone Flipkart page located) |
| Scale-O | Tank scale protector | Media in overhead tank; "Does not reduce TDS" | Mini 3,000 (6 months) / 5,000 (1 year); Semi 4,000 / 7,000; Centi 4,500 / 8,000 | 5,000 to 8,000 (subscription) | Own Shopify, Flipkart | 24 (4.2); 12.5% 1 to 2 star | "Helps reduce scale buildup" | [Mini](https://scale-o.com/products/mini-water-softener-500l-750l-tanks) · [Semi](https://scale-o.com/products/semi-water-softener-1000l-1500l-tanks) · [Centi](https://scale-o.com/products/centi-water-softener-2000l-2500l-tanks) · [Flipkart](https://www.flipkart.com/scaleo-scale-o-whole-house-water-softener-tanks-reduces-hard-scaling-problems-media-filter-cartridge/p/itmd64814a51a420?pid=WFCH8BCTGTSAZWGZ) |
| D'Cal | Tank scale protector | "Solid filter cartridge"; mechanism not stated | 4,174 | Unknown | Flipkart | 932 (3.72); **22.2% 1 to 2 star** | "Hard water softener" in title | [D'Cal (Flipkart)](https://www.flipkart.com/d-cal-whole-house-hard-water-softner-solid-filter-cartridge/p/itm5e58c842e6c97?pid=WFCFN6YHZ9HQTUMN) |
| aaeqovo9, Neeva, GD Water | Tank media look-alikes | Tank media | 2,246 to 3,186 | Unknown | Flipkart | 0 to 6 | "Skin and hair solution" | not found |
| Alkara | Salt-free "bathroom softener" | "Chemical-free"; conditioner by its own description (I) | 4,999 (Bajaj Finserv list, 2026) | 4,999 | Bajaj EMI listing, dealers | Not seen | Unknown | [Alkara (Bajaj Finserv)](https://www.bajajfinserv.in/alkara-water-softener) |
| ZeroB (Ion Exchange India) | Real bathroom softener, manual | Ion exchange; 8 to 10 L/min; max 500 ppm raw; **300 L per recharge at 500 ppm, 600 L at 250 ppm** | 9,891 (MRP 10,990) | About 13.3k to 30.9k (unit + salt) | zerobonline.com, dealers | Not on Flipkart sample | Capacity published; no running cost | [ZeroB bathroom softener](https://www.zerobonline.com/product/bathroom-softener-point-of-use/) |
| Aquaguard (Eureka Forbes) | Real bathroom softener, manual | Ion exchange; capacity per kg salt not stated | AWS I-250 12,499 (snippet 13,999); I-600 NXT 16,999 (Flipkart) / 19,999 (company page) | Unit + salt (not published) | eurekaforbes.com, Flipkart | **0 ratings** on all three listings | Free installation and service plan | [AWS C-500](https://www.eurekaforbes.com/dp/GWPDWSC5H00000/aquaguard-aws-c-500-water-softener) · [Softener category](https://www.eurekaforbes.com/c/water-purifiers/aquaguard-water-softener) (I-250 and I-600 NXT pages not separately found) |
| Kent | Real bathroom softener, manual (5.5 L resin) | Ion exchange; 1,000 L/h; **about 1,500 L per regeneration at 200 ppm**; 880 g salt | 14,949 | About 18.3k to 35.7k | kent.co.in, dealers | 2 on-site reviews | Capacity published; AMC ₹250/yr per a YouTube title (S) | [Kent bathroom softener](https://www.kent.co.in/products/water-softener-kent-bathroom-water-softener) |
| Kent | Automatic 8 L | Ion exchange; about 2,200 L per regeneration at 200 ppm; 1.28 kg salt | 30,500 | Unit + salt | kent.co.in | On-site only | | [Kent automatic 8 L](https://www.kent.co.in/products/kent-automatic-water-softener-8l) |
| A.O. Smith | Automatic CWS-25, CWS-40 | "Flow and time based" | Not shown | n/a | aosmithindia.com | n/a | Capacities not read | [A.O. Smith India home page](https://www.aosmithindia.com/) (CWS-25 / CWS-40 product pages not found) |
| WaterScience RENO | Whole-house / automatic | Ion exchange | RENO 1,500 (1 bathroom/kitchen) 39,995; whole house 69,995; Polaris 64,995; Altius 109,995 to 139,995; salt 980 ("Bangalore location only") | Unit + salt | Own site, store locator | Not sampled | 5-year valve warranty (Polaris) | [RENO 1500](https://www.waterscience.in/products/reno-1500-multiple-bathroom-water-softener-automatic) · [Polaris](https://www.waterscience.in/products/reno-polaris-fully-automatic-water-softner-h10-h25-h30) · [Altius](https://www.waterscience.in/products/reno-altius-indias-only-touch-screen-water-softener) · [Salt](https://www.waterscience.in/products/softener-salt-tablets-bangalore-location-only) |
| Aquaguard whole-house | Whole-house | Ion exchange | I-2500 69,990; C-3000 79,990; Select 5000 104,990; up to I-17500 2,49,000 | | eurekaforbes.com | | Free installation, unlimited repair visits | [Aquaguard softener category](https://www.eurekaforbes.com/c/water-purifiers/aquaguard-water-softener) (individual whole-house pages not found) |
| ZeroB Nano Soft / AS series | Automatic / whole-house | Ion exchange (resin 4.8 L, 2.5 kg salt for four recharges, up to 600 L/h) | Nano Soft 37,790; AS1 about 46,150, AS2 about 64,990 (S) | | zerobonline.com | | Free home installation | [Nano Soft](https://www.zerobonline.com/product/zerob-nano-soft/) · [ZeroB softener range](https://www.zerobonline.com/water-softener/) |
| 3M | Apartment / society | Ion exchange (S) | Commercial ₹4.27 lakh in a dealer snippet (S) | | Society B2B | | Not researched | not found |

Links checked 2026-11-27; prices may have changed since.

Livpure, Pureit, Havells, Hindware: no softener product found (O, not exhaustive). Culligan and Hello Klean hosts were unreachable (not opened). Kinetico: no India presence observed.

**Positioning whitespace:** measured, honest hardness reduction for bathing water; no player publishes a before/after hardness number in a named home. **Their strengths we cannot match:** WaterScience's Bengaluru base, borewell SKU, store network, installed-softener line and Bengaluru salt delivery; Kent/Aquaguard/ZeroB dealer and service networks. **Copy threat:** high for any cartridge; low for a service or transparency model that needs local logistics. **Defensibility:** low (shower form); medium at best for a bathroom-scale unit.
**Substantiation check:** none of the three conditioner brands publishes a hardness before/after number. WaterScience suggests a "lather test", not a hardness test.

## 5. Price points
**Price ladder (tax-incl. list or shelf price, ₹, 2026-11-26)**
| Tier | Range | Players | What the buyer gets |
|---|---|---|---|
| Liquid "instant softener" | 195 to 575 per bottle | Avimee, Swoffy, Kidzelo | Bucket-bath additive; ongoing cost |
| Generic shower/tap heads | 400 to 1,200 | White-labels, Snix, WaterLabs | Media cartridge; no proof |
| Branded conditioners | 1,000 to 2,800 | Purifit, RiverSoft, WaterScience tap | KDF/polyphosphate; "conditions" |
| Premium conditioners | 2,300 to 4,700 | WaterScience multi-flow, RiverSoft Diva Elite | Same media, nicer head |
| Tank scale protectors | 3,000 to 8,000 a year | Scale-O, D'Cal, Neeva | Subscription media in the tank |
| **Salt-free "bathroom softener"** | **4,999** | Alkara | Conditioner by description |
| **Real bathroom ion-exchange (manual)** | **9,891 to 19,999** | ZeroB 9,891; Aquaguard I-250 12,499, I-600 NXT 16,999 to 19,999; Kent 14,949 | Salt regeneration, resin |
| Automatic point-of-use / small whole-home | 20,000 to 40,000 | Aquaguard C-500 (37,990 to 38,990, a second figure of 20,349 not resolved); Kent 8 L 30,500; ZeroB Nano 37,790; RENO 1,500 39,995 | Auto regeneration |
| Whole-house / apartment | 55,000 to 2,49,000 | RENO, Aquaguard I-2500 to I-17500, ZeroB AS | Dealer-installed |

Cartridges: ₹684 to 849, claimed life 2 to 6 months (reviewers report 20 days to 3 months, section 6). Discounting: white-labels show 50 to 88% "off" inflated MRPs; branded D2C 17 to 69%; sale banners ("Black Friday ... upto 25% Off"). CCPA dark-pattern and misleading-price rules apply if we copy (verify with a professional). Mrudu's ₹1,999 + ₹599 sits inside the conditioner band. **WTP:** proven for a conditioner at ₹1.4k to 2.8k; **WTP for real softening at ₹5k to 15k is Unknown** (first question for any pivot).

**12-month cost of a real bathroom unit (calculation, Low-Medium; `calc/landscape_calc_output.txt`).** Inputs: Kent 5.5 L resin, 1,500 L at 200 ppm, 880 g salt; ZeroB 300 L at 500 ppm; both imply about 1.1 eq/L resin. **Assumptions:** 4 people, 8-minute showers at 9 L/min = 288 L/day; salt ₹56 to 136/kg (Flipkart: 15 kg bag ₹834, 5 kg ₹680, 2026-11-26); salt dose per regeneration unchanged with hardness (understates cost at high hardness).
| Raw hardness | Litres per regeneration (5.5 L resin) | Regenerate every | Salt per year | Salt cost per year |
|---|---|---|---|---|
| 200 ppm | about 1,500 | 5.3 days | 61 kg | ₹3.4k to 8.3k |
| 350 ppm | about 860 | 3.0 days | 107 kg | ₹6.0k to 14.6k |
| 500 ppm | about 600 | 2.1 days | 153 kg | ₹8.5k to 20.8k |

So a ₹10k to 15k unit costs about **₹13k to 36k in year one**, regenerated by hand every 2 to 5 days. None of the brand pages read shows this running cost. Conditioner 12-month costs are in section 4.

## 6. Customer problems and feedback
**Sample:** 379 unique Flipkart reviews across 13 listings (181 + 198), 5 + 2 brand-site reviews, 5 India Water Portal forum quotes (2010, 2013). Sorted negative-first and most-helpful, so counts are **not market shares**. Blocked: Reddit (empty shell), Quora, Team-BHP, TechEnclave, DesiDime (403), Amazon.in (503), YouTube comments. People who have the problem but bought nothing are under-sampled. Keyword counts are approximate.

**(a) The problem buyers are trying to solve**
| Theme | Count | Sample |
|---|---|---|
| Hair and skin feel (dryness, itching, rough hair) | 27 of 82 four- and five-star reviews; 37 of 198 in the second sample | 181 / 198 |
| Scale, stains, deposits on fittings, buckets, geysers | 10 of 198; plus 2 forum posts on geyser and washing-machine clogging | 198 |
| Soap and shampoo lather | 1 brand-site review | |
| Renter/PG, no-plumber fitting valued | 7 mention easy install | 198 |

Hair and skin is the dominant motive and a claim we cannot make (CLAUDE.md section 7). Scale and appliance protection is second and can be described with measurable facts.

**(b) Complaints about current products**
| Theme | Count | Evidence |
|---|---|---|
| "No change / waste / not working" | 32 of 87 low-star (first sample); 54 of 198, including 51 of 67 one- and two-star (second) | Every category: cartridge, liquid, tank media |
| Breakage, leaks, fit (CLEO plastic neck) | 24 of 87 low-star | first sample |
| Life shorter than claimed ("one week", "20 days", "3 months") | 10 of 198 | |
| Adverse reaction attributed to the product | 11 of 198, all on the liquid | claim-risk zone; never repeat in marketing |
| Buyer measured TDS or hardness and saw no move | 5+ in the first sample; 8 of 198 | |
| Price or value | 6 of 198 | |
| Salt, maintenance, regeneration (real softeners and tank media) | 5 of 198 | |
| Distrust of reviews | 3 of 198 | |

**(c) Unmet needs and price objections**
- Softening **without manual salt regeneration**; capacity beyond one bathroom; a visible number (buyers reach for TDS meters, which cannot show hardness change; one dealer visit guessed hardness as half of TDS); "price is very high" for quantity; renters value no-plumber fitting.
- Unprompted proof demand (High confidence, 5+ independent reviewers): buyers measure and conclude the product fails. Brands answer "filters do not reduce TDS". Nobody shows a hardness number.

**The best 10 quotes** (verbatim; names removed; city as shown). Keys resolve to URLs in `customer-voice.md`.
| # | Quote | Stars | City | Theme | Key |
|---|---|---|---|---|---|
| 1 | "No change to water after usage. Hardness remains the samw" | 1 | Bengaluru | No change | F2 (#1) |
| 2 | "It is nothing but cheating. The TDS before this 600, after this 600. Don't buy it" | 1 | Hyderabad | Measured, wrong test | F4 (#10) |
| 3 | "The filter does not effectively filter the water at normal water flow. It requires a very slow water flow to work properly. It is not recommended for use while bathing or washing your face" | 2 | Pune | Flow (the physics) | F1 (#19) |
| 4 | "Amazing product , If you are in Bengaluru ..you need to have it 100% Works very well And 💯recommended" | 5 | Bangalore Division | Positive, Bengaluru | F1 (#21) |
| 5 | "I'm staying in a PG with very hard water. This filter was a game changer for my hair. Softer, less frizzy, plus easy to maintain." | 5 | Chhatarpur | Renter, hair motive | F3 (#25) |
| 6 | "It claims the average life of the filter is 6 months but it stopped working just in 20 days." | 1 | Mau | Life vs claim | L7 (N34) |
| 7 | "After installing Scale-O, we could notice the hairfall getting reduced as water quality slowly improved. No maintenance is the best bit as nowadays softeners are challenging to operate." | 5 | Burdwan | Unmet need: no salt | L3 (N24) |
| 8 | "There was an immediate difference in the bathing experience, water feels much less harsh on the skin. It is very convenient. It works well for one bathroom but is not sufficient for the entire house. Regeneration is manual but simple once you get used to it. It has significantly reduced white stains on tiles and fittings." | not shown | not shown | Real softener, capacity | K1 (N36, Kent site, unverifiable) |
| 9 | "The water from borewell is very hard and because of this the water is clogging the geyzer, wahing machine etc in Bangalore. I am planning to buy a domestic water softner, please let me know its maintenance, cost, and its effect on water supply pressure and also where it should be fitted?" | forum, Mar 2013 | Bangalore | Appliance problem | IWP2 (N40) |
| 10 | "The sales person who came from Zero B measured the TDS of the water which was at 514 but had not brought the Hardness measurement kit. He mentioned that the Hardness of water would typically be half of the TDS, so ~250. Is this a valid assumption to make and would the Zero B water softener be the right choice for this?" | forum, Dec 2010 | J.P. Nagar, Bangalore | Proof gap | IWP1 (N38) |

Source URLs for these keys, the other 62 quotes (30 + 42 numbered), segment tags and theme counts: `customer-voice.md` (Appendix A). Quotes 5 and 7 sit in the hair/skin claim-risk zone and are research evidence only, not ad copy. Note: customer-voice.md's addendum uses F1 and F2 for the two forum posts; in this report they are IWP1 and IWP2 to avoid clashing with the Flipkart keys.

## 7. Marketing channels
**What could not be observed.** Meta Ad Library (403, JavaScript-only), Instagram (login redirect, no follower counts), Amazon.in (503), Reddit, Quora, Team-BHP, IndiaMART (403), YouTube video-level views, Google search ads and SEO traffic (no paid tools), quick commerce (needs app and location). **No ad was observed**, and no block was worked around. Hooks below are claims on brand pages, not ad creative.

**Channel map (O unless marked I)**
| Channel | WaterScience | RiverSoft | Purifit | Scale-O | Kent | Aquaguard | ZeroB | Avimee |
|---|---|---|---|---|---|---|---|---|
| Own Shopify / e-store | O | O | O | O | O | O | O | O |
| Meta pixel on own site | O | O | O | O | O (fbq) | not checked | not checked | not checked |
| Flipkart listing | O | O | O | O | not found | O (0 ratings) | not seen | O |
| Amazon | S | S | not opened | not opened | not opened | not opened | not opened | not opened |
| Meta ads running | Not observed; I: very likely (press: "internet-first ... impressive returns on digital marketing", Velocity, Jun 2021) | I | I | I | I | I | I | I |
| YouTube | 4.72K subs, 343 videos | **144K subs, 702 videos**; "SF-15 Pro Filter: Best Hard Water Solution for Hair Fall & Dry Skin in 2026" with shop links | 650 subs, 124 videos | not found | 51.1K subs, 19 videos | not found | not found | not found |
| Blog / SEO content | TDS vs hardness, how to choose | "Why use a RiverSoft shower filter?" | "Purifit vs WaterScience" | Install, working, comparison guide | FAQ per product | Category FAQ, blog | "water softener demo" page | not seen |
| Offline / dealers | "Locate Our Store"; more than 1,000 retailers (S, Sep 2025) | not seen | not seen | none | Dealer + technician install | Service network, free install | Dealers, "Register New Installation" | not seen |
| Offers | Black Friday up to 25% off; 10% popup | MRP discounts up to 70% | 50% off MRP | ₹500 to 1,000 off, subscription | EMI | Free installation, service plan | EMI, free installation | 17 to 33% off |

Other: WaterScience LinkedIn 18,290 followers (S), 1mg listing (S), DesiDime deal (S). Kent: YouTube review "No More Hard Water! Kent Bathroom Softener Review + ₹250/Year Annual maintenance" (S). Creator collaborations: not observed for anyone.

**Hooks (on pages, not ads).** (1) Hair fall and dry skin (WaterScience badges, RiverSoft video title, Kent and Aquaguard bathroom pages, Avimee, Scale-O reviews). (2) Scale and appliance life (Eureka Forbes, Kent, ZeroB, Scale-O). (3) No maintenance, no salt (Scale-O, Alkara). **No player leads with a measured hardness number.** Hook 1 is claim-risk territory for us.

**Acquisition cost (India).**
| | Value | Source | Confidence |
|---|---|---|---|
| CPC | ₹8 to 25 all-industry; Instagram feed ₹14 to 28, Reels ₹8 to 18 | owlclaw.com agency data (O) | Low |
| CPM | ₹50 to 120 (volatile) | owlclaw; superads.ai | Low |
| CVR | 1 to 3% | assumption | Low |
| Implied CPO | ₹267 to 2,800; central ₹800 | calc | Low |
| Max CAC (shower product) | ₹730; GO ₹511 | finance §0 | Medium |

A ₹10k+ considered purchase has a longer path (dealer demo, plumber visit); the ₹730 bar does not carry over and needs a new finance run before any test. Marketplaces carry the incumbents' rating moats; D2C via Meta is the only test route that does not compete on ratings from day one. Bengaluru apartment/RWA groups are the cheapest reach but need founder OK to post.

**White space (inferred, Medium).**
- **Proof:** no before/after hardness test in a named home; only ZeroB and Kent publish capacity at a stated hardness.
- **Online social proof for real bathroom softeners is empty:** Aquaguard's three have 0 Flipkart ratings; Kent's two have a handful of on-site reviews. The category is sold by dealers.
- **Running-cost transparency:** nobody shows the salt-per-year figure of section 5.
- **Salt and service logistics:** WaterScience sells salt for Bangalore only; elsewhere buyers buy 5 to 15 kg bags on Flipkart. A salt-refill or AMC subscription is unserved by the ₹10k to 15k brands (I).
- **Society/RWA and WhatsApp-group buying** likely how B2B sells; not observable here (I).
- **Creator/YouTube:** one large channel (RiverSoft) dominates shower filters; no creator content on real bathroom softeners.

## 8. Product feasibility: the physics
| Evidence | Says | Confidence |
|---|---|---|
| Resin: 1.9 eq/L = 95 g CaCO3 per L (Purolite C100E, O); working 73 g/L (Pure Water Products, O) | Capacity is fixed by resin volume | High |
| Cartridge resin volume 0.1 to 0.35 L | **Assumption**; the bench test measures it | Low |
| Litres softened = volume x capacity / hardness | 12 to 166 L at 200 to 600 mg/L = 0.2 to 3 showers (calc §2) | Medium |
| Service flow rating 8 to 40 BV/h (Purolite C100, Resinex KW-8, Lewatit S1567; Amberlite SR1L 5 to 50) | 6 to 10 L/min through 0.1 to 0.35 L is 1,029 to 6,000 BV/h, **26 to 150x over**; hardness leaks from the first minutes (calc §3) | Medium-High (snippets, four sheets agree) |
| Larger real cartridge (2.5 x 9.75 in, about 0.6 L): 57 L at 684 mg/L, 170 L at 256 mg/L (Pure Water Products, O) | 2 to 3x a shower cartridge's resin still gives 1 to 3 showers; sold for low flow | Medium-High |
| Full-flow softening at 8 L/min and 40 BV/h | Needs about 12 L of resin: a small tank, not a cartridge | Medium |
| Indian brands' wording | "conditions", "does not chemically soften water" (RiverSoft DIVA-01) | High (O) |
| Independent lab tests (waterfilterguru) | KDF left hardness unchanged; a resin "Shower Stick" softened (single tests) | Low (S; site unreachable) |

**Conclusion:** a shower-arm resin cartridge can soften at best the first litres of a shower at Bengaluru hardness, and the strip demo would show exactly that. Selling it on "hardness reduction" with a ₹599 refill would be a claim we cannot substantiate (ASCI Chapter I) and a refill model that cannot work. This is consistent with why no Indian brand sells one.
**Bathroom-scale sizing (calc §5):** 3 to 4 people x 60 L at 250 to 500 mg/L needs about 5 to 21 L of resin for 7-day regeneration; 4 people at 350 mg/L, 9.8 to 14.7 L. Published units use 4.8 to 5.5 L and need regeneration every 2 to 5 days (section 5).
**One assumption that would change the verdict:** that a shower-arm cartridge softens at least about 1,500 L at full flow. Physics says no. Cheapest check: loose-resin column run, Appendix C (about ₹1,000 to 1,500, needs OK).

## 9. Regulatory
Not a lawyer; verify with a professional before launch.
| Item | Finding | Source, date | Blocker? |
|---|---|---|---|
| BIS compulsory certification | Not on the BIS compulsory list; only RO drinking systems (IS 16240) | bis.gov.in (O, 2026-11-26) | No |
| GST / HSN | 18%; heading 8421 in Schedule II, Notification 9/2025-IT(Rate) as amended to 2026-04-30; cartridges as parts of 8421 assumed 18% | ICAI compilation (O) | No; confirm HSN with a CA |
| Legal Metrology | Rule 6(1) label: maker/packer/importer name and address, generic name, count, month/year of manufacture, MRP "inclusive of all taxes", consumer care; 6(10) the same on the website; 6(10-A) country of origin for imports; Rule 27 registration as packer/importer, ₹500, within 90 days | Khaitan consolidated rules to 2026-02-13 (O) | No (days, ₹500) |
| E-Commerce Rules 2020; CCPA misleading-ads (2022) and dark-patterns (2023) | Grievance officer, seller details, no false urgency or fake "MRP off" | consumeraffairs.nic.in **not reachable**; prior knowledge, unverified | No, if followed |
| ASCI Code Chapter I | Claims "capable of substantiation" | ascionline.in (O) | **Yes for "softens water" on a shower cartridge**; no for a measured bathroom unit |
| Health claims | Not allowed (CLAUDE.md section 7). UK ASA upheld complaints against a softener's "glossier hair", "softer skin" (A19-565203) and a conditioner's "improve certain skin conditions" (A25-1314135) (UK, persuasive) | asa.org.uk (O) | Avoid entirely |
| Installation / plumbing goods | Warranty, service and installer obligations for a plumbed unit; not researched | | Open |
| Trademark "Mrudu" | Not searched | | Open |

## 10. Segments and persona
- **Shower product:** none. The best-fit segment from the screen (Bengaluru renter/PG on borewell water) is exactly who cannot be served honestly by a shower-arm cartridge and cannot plumb in a real softener.
- **Pivot persona (hypothesis to test in its screen):** owner-occupier households in Bengaluru's borewell and tanker zones, about 30 to 50, in an independent house, villa or an apartment with control of its own bathroom plumbing, who have already bought a ₹1.5k to 2.8k "hard water filter" and seen no change. Segment size: SAM 128k to 565k owner-occupier households (section 3, Low).
- **Reachable segments by evidence:** buyers who measure (TDS meter owners; 5+ reviewers); appliance owners with geyser or washing-machine scale (2 forum posts, brand-site reviews); renters (valued no-plumber fit; not a softener buyer); apartment/RWA buyers (I, unobserved).
- **Target areas:** section 3.

## 11. Opportunities: the pivots
| Option | What | Evidence | Status |
|---|---|---|---|
| **Bathroom softener** (5 to 15 L resin, salt-regenerated) for owner-occupied Bengaluru borewell homes | A transparent offer: customer's own hardness reading, capacity at that reading, salt cost per month, AMC price | The ₹6k to 15k band is **occupied** by ZeroB 9,891, Aquaguard 12,499, Kent 14,949 (dealers, installation, warranty), but empty of online reviews and published running costs. Real running cost ₹13k to 36k in year one; hand regeneration every 2 to 5 days is the buyer's pain and the opening. WaterScience (Bengaluru) already sells real softeners from ₹39,995 and salt | **PARK.** Competition FAIL on price band alone; PASS only if the wedge is transparency plus service. Needs its own Stage 1 screen |
| **Salt/resin service subscription** for existing Kent/ZeroB/Aquaguard owners | Salt delivery, resin servicing and AMC; low capex | WaterScience serves salt in Bangalore only; Kent AMC ₹250/yr (S); salt costs ₹3.4k to 20.8k a year (section 5); no brand publishes a service offer | **PARK, screen first** (lowest capex, no inventory). Installed base size Unknown |
| **Hardness test + "right-size your softener" guide** as lead-gen for a dealer margin | Independent testing as the funnel | Buyers want a number (section 6); one sales visit had no hardness kit (quote 10) | **Idea only.** Needs dealer margin and test cost (Unknown) |

**The three cheap facts that move PARK to GO or NO-GO:** (1) real hardness in 5 to 10 target homes (strip or lab, ₹2k to 5k; 200 vs 500 ppm changes the product); (2) what an installed ₹10k to 15k unit costs a household over 12 months, from 2 to 3 owners (needs OK to contact); (3) dealer margin, MOQ and OEM price for the same class of unit (needs OK to contact suppliers).
**Pushback on the pivots:** a bathroom softener is a different business (considered purchase, installation, after-sales, salt logistics, plumbing warranty). A part-time founder needs a service partner, which is a contact and spend step needing OK. Ceiling illustration (assumptions): at ₹2k to 4k contribution after CAC per installed unit, ₹50k/month needs 13 to 25 units a month.

## 12. Launch plan and growth potential, if the venture continues
**Not a launch, a decision path (first 90 days).**
| Days | Step | Cost | Founder OK? |
|---|---|---|---|
| 0 to 7 | Founder decides: accept NO-GO on the shower form, or run the loose-resin column check | ₹0 / about ₹1,000 to 1,500 | Yes if spend |
| 0 to 7 | Stop all Mrudu landing, brand and ad work | ₹0 | CEO |
| 7 to 21 | Stage 1 screen of the pivots (section 11) | ₹0 | CEO confirms |
| 21 to 45 | If it passes: supplier quotes, 1 sample unit, full-flow bench test (Appendix C runs A and B) | ₹8k to 15k (Low) | Yes |
| 45 to 90 | If it passes: refundable pre-order smoke test, Bengaluru borewell zones, ₹25k ad cap (`playbooks/smoke-test.md`) | ₹25k | Yes |

Kill checkpoints: day 7 (founder decision), day 21 (pivot screen), day 45 (unit fails 1,500 L, or landed cost leaves no margin at ₹6k to 12k), day 90 (CPO vs new bars from Finance).

**Growth potential**
- Shower form: no honest repeat (a cartridge that lasts a shower cannot be refilled at ₹599 honestly). Ceiling 0.
- If a working product existed at ₹1,999: Bengaluru month-12 net about ₹10k to 26k a month at CPO ₹511 to 600, far below ₹50k.
- Second cities (Low; dated or snippet): Hyderabad has hardness above the permissible limit in 75 to 84% of 44 samples (2023; TNM 2026-09-14); Pune PCMC basalt groundwater 220 to 360 mg/L (MPCB 2014); Chennai coastal mean about 286 mg/L, Perungudi 610 to 675 (S, 2011). The problem is national, and so are the incumbents. Multi-city does not rescue the shower form; for a pivot, Hyderabad is the natural second city.
- **Economics fit:** shower product, contribution ₹937 per kept order before refunds, landed cost ₹600 is a placeholder; ₹50k/month needs 178 / 228 / 384 orders a month at CPO ₹450 / 511 / 600 vs a channel SOM of 27 to 111 a month. Hand-off to Finance for new bars at ₹6k to 15k only if a pivot passes its screen.

## 13. Kill-criteria scorecard
Rule (`playbooks/market-research.md`): any must-pass FAIL = NO-GO; UNKNOWN on a must-pass = PARK.
| # | Criterion | Shower form | Bathroom softener (pivot, from this evidence only) |
|---|---|---|---|
| 1 | Side-income size (must) | **FAIL**: needs about 228 orders/month at GO CPO; SOM 27 to 111/month; no honest repeat | UNKNOWN: no sizing at ₹10k+; BBMP 20 to 22 lakh properties known, hard-water share and WTP not |
| 2 | Test affordability (must) | PASS (moot): ₹25k ad cap; MOQ unknown | UNKNOWN: unit cost not sourced (resin ₹100 to 330/L, S) |
| 3 | CAC feasibility (must) | PASS at optimistic end only (₹267 vs ₹730) | UNKNOWN: needs a new max-CAC run at ₹10k+ |
| 4 | Regulatory blocker (must) | PASS: no BIS QCO; LM registration ₹500; GST 18% | PASS so far (same findings) |
| 5 | Margin 35% or more | PASS (model): 47% before refunds | UNKNOWN |
| 6 | Competition wedge | **FAIL**: wedge depends on a claim the product cannot back; incumbents at the same price with 4,381-rating listings | FAIL on price band alone (three incumbents); PASS if wedge is transparency plus service; needs a test |
| 7 | Demand evidence | PASS: 379 reviews, 13,079 Flipkart results for "shower filter for hard water", Bengaluru 15% of the first sample | PASS for the problem; WTP at ₹6k to 15k Unknown |
| 8 | Claim risk (must) | **FAIL** (Medium-High): capacity 12 to 166 L, flow 26 to 150x over rating; ASCI Chapter I | PASS if hair/skin claims avoided (every competitor's main hook is in that zone) |
| 9 | Concentration | PASS (n/a) | UNKNOWN: depends on one supplier and one service partner |

**Result: shower form 2 must-pass FAIL (1, 8) and 1 other FAIL (6) = NO-GO. Pivot: UNKNOWN on must-pass 1, 2, 3 = PARK with named validation tasks (section 14).**

## 14. Unknowns and next tests
Cheapest first; founder OK needed where marked.
1. Founder: accept NO-GO or run the loose-resin column check (₹1,000 to 1,500; OK).
2. Area-level hardness from CGWB/NAQUIM Bangalore Urban reports (free; needs a network that can reach cgwb.gov.in).
3. Reddit, Quora, apartment-group voice (blocked here; a human can read them in a browser, free).
4. Census 2011 HL-04 owner/renter split and current household count for Bengaluru (free).
5. Real hardness in 5 to 10 target homes (₹2k to 5k; OK to spend and to ask friends or neighbours).
6. 12-month cost of an installed unit from 2 to 3 owners (interviews; OK to contact).
7. Dealer margin, MOQ and OEM landed cost for 5 to 15 L manual-regeneration units (supplier quote; OK).
8. WTP at ₹6k to 15k (refundable pre-order smoke test, later).
9. Meta Ad Library and Instagram counts for the ten brands (a founder browser session); Amazon.in ranks and ratings; YouTube comments.
10. CCPA guideline text and E-Commerce Rules (CA or lawyer; consumeraffairs.nic.in unreachable here); HSN confirmation; trademark search for "Mrudu" only if the name is kept.
11. Aquaguard C-500: which of ₹38,990 and ₹20,349 is the selling price (unresolved; ₹38,990 used).

## 15. What we're missing
- **Non-buyers with the problem.** The sample is people who already bought a cartridge, liquid or tank media. The ₹10k softener sells to homeowners who bought nothing; their voice (Reddit, RWA and WhatsApp groups) was blocked.
- **Customer interviews** with 5 to 10 borewell-home owners: nobody has talked to a customer.
- **Hardness in actual target homes.** All hardness data is 2010 to 2022, sampled by government, vendors or surveys; none at pin-code level.
- **Supplier and dealer economics** for any real softener: landed cost, MOQ, margin.
- **Installer and service model** for a plumbed product.
- **Ads.** No ad was observed; hooks are page claims. A founder browser session on the Ad Library would close this.
- **Studio process.** The studio built a landing page, brand kit and ad plan before a datasheet check that takes an hour. Research must precede build (the playbook now says so).
- **Name and trademark** for "Mrudu"; check only if the name survives a pivot.

---
## Reconciliation notes (where earlier drafts disagreed; newer, page-verified figure used)
| Item | Earlier value | Used here | Why |
|---|---|---|---|
| WaterScience RENO entry price | from ₹34,995 (market-research.md) | RENO 1,500 at ₹39,995 | Landscape page read in full |
| Installed softener range | ₹14,949 (S) to ₹1,39,995 | ₹9,891 to ₹2,49,000 | Landscape added ZeroB 9,891 and Aquaguard I-17500 2,49,000 |
| Kent bathroom ₹14,949 and 8 L ₹30,500 | search snippet | page-verified | kent.co.in opened |
| RiverSoft price | ₹1,440 to 1,799 | ₹1,440 to 2,049 (SF-15 1,549; DIVA-01 1,699) | Product feed and landscape page |
| Snix price | ₹943 | ₹857 to 943 | Two listings |
| Price-gap framing | "nothing between ₹2.8k conditioners and ₹15k installed softeners" | Band ₹6k to 15k holds three real softeners; only ₹4.7k to 9.9k is salt-free-only (Alkara 4,999) | Landscape found ZeroB, Aquaguard, Kent |
| Reviews sample | 181 (+5 on-site) | 379 Flipkart reviews | 181 + 198 new |
| Quotes | 30 | 72 (30 + N1 to N42) | Landscape addendum |
| Purifit 1 to 2 star | 9.0% (356 ratings) | 9.0% (head); 14.7% (Atom, 75 ratings) | Two different listings |
| Scope | India + UAE | India only | Founder decision 2026-11-26; UAE content dropped |

The /50 attractiveness score and the shower-form scorecard are carried from the deep dive unchanged.

## Appendices
- **A. Verbatim quotes and source URLs:** [`customer-voice.md`](customer-voice.md) (72 quotes, segment tags, theme counts).
- **B. Source ledger** (URL, date, what it gave, opened / snippet / blocked): [`sources.md`](sources.md).
- **C. Bench-test spec** (loose-resin column check and full-flow runs; spec only, buying needs OK): [`bench-test-spec.md`](bench-test-spec.md).
- **D. Calculations:** [`calc/`](calc/): `stage2_calc.py` + output (capacity, flow, TAM/SAM/SOM, competitor-led, side-income gap), `landscape_calc.py` + output (implied resin capacity, salt cost, 12-month costs, star shares), `landscape_theme_counts.py` + output and `review_theme_counts.txt` (review themes).
- **E. Raw captures:** [`raw/`](raw/) (dated page captures; reviews with names removed).
- **F. Superseded drafts:** [`archive/`](archive/) (`market-research.md`, `india-landscape.md`, `competitors.md`).

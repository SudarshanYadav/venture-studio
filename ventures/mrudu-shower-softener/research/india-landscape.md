# India hard-water landscape: players, prices, customer problems, channels
Date: 2026-11-26 | Researcher: Market Researcher | Scope: India only (UAE dropped by founder) | Currency: INR, tax-inclusive shelf prices as displayed (Legal Metrology Rule 2(m); see `sources.md`)
Method: competitor-profiling and customer-research skills, WebFetch alternative stack (curl through the session proxy, pages converted to text; WebFetch itself cannot resolve hosts in this session). **SEO metrics: unavailable. Meta Ad Library: could not be read (see section 3).** Raw files: `research/raw/landscape/2026-11-26/`. Calculations: `research/calc/landscape_calc.py` and `landscape_theme_counts.py` (outputs saved beside them).

Evidence tags used below: **O** observed (page I opened, 2026-11-26), **S** search snippet only, **I** inferred (my reasoning, stated as such). Confidence H / M / L.

---

## 0. The answers to the founder's four questions, in one screen

1. **Who are the players?** 20 named players in 6 categories (section 1). Three clusters: (a) shower/tap "conditioners" at ₹0.4k to 4.7k (WaterScience, RiverSoft, Purifit, Snix and about 20 marketplace white-labels); (b) real salt-based ion-exchange softeners at ₹9.9k to ₹1.4 lakh from big brands and dealers (Kent, Aquaguard/Eureka Forbes, ZeroB/Ion Exchange, A.O. Smith, WaterScience RENO); (c) overhead-tank "scale protectors" at ₹3k to 8k a year (Scale-O, D'Cal, aaeqovo9, Neeva).
2. **Price points?** See the ladder (section 2). The **₹6k to 15k band holds only three real softeners: ZeroB bathroom softener ₹9,891, Aquaguard AWS I-250 ₹12,499, Kent bathroom softener ₹14,949.** Between ₹4.7k and ₹9.9k there is nothing salt-based except Alkara's ₹4,999 "chemical-free" unit (salt-free, so a conditioner by its own description).
3. **Customer problems?** 42 new verbatim quotes in `customer-voice.md`. Buyers want: softer-feeling water for hair and skin (largest motive by mention), less scale and stains on fittings, geysers and washing machines. They complain about: "no change" (single biggest complaint in every cartridge and tank-media listing), life shorter than claimed, TDS meters that do not move, and (on real softeners) manual salt regeneration and one-bathroom capacity.
4. **Marketing channels?** Marketplace (Flipkart for all; Amazon.in could not be opened), own Shopify store with Meta pixel installed, YouTube (RiverSoft 144K subscribers; others small), brand-site FAQ/blog content, and for real softeners dealer/installer networks and AMC. **I could not observe a single ad**: Meta Ad Library and Instagram refused automated access. Ad hooks below are therefore the claims on brand pages, not ad creative.

**Verdict on the pivot question (detail in section 6):** a real bathroom-scale softener at ₹6k to 15k is a real, un-served gap on *online proof and price transparency*, but it is **not an empty price band** (three branded incumbents), and the published specs show a bathroom unit must be regenerated with salt every 2 to 5 days for a family on Bengaluru-type borewell hardness. That is the product's real selling problem, and also the opening. Recommendation: **PARK, do not GO, until three cheap facts are in** (section 7).

---

## 1. Current players

Prices: tax-inclusive as displayed. "Rating count" is the marketplace figure on the day. 12-month cost = unit + replacement media or salt for one household, ranges, with the assumption stated in the last column of section 2.

### 1a. Shower and tap filters ("conditioners")
| Player | Mechanism (their words) / soften or condition? | Price (₹) unit; media | 12-month cost | Where sold (O) | Rating count | Claim and proof | Tag |
|---|---|---|---|---|---|---|---|
| **WaterScience** (Bengaluru, est. 2014) | KDF + "converts hard water salts into harmless forms"; **conditions, does not reduce TDS** (own FAQ) | CLEO SFM-419 2,795 (MRP 3,495); CLEO tap 1,495; cartridge 845 (2 for 1,595), "4 to 6 months" | 3,640 to 4,485 (shower) | Own Shopify, Flipkart, Amazon, 1mg listing (S), "more than 1,000 offline retailers" (S, Sep 2025 press) | Flipkart: CLEO tap 4,381 (3.8); 717 156 (3.8); SFU-423 226 (3.9); single-flow 77 (4.4); SFM-419 multi-flow 4 (3.5) | "Reduces the effects of hardness"; badges "Reduces Hairfall", "Protects Skin"; no hardness number | O |
| **RiverSoft** (Bengaluru, est. 2019) | KDF, calcium sulphite, carbon, vitamin C, mineral balls; DIVA-01 page: "does not chemically soften water" | SF-15 1,549 (MRP 4,999); DIVA PRO 1,440; DIVA-01 1,699; 2-cartridge pack 1,368 | 2,233 to 2,917 | Own site, Flipkart, Amazon (S) | SF-15 924 (3.9); DIVA PRO 442; DIVA-01 87 (4.1) | "helps reduce hardness"; none proven | O |
| **Purifit** | KDF-55, carbon, polyphosphate; "non-RO, non-softener" | Flipkart head 999 (MRP 1,999); Atom 1,719; Ultra 1,499; cartridge 699 to 849 | 1,698 to 3,197 | Own site, Flipkart | 356 (4.4); Atom 75 (**11 of 75 ratings are 1 to 2 star, 14.7%**) | "98.1% scale reduction" lab claim; report not opened | O |
| **Snix** | "Hard Water Softener" in title; media not stated | 857 to 943 | Unknown (cartridge not found) | Flipkart only (site parked) | 308 (3.7) and 11 (3.8) | None | O |
| **Wevora / Flaner / WaterLabs / Wallberrie / Suicune / Poolcraft / Eshva / TruQual** (marketplace white-labels, 15 to 22 stage) | KDF, vitamin C, "stages" | 448 to 1,199 (MRP up to 5,999; 50 to 88% "off") | 900 to 2,400 (assumes 1 to 2 refills; refills often unavailable) | Flipkart | Mostly under 150; WaterLabs HL-40 66 (4.1); Wevora 136 | "Softener", "Reduces Hair Fall" in titles; none proven | O |
| **Tap-mount mesh filters** (gvantikA, DEAGAN, Rainflow) | Mesh or cotton aerator, **not a hardness product** but sold in the same search | 130 to 380 | n/a | Flipkart | gvantikA 3,473 (4.1); DEAGAN 427; Rainflow 1,562 | Sediment only | O |

### 1b. Liquid or "instant" softeners (bucket-bath substitute)
| Player | Mechanism | Price (₹) | 12-month cost | Where | Rating count | Claim | Tag |
|---|---|---|---|---|---|---|---|
| **Avimee** | Sodium gluconate + apple cider vinegar (reviewer quote of the label) | 410 per 400 ml (MRP-linked 17% off); 742 to 1,000 larger packs | About 4,900 **if** one bottle a month (assumption; dose is "three caps per bucket" per one reviewer, bottle yield unknown) | Flipkart, own site (home page blocked a full read) | **4,805 (4.2); 10.0% are 1 to 2 star** | "Hairfall control" in title | O |
| Swoffy, Kidzelo, Khubee, Ramiloo, Parisar Pharma, Mokleva, Vrootoo | Same format | 195 to 575 | Same | Flipkart | Swoffy 5 to 42; others under 40 | "Instant water softener", "Hair fall control" | O |

### 1c. Overhead-tank and whole-house "scale protectors" (no salt, no electricity)
| Player | Mechanism | Price (₹) | 12-month cost | Where | Rating count | Claim and proof | Tag |
|---|---|---|---|---|---|---|---|
| **Scale-O** | Media dropped in the overhead tank (floats); its own page: "Does not reduce TDS", "Does not change pH, colour, taste" | Mini 3,000 (6 months), 5,000 (1 year, 2 cartridges); Semi 4,000 / 7,000; Centi 4,500 / 8,000 | **5,000 to 8,000** (subscription model, scale-o.com) | Own Shopify (Meta pixel installed, O), Flipkart | Flipkart 24 (4.2); 3 of 24 ratings are 1 to 2 star | "Helps reduce scale buildup"; comparison guide; ₹500 to 1,000 off, free shipping | O |
| **D'Cal** | "Solid filter cartridge", anti-scale; mechanism not stated on the listing | 4,174 (7% off) | Unknown (life not shown) | Flipkart; "free demo kit" mentioned by a reviewer | **932 ratings, mean 3.72, 22.2% are 1 to 2 star** | "Hard water softener" in title | O |
| aaeqovo9, Neeva, GD Water, ScaleO look-alikes | Tank media | 2,246 to 3,186 | Unknown | Flipkart | 0 to 6 shown | "Skin and hair solution" | O |

### 1d. Bathroom (point-of-use) salt-regenerated softeners
| Player | Product | Price (₹) | Spec published (O) | 12-month cost (unit + salt) | Where | Rating count |
|---|---|---|---|---|---|---|
| **ZeroB** (Ion Exchange India) | Bathroom Softener (point of use), manual | **9,891** (MRP 10,990) | 8 to 10 L/min; max raw hardness 500 ppm; outlet below 50 ppm; **300 L per recharge at 500 ppm, 600 L at 250 ppm**; recharge 30 min | 9,891 + salt 3.4k to 21k (section 2b) | zerobonline.com, dealers | Not on Flipkart sample |
| **Aquaguard** (Eureka Forbes) | AWS I-250 bathroom; I-600 NXT manual POU; C-500 automatic | I-250 **12,499** (Flipkart; 13,999 in a search snippet); I-600 NXT 16,999 Flipkart / 19,999 company page; C-500 37,990 to 38,990 | Brand page names "ion-exchange", 1-year warranty, free installation and service plan; capacity per litre of salt not stated on the pages read | Unit + salt (not published) | eurekaforbes.com, Flipkart | **0 ratings** on all three Flipkart listings |
| **Kent** | Bathroom Water Softener (5.5 L resin, manual, no electricity) | **14,949** | Flow 1,000 L/h; **about 1,500 L per regeneration at 200 ppm hardness**; 880 g salt per regeneration; 1-year warranty; resin servicing every 12 to 18 months | 14,949 + salt 3.4k to 21k; AMC ₹250/yr per a YouTube title (S, unverified) | kent.co.in, dealers | 2 on-site reviews |
| Kent | Automatic Water Softener 8 L | 30,500 | 1,200 L/h; about 2,200 L per regeneration at 200 ppm; 1.28 kg salt; weekly to monthly refill by use | 30,500 + salt | kent.co.in | On-site only |
| **Alkara** | Bathroom Softener W3 ("chemical-free", salt-free) | 4,999 (Bajaj Finserv price list, 2026) | Salt-free = conditioner by its own description (I) | 4,999 | Bajaj Finserv EMI listing, dealers | Not seen |
| **A.O. Smith** | CWS-25, CWS-40 (automatic, "flow and time based") | Price not shown on page | Capacities not read | n/a | aosmithindia.com | n/a |

### 1e. Whole-house, automatic and apartment/society (B2B-ish)
| Player | Product | Price (₹) | Notes | Tag |
|---|---|---|---|---|
| **WaterScience RENO** (Bengaluru) | RENO 1,500 (1 bathroom/kitchen) 39,995; 2 bathrooms 49,995; whole house 69,995; Polaris (apartment, up to 4 members) 64,995; Altius touch-screen 109,995 to 139,995; Aquilus 54,995; salt tablets 980 ("Bangalore location only") | 5-year valve warranty on Polaris; installation video; "Locate Our Store" | O |
| **Aquaguard** whole-house | I-2500 69,990; C-3000 79,990; Select 5000 104,990; 7500 124,990; I-17500 249,000 | "Free Service Plan including free unit installation and unlimited repair visits" | O |
| **ZeroB** | Nano Soft 37,790 (resin 4.8 L, 2.5 kg salt for four recharges, up to 600 L/h); AS1 about 46,150, AS2 about 64,990 (S) | Free home installation, EMI, "Register New Installation" page | O / S |
| **3M** (apartments and individual houses) | YouTube videos on apartment softening seen in search results; commercial price ₹4.27 lakh seen in a dealer snippet | Society B2B; not researched further | S |
| Livpure, Pureit, Havells, Hindware | **No softener product found** on home pages or in search | They sell RO and heaters; not competitors here | O (not exhaustive) |
| Culligan, Hello Klean | Hosts unreachable through the session proxy | Unknown | not opened |
| Kinetico | US site only, no India presence observed | | O |

Count of named players: WaterScience, RiverSoft, Purifit, Snix, Wevora, WaterLabs, Suicune, Poolcraft, Avimee, Swoffy, Kidzelo, Scale-O, D'Cal, aaeqovo9, Neeva, Alkara, ZeroB, Kent, Aquaguard, A.O. Smith, 3M, plus about 20 unbranded white-labels.

---

## 2. Price points

### 2a. Price ladder (tax-incl. list or shelf price, ₹, 2026-11-26)
| Tier | Range | Players | What the buyer gets |
|---|---|---|---|
| Liquid "instant softener" | 195 to 575 per bottle | Avimee, Swoffy, Kidzelo | A bucket-bath additive; ongoing cost |
| Generic shower/tap heads | 400 to 1,200 | White-labels, Snix, WaterLabs | Media cartridge; no proof |
| Branded conditioners | 1,000 to 2,800 | Purifit, RiverSoft, WaterScience tap | KDF/polyphosphate; "conditions" |
| Premium conditioners | 2,300 to 4,700 | WaterScience multi-flow, RiverSoft Diva Elite | Same media, nicer head |
| Tank scale protectors | 3,000 to 8,000 a year | Scale-O, D'Cal, Neeva | Subscription media in the tank |
| **Salt-free "bathroom softener"** | **4,999** | Alkara | Conditioner by description |
| **Real bathroom ion-exchange (manual)** | **9,891 to 19,999** | ZeroB 9,891; Aquaguard I-250 12,499, I-600 NXT 16,999 to 19,999; Kent 14,949 | Salt regeneration, resin |
| Automatic point-of-use / small whole-home | 20,000 to 40,000 | Aquaguard C-500; Kent 8 L 30,500; ZeroB Nano 37,790; RENO 1,500 at 39,995 | Auto regeneration |
| Whole-house / apartment | 55,000 to 2,49,000 | RENO Stellaris/Polaris/Altius; Aquaguard I-2500 to I-17500; ZeroB AS series | Installed by dealer |

Observed discounting: shower-filter white-labels show "50 to 88% off" against inflated MRPs; branded D2C show 17 to 69% off MRP; Scale-O and WaterScience run sale banners ("Black Friday Sale ... upto 25% Off"). CCPA dark-pattern and misleading-price rules apply if we copy that (verify with a professional).

### 2b. What a "₹6k to 15k" bathroom softener costs to run (calculation, Low-Medium confidence)
Inputs: the makers' published capacities (Kent: 5.5 L resin, 1,500 L at 200 ppm, 880 g salt; ZeroB: 300 L at 500 ppm; both imply about 1.1 eq per litre of resin, so they are consistent). **Assumptions (mine):** 4 people, 8-minute showers at 9 L/min = 288 L/day through the unit; salt ₹56 to ₹136/kg (Flipkart: 15 kg bag ₹834, 5 kg ₹680, 2026-11-26); salt dose per regeneration unchanged with hardness (understates cost at high hardness).

| Raw hardness (CaCO3) | Litres per regeneration (5.5 L resin) | Regenerate every | Salt per year | Salt cost per year |
|---|---|---|---|---|
| 200 ppm | about 1,500 | 5.3 days | 61 kg | ₹3.4k to 8.3k |
| 350 ppm | about 860 | 3.0 days | 107 kg | ₹6.0k to 14.6k |
| 500 ppm | about 600 | 2.1 days | 153 kg | ₹8.5k to 20.8k |
Bengaluru borewell hardness is reported from below 100 to above 500 mg/L by area (DrinkPrime 2022 sampling: Whitefield 96 to 492, Electronics City 8 to 580; see earlier `sources.md`), so a typical buyer is somewhere between the first and third rows. **So the 12-month cost of a ₹10k to 15k bathroom unit is about ₹13k to 36k, and a family regenerates it by hand every 2 to 5 days.** None of the brand pages read shows this running cost. Scripts: `calc/landscape_calc.py`.

---

## 3. Marketing channels, from evidence

### 3a. What I could and could not observe
| Source | Result 2026-11-26 |
|---|---|
| Meta Ad Library (country India) | **403 from the page; JavaScript-only.** No ad counts or hooks observed for any player. Not worked around. |
| Instagram profiles | 302 redirect to login. **Follower counts not observed.** |
| Amazon.in search | 503 error page. **Ranks and rating counts for Amazon not observed.** |
| Reddit | Returned an empty application shell (no content); the fetch tool also refuses reddit.com. Nothing read. |
| Quora, Team-BHP, TechEnclave, DesiDime, IndiaMART, Sulekha | 403. Not worked around. |
| YouTube channel pages | Opened: subscriber and video counts read. Video-level views and comments not read (needs JavaScript or API). |
| Google search ads, SEO traffic | Not observable without paid tools. |
| Quick commerce (Blinkit, Zepto, Instamart) | Needs app and location; not checked. |

### 3b. Channel map by player
| Channel | WaterScience | RiverSoft | Purifit | Scale-O | Kent | Aquaguard | ZeroB | Avimee |
|---|---|---|---|---|---|---|---|---|
| Own site (Shopify) | O | O | O | O | O (own e-store) | O | O | O |
| Meta pixel on own site | **O** (facebook_pixel in home page source) | **O** | **O** | **O** | **O** (fbq) | not checked | not checked | not checked |
| Flipkart listing | O | O | O | O | not found | O (0 ratings) | not seen | O |
| Amazon | S (listed on press) | S | not opened | not opened | not opened | not opened | not opened | not opened |
| Meta ads running | **Not observed** (library blocked); I: very likely, press quote calls it "internet-first ... impressive returns on digital marketing" (Velocity, Jun 2021) | I only | I only | I only | I only | I only | I only | I only |
| YouTube | **4.72K subs, 343 videos** (O) | **144K subs, 702 videos**; featured video "SF-15 Pro Filter: Best Hard Water Solution for Hair Fall & Dry Skin in 2026" with shop links and a WhatsApp number (O) | 650 subs, 124 videos (O) | not found | 51.1K subs, 19 videos (O) | not found | not found | not found |
| Instagram | linked; counts not observed | linked | linked | linked | linked | not checked | not checked | not checked |
| Other social | LinkedIn 18,290 followers (S) | Product Hunt profile and launch (S) | none seen | Facebook page | | | | |
| Blog / SEO content | O: blogs on TDS vs hardness, how to choose a softener, whole-house vs shower filter | O: blog "Why use a RiverSoft shower filter?" | O: "hard water effect" and "Purifit vs WaterScience" pages | O: installation, working, replacement guide and comparison page | O: FAQ pages per product | O: category FAQ and blog posts | O: "water softener demo" page | not seen |
| Offline retail / dealers | **O/S: "Locate Our Store", "Find the Nearest Store"; more than 1,000 offline retailers (press, Sep 2025)** | not seen | not seen | none (online) | O: dealer and technician installation | O: service network, free installation | O: dealers, "Register New Installation" | not seen |
| Pharmacy marketplace | 1mg listing (S) | | | | | | | |
| Deal sites | DesiDime deal for CLEO (S; page blocked) | | | | | | | |
| Offers | Black Friday up to 25% off; "10% off!" popup | Heavy MRP discounts (up to 70%) | 50% off MRP | ₹500 to 1,000 off, free shipping, subscription plans | EMI | Free installation, service plan | EMI, free installation | 17 to 33% off |
| Trial / demo | | | | "Trial plan" 6 months | | | "water softener demo" page | D'Cal: "free demo kit" (reviewer, O) |
| Creator content | Not observed | Not observed | Not observed | Not observed | YouTube review video "No More Hard Water! Kent Bathroom Softener Review + ₹250/Year Annual maintenance" seen in search results (S) | | | |

### 3c. Hooks (claims on brand pages; not ad copy)
Observed on pages, not on ads: **hair fall and dry skin** (WaterScience badges, RiverSoft YouTube title, Kent and Aquaguard bathroom pages "reduces hair loss", Avimee "Hairfall control", Scale-O reviews). Second hook: **scale and appliance life** (Eureka Forbes, Kent, ZeroB, Scale-O). Third: **no maintenance, no salt** (Scale-O, Alkara). **No player leads with a measured hardness number.** These health-adjacent hooks are claim-risk territory for us (CLAUDE.md section 7: no medical or hair-fall claims).

### 3d. White space (inferred from the above, Medium confidence)
- **Proof:** no player publishes a before/after hardness test in a named home. Only ZeroB and Kent publish capacity at a stated hardness.
- **Online social proof for real bathroom softeners is empty:** Aquaguard's three bathroom softeners have 0 Flipkart ratings; Kent's two have a handful of on-site reviews. The category is sold by dealers and brand sites, not on marketplaces.
- **Running-cost transparency:** nobody shows the salt-per-year figure of section 2b.
- **Salt and service logistics:** WaterScience sells salt "Bangalore location only"; outside it, buyers buy 5 to 15 kg bags on Flipkart. A salt-refill or AMC subscription is unserved by the ₹10k to 15k brands (I).
- **Society/RWA and WhatsApp-group buying** (apartments sharing a borewell) is likely how B2B sells; not observable here (I).
- **Creator/YouTube:** a single large channel (RiverSoft) dominates shower filters; no creator content on real bathroom softeners beyond a few video titles.

---

## 4. Customer problems and feedback
New sample: **198 unique Flipkart reviews** across 7 listings (Avimee liquid softener, D'Cal tank unit, Scale-O, RiverSoft DIVA-01, WaterScience CLEO 717 and single-flow, Purifit Atom), plus 2 brand-site reviews (Kent), plus 5 forum-question quotes (India Water Portal, 2010 and 2013). **42 verbatim quotes with URLs are in `customer-voice.md`, section G onwards (numbered N1 to N42).** Combined with the 181 reviews already in that file, the sample is 379 Flipkart reviews. The sample is sorted negative-first and most-helpful, so counts are **not market shares**. Keyword counts (approximate, `calc/landscape_theme_counts_output.txt`).

### 4a. The problem people are trying to solve (the "job")
| Theme | Count in the 198 new reviews | Example (quote # in customer-voice.md) |
|---|---|---|
| Hair and skin feel (dryness, itching, rough hair) | 37 | N1, N14, N28 |
| Scale, stains, deposits on fittings, buckets, pipes, geysers | 10 | N3, N13, N26 |
| Appliance damage (geyser, washing machine clogging) | 2 forum questions plus brand-site copy | N39, N40 |
| Soap and shampoo lather | 1 brand-site review | N37 |
| Renter/PG, no-plumber fitting | 7 mention easy install | N31 |
Observed (O): hair and skin dominate unprompted motives, as the first screen found. Scale and appliance protection is the second motive and is the one we can describe with measurable facts.

### 4b. Complaints about current products
| Theme | Count (keyword, approximate) | Evidence |
|---|---|---|
| "No change / waste / not working" | 54 of 198 (51 of the 67 one- and two-star reviews) | N5, N6, N22, N27, N35 |
| Life shorter than claimed ("one week", "3 months", "20 days") | 10 | N18, N20, N21, N33, N34 |
| Adverse reaction attributed to the product (more hair fall, itching, darker skin) | 11 (all on the liquid) | N8, N9, N10, N11 |
| Price or value | 6 | N4, N5, N17 |
| TDS or hardness measured by the buyer and not moving | 8 | N16, N22, N35 |
| Salt, maintenance, regeneration | 5 | N24, N25, N36, N37 |
| Distrust of reviews | 3 | D'Cal, Avimee reviews (not quoted by name) |
| Breakage and fit (first screen) | 24 of 87 low-star | see earlier sections B to C |

### 4c. Unmet needs and price objections
- **"Softeners are challenging to operate"** (N24): the leading unmet need is softening **without manual salt regeneration**. Kent's own review: "salt refilling is something you need to manage regularly" (N37).
- **Capacity**: "works well for one bathroom but is not sufficient for the entire house" (N36).
- **Proof**: people reach for TDS meters, which cannot show hardness change (N15, N16, N22, N35); one sales visit measured TDS 514 and guessed hardness at about 250 (N38).
- **Price**: "price is very high" for the quantity (N4, N17); "slightly expensive" for a ₹30k unit (N37).
- **Renters**: easy fit "no need of plumber" (N31) is valued; a plumbed ₹10k+ unit loses that.

Not available: Reddit, YouTube comments, Quora, Amazon reviews, WhatsApp groups. The people who have the problem but have not bought anything are therefore under-sampled.

---

## 5. Channel economics context (carried from the earlier report, not re-verified)
India Meta CPC ₹8 to 25, CPM ₹50 to 120 (agency data, Medium); the finance model's max CAC for the ₹1,999 Mrudu product was ₹730. A ₹10k+ considered purchase has a longer path (dealer demo, plumber visit); a ₹730 CAC bar does not carry over and needs a new finance run before any test.

---

## 6. What this means for a pivot (India, Bengaluru borewell homeowners)
**Observed facts that matter**
1. The ₹6k to 15k real-softener band is **occupied** by ZeroB (₹9,891), Aquaguard (₹12,499), Kent (₹14,949), each with dealers, installation, warranty, and a large brand. It is **empty of online reviews and published running costs**.
2. Cartridge and tank-media products are cheaper but draw the loudest "no change" complaints (10% to 22% one- and two-star) and give buyers no number. Real softeners show no such complaint volume because they have almost no online reviews at all.
3. The published specs imply a bathroom resin unit needs manual salt regeneration every 2 to 5 days for a four-person home (section 2b).
4. WaterScience (Bengaluru) already sells real softeners (₹39,995 and up), salt, and has offline retail. It is the nearest competitor to the persona.

**Inferred (Medium to Low)**
- A pivot is a **different business** from the first idea: considered purchase, installation, after-sales, salt logistics, warranty on plumbing goods. A founder running this part-time from a distance needs a service partner (plumber/installer), which is a contact and spend step that needs founder OK.
- A defensible wedge would be **transparency**: sell with the customer's own hardness reading, the capacity at that reading, the salt cost per month, and the AMC price, none of which the three incumbents publish. This is a claim about measurable product facts, not about hair or skin.
- Alternative wedges worth a look before choosing the bathroom softener: (a) a **salt-and-resin-service subscription** for existing Kent/ZeroB/Aquaguard owners (low capex; WaterScience serves Bangalore only for salt); (b) **independent hardness testing plus a "right-size your softener" guide** as a lead-gen funnel for a dealer margin.

**Kill criteria status (playbook section 5), for the bathroom softener, from this evidence only**
| # | Criterion | Status |
|---|---|---|
| 1 Side-income size | UNKNOWN: no sizing done on this landscape; 20 to 22 lakh BBMP properties and borewell reliance are known, share with hard water and willingness at ₹10k+ are not |
| 2 Test affordability | UNKNOWN: unit cost not sourced; resin cost earlier ₹100 to 330/L (S) |
| 3 CAC feasibility | UNKNOWN: needs a new max-CAC run at ₹10k+ price |
| 4 Regulatory | PASS so far: earlier BIS compulsory list review found no entry for softeners (O, earlier file); GST 18% for 8421 (O, earlier) |
| 8 Claim risk | PASS if we avoid hair/skin claims; every competitor's main hook is in the claim-risk zone |
| 6 Competition | FAIL on price band alone (three branded incumbents), PASS if wedge is transparency plus service; needs a test |

---

## 7. Unknowns, cheapest first (founder OK needed where marked)
1. **Real hardness in the target homes** (200 vs 500 ppm changes the product, section 2b). A strip test kit or lab test of 5 to 10 homes (needs founder OK to spend about ₹2 to 5k, and to ask friends or neighbours).
2. **What an installed ₹10k to 15k unit actually costs a household in 12 months** from two or three owners (interviews; needs founder OK to contact people).
3. **Dealer margins, MOQ and OEM price for the same class of unit** (contacting suppliers; needs founder OK).
4. Meta Ad Library and Instagram follower counts for the ten brands: needs a browser session by the founder, or the facebook.com ads-library host and instagram.com allowed with a logged-out browser. I did not try to get around the block.
5. Amazon.in ranks and ratings for the same players (host returned 503).
6. YouTube comments on the top review videos (for more customer voice).

## 8. Pushback and gaps
- The first screen's "what customers want" was measured on **people who already bought a cartridge product**. This file adds a liquid and a tank-media sample, but still not a sample of **homeowners with the problem who bought nothing**. That is the segment a ₹10k softener sells to.
- The brief said "at least 15 players". Counted: 20 named. But for **real softeners I could read specs for only four**; prices for ZeroB AS series, Alkara, 3M are from price-list snippets or aggregators, marked S.
- Aquaguard's C-500 list page shows both ₹38,990 and ₹20,349 near the product; I did not resolve which is the selling price and used ₹38,990.

## 9. Files read in full vs snippet
Opened in full (text read): kent.co.in two product pages; eurekaforbes.com category page and two product pages; waterscience.in products feed, two RENO pages; theriversoft.com products feed and home; purifit.in home; scale-o.com home, products feed and product page; zerobonline.com three pages; aosmithindia.com home and CWS-25 page; bajajfinserv.in Alkara page; Flipkart search pages (10 queries) and review pages (7 listings x 3 sort orders x 3 pages); indiawaterportal.org two question pages; indianstartupnews.com and india.entrepreneur.com articles. Search snippet only: LinkedIn follower count, 1mg and DesiDime listings, 3M price, Bajaj list for ZeroB AS1/AS2, YouTube-title evidence for Kent AMC. Blocked: see section 3a.

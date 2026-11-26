# Playbook: creative quality bar (brand, website, ads)

Owner: Marketing Lead (brand, ads) and Developer (website). Reviewers: the other of the two, then the CEO. Written 2026-11-26 after the founder's review of the Mrudu work ("college project", "website quality very low", "the name had no research").

Every brand, landing-page and ad deliverable clears this bar **before** it reaches the CEO. Work that does not clear it is labelled **DRAFT**, never DONE.

## What "global standard" means here

Global standard means craft, taste and clarity. It does not mean expensive production. A ₹1,999 product from a two-person studio can look as considered as Jolie or Aesop if it gets five things right:

1. **Show the real thing.** The buyer sees the actual product, in a real Bangalore bathroom, photographed well. Drawings, renders and empty placeholder boxes are working files. They never ship, and they never go to the founder labelled as finished work.
2. **Proof is the design.** Our idea is that you can check the result with a test strip. The best brands make their proof the hero: Minimalist puts the active percentage in the product name, and The Whole Truth prints every ingredient on the front of the pack. Our hero is a measured, dated strip reading on borewell water. Until that reading exists, we are not ready for craft work.
3. **One idea, said plainly, in the customer's words.** Each headline traces to something a real buyer said, and it would not work unchanged on a competitor's page.
4. **Restraint.** Use one or two typefaces, a small palette and one memorable element per page. Cut decoration. Aesop's warmth comes from photography and restraint, not colour.
5. **Honest is non-negotiable, and it helps.** Hello Klean's own FAQ says no shower filter removes calcium. Being precise about what we do and what we have measured is a positioning advantage, as long as we have the measurement. CLAUDE.md §7 always applies.

### What we can do well cheaply

| Lever | How | Rough cost (estimate, not quoted) |
|---|---|---|
| Product photography | A recent phone, window daylight, a white or grey sheet, tripod, AI "enhance" off. Shoot 4:5, 1:1 and 9:16. 30 frames per setup, keep the best 3. | ₹0. Optional half-day local product photographer for the hero, which needs founder OK. |
| In-situ photography | The real unit on a real shower arm in a real Bangalore flat (ours, or with the owner's written OK). | ₹0 |
| Proof footage | One continuous take of the strip test, in daylight, with the date and litres logged. | Cost of strips |
| Typography | One distinctive OFL display family plus one text family, or one superfamily. Self-host as WOFF2 and subset. | ₹0 |
| AI-assisted imagery | Allowed **only** for backgrounds, textures and mood. Never for the product, never for a result, never for people presented as customers. Label it where a viewer could take it as real. | ₹0–2k/month tool |
| Video editing | CapCut or similar for burned-in captions and 9:16 safe-zone checks. | ₹0 |
| Packaging | A printed sleeve or sticker plus an insert card with the strip instructions. Shoot it in the unboxing. | ₹2–5k for a small run, needs founder OK |
| Product industrial design | Choose the best-looking OEM housing and colour, and add a branded sleeve or cap. Avoid the generic white marketplace cylinder. | Sample cost |

## How to use the checklists

- Each item is **PASS / FAIL**. If there is no evidence, the item fails. "Looks fine" does not count as evidence.
- **M** marks a must-pass item. A deliverable clears the bar only if **every M item passes and at least 85% of all items pass**.
- Put the evidence for each item (file, screenshot, tally sheet, command output) in the evidence pack. See "How we review" below.
- An item that cannot be met yet (for example, proof that is not measured) stays FAIL and blocks shipping. Do not paper over it with an illustration.

## (a) Brand and naming

| # | Check (pass if...) | Evidence | M |
|---|---|---|---|
| B1 | A wordmark and phonetic search on the IP India public search (tmrsearch.ipindia.gov.in), in class 11 and in any other class we sell in, finds no identical or confusingly similar live mark. A trademark attorney has given a clearance opinion before we spend money on packaging or a domain. | Search printouts with date, attorney note | M |
| B2 | The exact name, or name plus one generic word, is available as a .in or .com domain and as an Instagram handle. | Screenshots with date | M |
| B3 | Spelling test: 10 target buyers hear the name spoken once, and at least 8 of 10 write it the same way we do. | Tally sheet | M |
| B4 | Reading test: 10 target buyers read the written name aloud, and at least 8 of 10 say it the way we intend. | Tally sheet | |
| B5 | Native speakers of Kannada, Hindi, Tamil, Telugu and English confirm the name has no negative, comic or misleading meaning. A misleading meaning includes one that implies a health outcome. | Signed-off notes, one per language | M |
| B6 | At least 3 alternative names were scored on a written rubric (B1–B5, plus memorability and fit with the proof idea) before one was chosen. | Naming sheet | M |
| B7 | The positioning is one sentence that names the buyer, the problem and the proof, and it fails the swap test: it would be false on WaterScience's, Jolie's or Hello Klean's page. | Brand kit line | M |
| B8 | The logo is legible at 16px and in one colour. When 5 people are asked "what is this?", fewer than 2 name a different common object (for example a traffic light or a battery). | Renders at 16/32/96px, tally | |
| B9 | The identity uses at most 2 type families, with licences recorded. | Brand kit | |
| B10 | The palette has at most 6 colours, with a WCAG contrast table, and every text use is AA or better. | Brand kit | |
| B11 | At least 3 of our own photos of the real unit exist: hero on a plain backdrop, fitted on a shower arm, and in a hand for scale. Each is at least 2000px on the long side, in daylight, unretouched apart from crop and exposure. | Files in `marketing/evidence/` | M |
| B12 | The product looks like ours. A Google Lens reverse-image search of our hero photo does not return the identical unbranded unit on Amazon, Alibaba or IndiaMART as the top match, or the unit carries a visible branded element (sleeve, cap, colour). | Lens screenshot | M |
| B13 | A packaging or unboxing concept exists (box or sleeve, plus an insert card with the strip instructions) and has been photographed. | Photo | |
| B14 | The voice guide has 3 to 5 do/don't pairs, and every public line passes the AI-tells check in `.claude/skills/copywriting/SKILL.md` (no contrast reveals, negation lists, colon reveals, stock phrases, or em dashes in short copy). | Brand kit, check log | |
| B15 | One review sheet shows the system applied to at least 3 real touchpoints (page hero, one ad, the box), and they look like one brand. | Single image or PDF | M |

## (b) Website / landing page

Measure at **390×844** (mobile) and **1366×768** (desktop) unless a check says otherwise.

| # | Check (pass if...) | Evidence | M |
|---|---|---|---|
| W1 | The hero headline is 8 words or fewer and states the buyer's outcome or the proof, not the mechanism. | Screenshot, word count | M |
| W2 | A **real photo or video of the real unit** is visible above the fold on mobile. | 390×844 screenshot | M |
| W3 | The price, inclusive of all taxes, and the primary CTA are both above the fold on mobile. | 390×844 screenshot | M |
| W4 | There is one primary CTA. Its label names the action and the price (for example "Pre-order for ₹1,999"), and it is used consistently on the page. | Screenshot | |
| W5 | Hero supporting copy is 25 words or fewer. | Word count | |
| W6 | Proof sits above the fold or in the first scroll: a measured, dated, sourced result, or our own unedited demo footage. Illustrations never stand in for proof. | Screenshot, claims register | M |
| W7 | 5-second test: 5 people who have not seen the page look at the mobile hero for 5 seconds. At least 4 of 5 can say what the product is, who it is for and roughly what it costs. | Tally sheet | M |
| W8 | The shipped or review build shows **zero** visible placeholders: `grep -oE '\[[A-Z][A-Z_ ]{3,}' index.html policies.html` returns nothing outside code comments and config, and the screenshots contain no "[...]" text. | Command output | M |
| W9 | The page uses at most 2 type families, both loaded (or a deliberate system stack written down), with a stated modular scale. Body text is at least 16px and lines are at most 75 characters. | CSS, screenshot | |
| W10 | At most 1 of the generic-template tells listed in `.claude/skills/frontend-design/SKILL.md` appears: identical bordered or shadowed cards everywhere, an all-caps eyebrow above each heading, one accented word in the headline, gradient washes, cream plus terracotta, middle-dot meta strings, "→" on buttons. | Reviewer count | |
| W11 | No stock-photo clichés: no model in a towel, splash shot, spa stones, lab coat, or generic luxury bathroom. Every product image is our own. | Image list | M |
| W12 | The page carries at least 3 of our own images or videos: the product, the fitting, and the proof. | Image list | |
| W13 | Lighthouse mobile (default throttling) scores **Performance ≥ 90**, with **LCP ≤ 2.5 s**, **CLS ≤ 0.1** and **TBT ≤ 200 ms** (the lab proxy for INP). These follow web.dev's "good" thresholds. | Lighthouse JSON/HTML | M |
| W14 | First-load page weight is 1 MB or less. The hero image is 200 KB or less, in AVIF or WebP, with width and height set. | Network log | |
| W15 | Accessibility: Lighthouse a11y ≥ 95, axe shows 0 serious or critical issues, and focus is visible. | Report | M |
| W16 | Message match: each live ad angle lands on a hero whose headline reuses that ad's hook words, either as a separate URL or as a UTM-driven variant. | URL list and screenshots | |
| W17 | The FAQ answers fit, cartridge cost and life, refund, delivery area, and "how is this different from a chlorine filter?". | Screenshot | |
| W18 | Checkout asks for at most 3 fields before payment, the terms are visible next to the pay button, and the Razorpay test-mode checkout opens on mobile. | Playwright run | M |
| W19 | Legal: seller name and address, grievance officer, ship date and refund timeline are present, and all prices include taxes (E-Commerce Rules 2020, CLAUDE.md §7). | Screenshot | M |
| W20 | Blind tier test: hero screenshots of ours, 2 benchmarks and 2 ordinary marketplace listings, logos blurred and order shuffled, go to 3 reviewers (the founder may be one). At least 2 of the 3 rank ours in the top 3 of 5. | Sheet with ranks | M |
| W21 | Every claim on the page is listed in a claims register with its evidence file. Any claim without evidence is removed. | `claims.md` | M |

## (c) Ad creatives

| # | Check (pass if...) | Evidence | M |
|---|---|---|---|
| A1 | The hook is specified as all three components (visual action in 0–2 s, spoken line, caption of 7 words or fewer), and the caption does not repeat the spoken line. For statics: visual plus headline, and the headline does not caption the image. | Hook matrix | M |
| A2 | The creative uses **real footage or photos of the real product**. No mockup, render or illustration runs as an ad. | Source files | M |
| A3 | Burned-in captions make the ad fully understandable with sound off. | Muted playback check | |
| A4 | It is built natively per placement: 4:5 for Feed and 9:16 for Reels and Stories (not centre-cropped), with no key text inside Meta's Reels safe-zone overlay. | Overlay screenshot | M |
| A5 | The product is on screen by second 3, or by second 5 for problem-first hooks. | Timestamp | |
| A6 | Format range: the test set covers at least 3 distinct formats, for example founder-to-camera, unedited demo, static proof card, hands-only how-to, or a street or RWA demo. It is not one template with swapped headlines. | Set overview | M |
| A7 | Each creative has a hypothesis that a result can prove wrong, naming the metric, the comparison and the expected direction. | Creative sheet | |
| A8 | Each hook traces to a verbatim customer quote with its source in `research.md`, or it is flagged HYPOTHESIS. At least half the set is quote-sourced. | `research.md` | M |
| A9 | The key point of the primary text falls within the first 125 characters. There are no AI tells and no em dashes. | Text | |
| A10 | The end card shows the product, the price inclusive of taxes and the pre-order terms, for 3 seconds or less. | Frame grab | |
| A11 | Compliance C1–C8 all pass (personal-attribute phrasing, health, before/after body, measurable only, fake proof, fake urgency, price incl. taxes, substantiation). | Compliance table | M |
| A12 | Feed recall test: the ad goes into a mock feed among 9 real ads and is shown to 5 people, and at least 3 recall our product unprompted afterwards. | Tally | |
| A13 | Craft floor: the subject is in focus, exposure is correct, the horizon is level, there are no watermarks or other brands' logos, and the export is at least 1080px wide. | Frame grabs | M |
| A14 | At least one variant shows a real person (hands or face, with a signed consent release) in a real Bangalore home. Meta and ASCI rules ban before/after body imagery and health claims. They do not ban people. | Release on file | |

## Benchmarks: what to learn

**Source status:** on 2026-11-26 this session had no direct network access to the brand sites. The notes below come from web-search extracts of the listed pages and third-party coverage, so **no page has yet been opened by a reviewer**. Before a benchmark is used in a side-by-side (W20) or quoted in a brief, the reviewer opens the URL and writes "visited YYYY-MM-DD" in the last column. Do not copy assets or text from any of these brands.

| Brand | URL(s) | What makes it world-class | What we take | Avoid | Visited |
|---|---|---|---|---|---|
| Jolie (US shower filter) | https://jolieskinco.com/products/the-replacement-filter · https://jolieskinco.com/pages/faq · review: https://www.nbcnews.com/select/shopping/jolie-filtered-showerhead-review-rcna177595 | The showerhead is a designed object in five colours. Free shipping and 60-day returns sit by the CTA. The filter subscription (every 90 days, "Subscribe & Save") makes recurring cost explicit. Many angle-specific landing pages (/pages/curly-hair, /pages/problem-focused, /pages/jolie-water-advertorial) message-match each ad. | The product as an object, recurring cost shown upfront, one landing variant per ad angle (W16) | Health-outcome pages (/pages/acne, /pages/jolie-showerhead-for-eczema, /pages/hair-growth) and "500,000+ happy customers" style proof: illegal or unavailable for us | No |
| Hello Klean (UK/AU shower filter) | https://www.helloklean.com/pages/faqs · https://helloklean.com/pages/wash-and-learn | The FAQ says plainly that no shower filter removes calcium. It is stocked by premium beauty retailers (https://www.cultbeauty.com/hello-klean). | Category honesty as a trust signal. **Also a warning:** experts and competitors doubt shower-sized softening, so our proof must be measured over realistic volume. | Implying hair or skin outcomes | No |
| WaterScience CLEO (Bangalore, direct local competitor) | https://waterscience.in/products/multi-flow-shower-filter-cleo-sfm-419-fits-standard-shower-arms-with-free-self-installation-kit · https://yourstory.com/herstory/2022/05/bengaluru-startup-waterscience-non-drinking-water-tap-filters | It sells "shower filter for hard water" D2C and on marketplaces, in the same city and to the same buyer. Its page says it does not reduce TDS. | It is the page our buyer will compare us with. We must beat it on proof (a measured strip result) and on photography. | Fuzzy "for hard water" claims | No |
| Ruhe Cleanza (India) | https://ruheindia.com/products/cleanza-tap-and-shower-filter-for-hard-water | Scale proof in the header ("Trusted by 10 Lakh+ customers"). | Shows the proof level Indian buyers see. We answer with measured proof, never invented counts. | Unverifiable counts | No |
| Minimalist (India skincare) | https://www.hul.co.in/brands/beauty-wellbeing/minimalist/ · analysis: https://www.markhub24.com/post/minimalist-and-the-rise-of-ingredient-literate-skincare-consumers | The proof is in the name and on the label: active ingredient and percentage. The design is clinical and quiet. | Put our number (ppm before and after, litres tested) where they put the percentage, in the hero and on the pack. | n/a | No |
| The Whole Truth (India food) | https://confetti.design/audit/the-whole-truth · scrutiny: https://india.entrepreneur.com/business-news/when-trust-faces-scrutiny-the-whole-truths-clean-labels-put-to-the-test | All ingredients on the front of the pack, and a system that feels hand-annotated. The brand is the disclosure. | The strip reading as our front-of-pack truth. The hand-annotated feel suits a demo-led brand. | Transparency claims get audited by press, so every number needs a source file | No |
| Aesop (global) | https://work.co/clients/aesop · https://wallpaper.com/design/global-roaming-the-secret-behind-aesop-success | Restraint. The site layout follows the packaging, photography carries the warmth, and the type is literate and unglamorous. | One family used with discipline. Let photography do the emotional work. | Luxury mood that a ₹1,999 Bangalore buyer may not trust | No |
| Glossier (global) | https://www.adweek.com/brand-marketing/glossiers-biggest-campaign-ever-is-all-about-real-people/ | Real people and real bathrooms as the visual identity. | Real Bangalore bathrooms and real hands (A14), not stock luxury bathrooms | Implied skin results | No |
| Oura (global hardware plus subscription) | https://ouraring.com/store · https://support.ouraring.com/hc/en-us/articles/4409086524819 | Hardware price plus recurring membership cost disclosed, and a support page saying exactly what you lose without it. | State cartridge price and tested life beside the unit price | The vague hero line ("More personal, more intuitive, more you") fails our W1 | No |
| Bombay Shaving Company (India) | https://www.storyboard18.com/quantum-brief/bombay-shaving-company-refreshes-logo-as-it-eyes-bigger-share-of-offline-market-11634.htm · ad analysis (vendor estimate): https://hawky.ai/blog/decoding-bombay-shaving-company | Its refresh compacted a long name (7 syllables) into a bold, simple identity for shelf and offline use. Third-party analysis says its Meta mix is mostly video. | Name length and pronunciation drive identity cost (B3, B4). Lead the Meta test with video. | n/a | No |
| Reference standards | https://web.dev/articles/defining-core-web-vitals-thresholds · https://creators.facebook.com/blog/10-video-best-practices · https://tmrsearch.ipindia.gov.in/tmrpublicsearch/ | Core Web Vitals thresholds: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1. Meta's sound-off and caption guidance. The official Indian trademark search. | W13, A3, B1 | n/a | No |

## How we review

1. **Author self-check.** The author fills in the checklist for their section (B, W or A) with PASS/FAIL and an evidence link for every item. Anything that fails stays labelled DRAFT.
2. **Evidence pack**, in `ventures/<venture>/<team>/review/YYYY-MM-DD/`:
   - Playwright screenshots at 390×844 (above the fold and full page) and at 1366×768 (above the fold and full page).
   - The **side-by-side sheet**: our mobile hero next to two benchmark heroes at the same viewport (benchmarks marked "visited"), plus the W20 blind-rank tally.
   - Lighthouse mobile report, axe output, and the placeholder grep output (W8).
   - Claims register plus the compliance table C1–C8 (CLAUDE.md §7, Meta ad policy, ASCI).
   - Tally sheets for any people tests (B3, B4, B8, W7, A12). Record first names only, with consent to note answers, and no contact details.
   - A self-critique of 3 lines: the weakest element, and what we would fix with one more day.
3. **Cross-review.** The Marketing Lead reviews the Developer's page and the Developer reviews the Marketing Lead's ads and brand work. The reviewer re-runs W8 and W13 and spot-checks 3 random evidence links. If a reviewer cannot reproduce an item, it fails.
4. **CEO review.** The CEO checks that every M item passes and at least 85% of items pass overall, reads the side-by-side, and either sends the work back with numbered fixes or forwards it to the founder.
5. **Founder** sees only work that has cleared the bar, or work clearly labelled DRAFT with the failing items listed. The founder is never shown placeholder work presented as finished.
6. **Compliance outranks craft.** If a creative choice conflicts with CLAUDE.md §7, the creative choice loses.

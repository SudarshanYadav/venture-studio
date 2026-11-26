# Mrudu: quality audit against `playbooks/quality-bar.md`

Auditor: Marketing Lead, 2026-11-26. Much of the audited work is my own (brand kit, creatives, ad mockups), so I have scored it strictly. No evidence counts as FAIL.

**Verdict: does not clear the bar.** Landing page 6 of 21 items pass (29%), 10 M items fail. Brand 4 of 15 pass (27%), 8 M items fail. Ads 6 of 14 pass (43%), 6 M items fail. The 85% overall threshold and the all-M rule both fail on every section.

What is good and should be kept:
- The compliance discipline: honest pre-order terms, no invented proof, C1–C8 checks.
- A lean page of 26 KB with no images and no webfonts.
- The core idea: "a shower softener you can test with a strip" is distinctive and true to the product.

The problem is not the idea or the honesty. We showed the founder wireframe-grade work, with drawings where the product should be and placeholders where proof should be, and labelled it DONE.

## Top failures, ranked by impact

1. **There is no real product anywhere: page, ads or brand.** (W2, W12, A2, B11, B12, B13, all M)
   - `landing/index.html` L136–160: the hero visual is a hand-drawn SVG of two strips, captioned "Illustration ... not a measured result" (L159). The page has 0 `<img>` tags.
   - `marketing/brand/ad-mockups.html` L69–88, L106–124, L142–162 and L180–205: every creative is a drawing with dashed empty boxes (`stroke-dasharray`, L76, L80, L151, L156) and an orange "Placeholder: our photo" tag.
   - `brand/product-render.svg`: a generic cylinder.
   - Root cause: we have no physical unit. No amount of design craft fixes this. It is the single biggest reason the work reads as a college project.
2. **The proof is missing, and the page is built around proof.** (W6 M, A8 M)
   - The promise is "check it yourself", but every result is `[TO BE MEASURED]`. That appears 3 times in `index.html` (L159, L186, L265), plus `[CARTRIDGE LIFE — TO BE MEASURED]` at L194 and L268.
   - Competitors and category experts say shower filters do not remove calcium (Hello Klean FAQ, see the benchmarks). So an unproven softening claim is a weakness, not a neutral gap.
   - Same root cause as failure 1, and the same blocker as the capacity decision.
3. **The name "Mrudu" has no research behind it.** (B1, B2, B3, B5, B6, all M)
   - `brand/brand-kit.md` L3 says only that it is a placeholder.
   - Not done: an IP India search, a domain or handle check, alternatives, a spelling test, or a native-speaker meaning check.
   - Specific risks, unverified: the Sanskrit/Kannada root (soft) has several common spellings in India (Mridu, Mrudu, Mridhu), which threatens spelling recall (B3) and search. "Mridu" is also a common given name. The "Mr" opening cluster may be read as "Mister" by non-native readers (B4).
   - We built a wordmark, icon and mockups on an untested name.
4. **Drafts were presented as finished.** (W8 M, W9, B15 M, W10)
   - `index.html` has 27 bracket-placeholder matches (`grep -oE '\[[A-Z][A-Z_ ]{3,}'`), 25 of them visible on the page and 2 in script config, and `policies.html` has 12 more lines with them. `[SHIP DATE — founder to set]` appears in the hero itself (L131) and is visible in `screenshots/mobile-390-1-hero-final.jpg` and `desktop-1366-1-hero-final.jpg`.
   - The brand kit was never applied. The page still uses `system-ui` (L19), not Bricolage/Atkinson (`brand-kit.md` L35–38; `handoff-to-developer.md` not executed).
   - Template tells (W10): there are 2. The page uses the same bordered rounded panel everywhere (`.strips` L52, `.panel` L61, `.steps li` L66) and a middle-dot meta string (L279). The failure limit is 2 or more.
5. **The ads are one template with no people and no customer language.** (A6 M, A8 M, A14, A1 M, A4 M)
   - Format range (A6): all four mockups use one layout: headline at the top, a drawing in the middle, and an identical ink price band (`ad-mockups.html` L90, L126, L164, L207, L227).
   - Customer research (A8): `marketing/` has **no `research.md`**, so no hook traces to a real customer quote. The angles came from our own reasoning.
   - People (A14): `creatives.md` L5 bans "people's skin or hair" outright. That over-corrects. The rules ban before/after body imagery and health claims, not hands or faces. The result is a set with no human in it.
   - Hooks (A1): hooks are written as captions only, with no spoken line.
   - Placement (A4): there is no Reels safe-zone check.

Further failures, lower impact:

6. No message-matched landing variants per angle (W16). There is one hero for four angles.
7. Not done: a Lighthouse or axe report (W13, W15). The page is probably fast, but this is unverified. Nor were the 5-second test (W7) or the blind tier test (W20) run.
8. Hero support copy is 39 words (L127, limit 25). It leads with competitors ("Many shower filters are made to remove chlorine") and with chemistry before the buyer's problem (W5).
9. Seller identity and grievance officer are placeholders (W19, L278). This is a founder input, but it blocks shipping.
10. At 16px the icon (`brand/icon.svg`: a magenta square over a green square in a dark rounded rectangle) can read as a traffic light (B8). This is my own observation from the rendered mockup header and has not been tested with people.

## Scorecard

### Landing page: `ventures/mrudu-shower-softener/landing/index.html` and `screenshots/`

| # | Result | Where / why |
|---|---|---|
| W1 M | PASS | L126 "Hard borewell water, softened at your shower head." 8 words. Borderline: it describes where the product works more than the buyer's outcome. |
| W2 M | FAIL | No product image. L136–160 is an illustration. |
| W3 M | PASS | `mobile-390-1-hero-final.jpg`: price and CTA are above the fold. |
| W4 | PASS | "Pre-order for ₹1,999" (L129, L247), used consistently. |
| W5 | FAIL | Lede is 39 words (L127). |
| W6 M | FAIL | No measured proof (L159, L186, L265). |
| W7 M | FAIL | Not run. |
| W8 M | FAIL | 25 visible placeholders in `index.html`, including the hero (L131). |
| W9 | FAIL | System fonts (L19); brand type not applied; no scale written down. |
| W10 | FAIL | 2 tells (repeated bordered panels; middle-dot string at L279). |
| W11 M | PASS | No stock imagery. |
| W12 | FAIL | 0 own images. |
| W13 M | FAIL | No Lighthouse report in `landing/README.md` or `screenshots/`. Likely passes (26 KB, no images), but unverified. |
| W14 | PASS | 26 KB, inline CSS, no images (measured with `wc -c`). |
| W15 M | FAIL | No axe or Lighthouse a11y report. Contrast was computed in the brand kit only. |
| W16 | FAIL | One hero for 4 angles. |
| W17 | PASS | FAQ L265–272 covers fit, cartridge, chlorine vs hardness, refund and delivery. Cartridge life is still unknown. |
| W18 M | FAIL | 3 fields and terms by the button pass (L232–249), but Razorpay test mode was never opened. Per ORG.md the server was never run. |
| W19 M | FAIL | Seller and grievance placeholders (L278); ship date placeholder. |
| W20 M | FAIL | Not run. |
| W21 M | FAIL | No standalone claims register in `landing/`. Claims are only listed in the marketing compliance table. |

### Brand: `marketing/brand/brand-kit.md`, `wordmark.svg`, `icon.svg`, `product-render.svg`

| # | Result | Where / why |
|---|---|---|
| B1 M | FAIL | No trademark search (brand-kit L3; BRIEF.md). |
| B2 M | FAIL | Not checked. |
| B3 M | FAIL | Not run. Spelling-variant risk noted above. |
| B4 | FAIL | Not run. |
| B5 M | FAIL | Not run. |
| B6 M | FAIL | No alternatives were considered. |
| B7 M | PASS | L7 positioning names the buyer, the problem and the strip proof. It would be false on WaterScience's or Jolie's page. |
| B8 | FAIL | Not tested. Traffic-light risk (`icon.svg` L4–7). |
| B9 | PASS | 2 OFL families with licences (L35–38). |
| B10 | PASS | Contrast table (L22–33). |
| B11 M | FAIL | No photos (`images.md`: "Nothing has been downloaded", and the shot list has not been shot). |
| B12 M | FAIL | No unit. The render is a generic cylinder. |
| B13 | FAIL | No packaging concept. |
| B14 | PASS | Tone table (L12–20). Sentence case, no exclamation marks. |
| B15 M | FAIL | Applied only to placeholder mockups. The landing page is unchanged. |

### Ads: `marketing/creatives.md`, `marketing/brand/ad-mockups.html`

| # | Result | Where / why |
|---|---|---|
| A1 M | FAIL | The visual and caption are specified (creatives L21, L41) but there is no spoken-line column and no hook matrix. |
| A2 M | FAIL | Every visual is a placeholder drawing (mockups L57 says "These are not ads"). |
| A3 | PASS | Burned-in captions required (creatives L5). |
| A4 M | FAIL | Both sizes are specified (L5), but there is no safe-zone check. |
| A5 | PASS | Planned: A and C show the product or strips at 0–2 s (L21, L41). |
| A6 M | FAIL | One template. Formats are 3 demos and 1 static; no founder, no person, no RWA demo. |
| A7 | PASS | Each angle names a metric and comparison (L14, L24, L34, L44). |
| A8 M | FAIL | No `research.md`; 0 hooks are quote-sourced. |
| A9 | PASS | Key point in the first 125 characters; no em dashes in primary text. |
| A10 | PASS | End card specified (L21). |
| A11 M | PASS | C1–C8 table (brand-kit L50–64; test-plan §9). |
| A12 | FAIL | Not run. |
| A13 M | FAIL | No footage exists to check. |
| A14 | FAIL | People banned outright (L5). |

## What it takes to clear the bar (in order)

1. **Get 2–3 sample units and strips.** One purchase unblocks the capacity bench test, the proof footage and the product photography: W2, W6, W12, A2, A13, B11 and B12. Founder OK needed, about ₹3–5k as already proposed.
2. **Name research** (B1–B6), done before any more brand work. Keep the strip-mark system, which survives a rename.
3. **Customer research** (`research.md`): Reddit r/bangalore, Google and Amazon reviews of WaterScience and Ruhe, and RWA groups (read only). Rewrite hooks from real quotes.
4. **Rebuild the page around the real photo and the measured strip reading.** Apply the brand type, remove all placeholders from the review build, run Lighthouse, axe, the 5-second test and the blind tier test.
5. **Shoot 3 formats** (founder or hands-to-camera, unedited strip demo, static proof card) with consent releases for anyone on camera.

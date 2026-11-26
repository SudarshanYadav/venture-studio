# Mrudu: bench-test spec (cartridge capacity)
Date: 2026-11-26 | Researcher: Market Researcher | Status: **spec only. Buying anything needs founder OK** (CLAUDE.md §8). Feeds `decisions/2026-11-25-mrudu-cartridge-capacity-blocker.md`.

## 1. The question, and what desk research already says
**Question:** how many litres of real Bengaluru borewell water, at real shower flow, does a shower-arm resin cartridge bring below a stated hardness, before it stops?

**Desk answer (Medium-High confidence on physics, Low on the cartridge's resin volume):** about **0.2 to 3 showers**, and probably not even one shower fully softened at full flow. Working in `research/calc/stage2_calc.py`:
- Fresh sodium-form softening resin holds at most **1.9 eq/L = 95 g CaCO3 per litre of resin** (Purolite C100E datasheet, opened). A retailer's working figure is 32,000 grains/ft³ = **73 g/L** (Pure Water Products, opened).
- A shower-arm cartridge holds roughly **0.1 to 0.35 L** of media (assumption: no supplier spec seen; the test measures it).
- At 200 / 350 / 600 mg/L hardness, that is **12 to 166 L** of water before exhaustion; a shower uses about 50 to 80 L (assumption).
- **Flow is the bigger problem.** Softening resin is rated for about **8 to 40 bed volumes per hour** (Purolite C100 literature; Resinex KW-8; Lewatit S1567: datasheets seen as search snippets, ranges agree). A 0.2 L bed at 6 to 10 L/min is **1,800 to 3,000 BV/h, 45 to 75 times the maximum**, so hard water leaks through from the first minutes. Full-flow softening needs about **12 L of resin** at 8 L/min.
- Independent cross-check: a 2.5 x 9.75 inch softening cartridge (about 0.6 L of resin, three times a shower cartridge) is rated for **57 L at 684 mg/L or 170 L at 256 mg/L** (Pure Water Products table, opened), and that maker sells it for low-flow use, not showers.

So the test is no longer "will it last 2 to 3 months?". It is **"does it soften anything at shower flow, and for how many litres?"** If the answer is "under 200 L", the ₹1,999 + ₹599 shower-arm product is dead and the test becomes evidence for the pivot (a bathroom-scale unit) and for honest content.

## 2. What to buy (needs founder OK; total about ₹3.5k to 6k)
| Item | Why | Indicative cost | Source of price |
|---|---|---|---|
| 1 resin shower softener cartridge/unit that states "ion exchange resin" on the pack (import listing, e.g. Amazon.ae "shower softener" or an Indian seller if found) | The product type we would sell | ₹1,500 to 3,000 | Unknown; Amazon.ae premium tier AED 229 is too dear; a generic resin cartridge may be cheaper. **Not found in India in this research** |
| 1 WaterScience CLEO borewell/tanker cartridge unit (SFU-423 HHC, ₹1,390 to 1,495 on Flipkart) | Control: the market leader, a conditioner | ₹1,390 to 1,495 | Flipkart listing, opened |
| 250 to 500 g loose softening resin (Na form) | Lets us test resin volume directly, independent of cartridge design | ₹100 to 330 per L | IndiaMART listings, **snippet only** |
| EDTA total-hardness titration kit (drop count, 1 drop = 10 or 17.1 mg/L) | Quantitative, about ±10 to 20 mg/L | ₹400 to 900 | Not sourced; check before buying |
| Hardness test strips (0 to 425+ mg/L bands), 50 count | The proof format we would use in ads; cross-check against titration | ₹300 to 700 | Not sourced |
| 10 L bucket with litre marks, stopwatch (phone), measuring jug | Flow and volume | ₹200 to 400 | |
| Optional: lab test of one inlet sample (NABL lab) | Anchors the kit readings | ₹500 to 1,500 | Not sourced; DMG Bengaluru also tests water (IWP 2011 page) |

## 3. Method
**Setup**
1. One bathroom on borewell or tanker water in Bengaluru. Record locality and source. Test inlet hardness 3 times on different days (titration + strip). Aim for 250 to 500 mg/L; record if outside.
2. Measure the shower's flow with the bucket: litres in 60 s at full tap, and at half tap. Repeat 3 times.
3. Weigh/measure the media: after the test, open the spent cartridge, separate the resin beads (amber, 0.3 to 1.2 mm), and measure their volume in a jug. This settles the 0.1 to 0.35 L assumption.

**Runs (each unit, fresh cartridge)**
| Run | Flow | Sampling points (cumulative litres) | Measure at each point |
|---|---|---|---|
| A | Full flow (as a user would) | 2, 5, 10, 20, 40, 60, 80, 120, 160, 200, 300, 500 | Titration on the outlet sample taken in the last 10 s; strip on the same sample; water temperature |
| B (only if A shows any reduction) | Half flow | same | same |
| C (loose resin, optional) | Gravity column, 0.25 L resin in a 50 mm pipe at 1 L/min, then 5 L/min | same | Shows the flow effect directly |
Stop a run when the outlet is within 10% of the inlet at two consecutive points.

**Controls**
- Inlet sample at every 5th point (inlet hardness drifts).
- The CLEO control run uses the same points: expect no hardness change (their own page says it "conditions" and does not change TDS). Record anyway; it is the content for honest comparison.
- Blind the strip reading: one person dips, another reads the colour without knowing the litre count.

**Records**
- One row per sample: unit, run, litres, flow, inlet mg/L, outlet mg/L (titration), strip band, photo of strip against the chart under daylight, time, temperature.
- Video of the full-flow run from the start, with the litre count on screen (the only honest footage we could use).

## 4. Pass / fail (set before testing)
| Result | Meaning | Decision |
|---|---|---|
| Outlet at least 50% below inlet for at least **1,500 L** at full flow (about 20 to 30 showers; a month for one person) | A shower-arm product could carry an honest, specific claim | Reopen the Mrudu shower product; size cartridge price to the measured life |
| Some reduction but under 1,500 L, or only at half flow | Claim would need "first X litres" or "at low flow"; not a credible product | **Kill the shower-arm form.** Use data for the pivot screen |
| No reduction beyond the first 20 to 50 L | Physics confirmed | **Kill the shower-arm form** |
The 1,500 L bar is my proposal (a cartridge that lasts under a month at one shower a day cannot be priced or refilled honestly); founder to confirm.

## 5. Claims we could make from this test (and only these)
- "Outlet hardness at full flow: X mg/L at Y litres, measured on Bengaluru borewell water of Z mg/L, on [date]", with the method published.
- Nothing about hair, skin, hair fall, eczema or dandruff (CLAUDE.md §7; the UK ASA upheld complaints against a real whole-house softener's "glossier hair" and "softer skin" claims, Harvey Water Softeners, A19-565203, opened).
- No strip demo in ads that shows only the first litres. That would be misleading under ASCI Chapter I ("capable of substantiation"; opened) and the CCPA misleading-advertisement guidelines (2022; text not opened in this session).

## 6. Who does it, how long
About half a day of hands-on work plus one week elapsed for buying. The founder or anyone in Bengaluru with a borewell bathroom. No supplier contact needed for the control and loose-resin runs; the resin cartridge may need an import order (founder OK).

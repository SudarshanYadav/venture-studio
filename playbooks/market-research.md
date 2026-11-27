# Playbook: market research (India only) before any build or spend

Owner: Market Researcher (`.claude/agents/market-researcher.md`). Inputs: Finance Analyst (max CAC and margin check), Marketing Lead (customer language, channels). CEO reviews each stage; the founder decides go / no-go. Rule adopted 2026-11-26 ([decision](../decisions/2026-11-26-market-research-and-model-budget.md)). **Scope changed 2026-11-26: India only. The founder dropped the UAE from all future work; do not research or compare it.** Every screen and deep dive must contain the four mandatory sections in section 1a.

## 1. When it runs
- Every **new venture or new product** gets market research **before** a landing page, ad plan, supplier order or any spend. No exceptions for "small" ideas; the screen is cheap.
- It comes **before** `playbooks/smoke-test.md` step 1. The research proposes the country, the price band, the claim risks and the test design; the smoke test then proves CAC.
- Existing ventures (Mrudu, Lavan) are covered only if the founder asks (open question in the decision log).
- Research is not a substitute for the smoke test. It cannot prove demand; it can kill ideas cheaply and narrow what the test must prove.

### 1a. Four mandatory sections (every screen and every deep dive)
The founder reviewed the first Mrudu research and said it did not clearly answer four questions. Each report must now answer them under these exact headings, each with sourced numbers:
1. **Current players**: at least 15 named players where the category has that many (D2C, big brands, marketplace white-labels, B2B), by sub-category, with mechanism (what it actually does vs what it claims), where sold, marketplace rating counts, and one checked **Link** per product (brand page, otherwise marketplace listing).
2. **Price points**: MRP and selling price (tax-incl.), consumable or refill cost, 12-month cost to the buyer, and a price ladder across sub-categories showing where the gaps are.
3. **Customer problems and feedback**: verbatim quotes with URLs (screen: at least 15; deep dive: at least 40), grouped into themes with counts. Keep apart (a) the problem buyers are trying to solve and (b) complaints about current products, plus unmet needs and price objections. Say which sources were blocked.
4. **Marketing channels**: per player, from evidence, tagged **observed** or **inferred**: Meta Ad Library (active ads and hooks, India), Instagram/YouTube presence and counts, creator collaborations, Google search ads, SEO/blog content, marketplaces, offline/dealer, offers and discounts. Then a channel map and the white space. If the Ad Library or a platform cannot be read, say so and do not describe ads that were not seen.

## 2. Two-step gate

| | Stage 1: Screen | Stage 2: Deep dive |
|---|---|---|
| Purpose | Kill bad ideas cheaply, pick country, list what Stage 2 must prove | Produce the go / no-go the founder can sign |
| Effort | About 1 hour of agent work. About 15 searches (standard mode), at most about 15 page fetches (the four mandatory sections need review and listing pages), 2 pages out plus an appendix of quotes | Up to about 4 hours. Extended search only for a question a decision depends on |
| Output | `ventures/<venture>/research/screen.md` | `ventures/<venture>/research/REPORT.md` (template, section 4) |
| Runs when | Always | Only if the screen passes **and** the CEO confirms (founder OK if it needs paid data) |
| Ends with | PASS / KILL / PARK, country lean, 3 open questions | GO / GO-NARROW / NO-GO, country first, launch plan |

### Stage 1 screen: contents (all on 2 pages)
1. Market definition in one sentence (country, buyer, use case, price band, what is out of scope).
2. Rough SOM range for India from **one** method, labelled Low confidence.
3. **Current players, price points, customer problems, marketing channels** (section 1a): at screen depth, the top 5 to 8 players with shelf price and pack, a price ladder, at least 15 verbatim quotes grouped by theme, and a one-line channel read per player (observed or inferred). Status quo alternative.
4. One-line regulatory flag: blocked / needs licence (time, cost) / free to sell.
5. Gross margin sanity check: shelf price (tax-incl.) minus tax, landed cost estimate, fees. Is the implied max CAC above what Meta CPCs in India make plausible?
6. Kill-criteria table (section 5) filled in with PASS / FAIL / UNKNOWN.
7. Verdict: **PASS** (go to Stage 2), **KILL**, or **PARK** (only unknown facts a 1-hour search cannot settle; name the cheapest way to learn them). Two or more must-pass failures = KILL.

### Stage 2 deep dive
Fill the full template. Answer only what the Stage 1 open questions and the kill criteria need. Stop researching a section once it can no longer change the verdict.

## 3. Evidence rules
- Every number: source URL, date, **confidence** (High: two independent sources agree or first-party data; Medium: one credible source or credible partial evidence; Low: inference or thin support; Unknown: missing, becomes a validation task).
- **Ranges**, never single precise figures. Assumptions listed apart from observed facts.
- At least **two sizing methods** (bottom-up, search-led, competitor-led, channel-led; see `.claude/skills/market-sizing/`). More than 3x apart means an assumption is broken: find it first.
- Observed vs inferred vs implication kept apart (see `.claude/skills/competitor-profiling/`). "Not observed" is not "absent".
- Never fill an unknown with an invented number. Mark "page blocked" or "snippet only" where true.
- Prefer, in order: first-party data, observed market behaviour (prices, listings, review counts, ads), search and demand proxies, government or platform data, third-party reports, expert opinion; treat uncited market-size claims and AI summaries as weak.

## 4. Report template: one file, `ventures/<venture>/research/REPORT.md`

Every venture's research is **one report** the founder can read end to end, with exactly these 15 sections in this order (the Mrudu report is the worked example). Standard companion files, and only these: `customer-voice.md` (all verbatim quotes with URLs, segment tags, theme counts) and `sources.md` (ledger). Also allowed: `calc/` (scripts and outputs), `raw/<slug>/<YYYY-MM-DD>/` (captures, reviews with names removed), `bench-test-spec.md` if a physical test is proposed, and `archive/` (superseded drafts, each headed "Superseded by REPORT.md (date)"). Update REPORT.md in place; do not create a second report. Stage 1 still produces `screen.md` (2 pages) and may fold into REPORT.md when a deep dive is approved. Keep it tight: no repeated content between sections; link, do not copy.

```markdown
# <Venture>: market research report (India)
Date | Researcher | Stage | Currency and rate | Evidence tags (O observed / S snippet / I inferred) and confidence (H/M/L/Unknown)

## 1. Verdict and the decisions the founder needs to make
GO / GO-NARROW / NO-GO / PARK, confidence. Deciding number. The one assumption that would change it, and the cheapest test. Decision table: decision, options, cost, recommendation.
## 2. Key numbers
One table: number, value (range), source, confidence.
## 3. The problem and the market
Market definition (one sentence, out of scope). The problem in measurable terms (e.g. hardness data). Target areas or segments by evidence. TAM / SAM / SOM table, two or more methods compared (more than 3x apart: explain), arithmetic shown, swing factor, attractiveness score /50.
## 4. Current players
ONE table, at least 15 named players where the category has that many: player, category (brand / marketplace private label / local / B2B), mechanism (does it do what it claims?), price (tax-incl.), 12-month cost, where sold, marketplace rating count, claim and proof offered, **Link** (one checked link per product: the brand page, otherwise the marketplace listing; open it and record the date checked). Status quo and substitutes. Whitespace, strengths we cannot match, copy threat, defensibility.
## 5. Price points
Price ladder across sub-categories (tax-incl., MRP and selling price, per unit and per use), consumable or refill cost, 12-month running cost with assumptions, discount depth, gaps, willingness-to-pay evidence.
## 6. Customer problems and feedback
Sample size and blocked sources. Themes with counts: (a) the problem being solved, (b) complaints about current products, (c) unmet needs and price objections. The best 10 quotes with source keys (full set and URLs in `customer-voice.md`; at least 15 at screen, 40 at deep dive).
## 7. Marketing channels
What could not be observed. Channel map per player, observed vs inferred (Meta Ad Library, Instagram/YouTube counts, creators, Google ads, SEO/blog, marketplaces, offline, offers). Hooks. CPM / CPC / CVR / implied CPO vs max CAC. White space.
## 8. Product feasibility
Does the product do what it would claim? Physics, performance or supplier evidence, cheapest honest test. Omit detail that cannot change the verdict.
## 9. Regulatory
Licences, labels, certifications as relevant (FSSAI, BIS, CDSCO, Legal Metrology, GST, CCPA/ASCI, E-Commerce Rules, DPDP): item, finding, source and date, blocker yes/no. Claim risks. Trademark status. "Verify with a professional before launch."
## 10. Segments and persona
Segments ranked by evidence, the recommended persona, and who cannot be served.
## 11. Opportunities
Pivots and adjacent ideas, each with evidence and status (GO / PARK / idea only) and what would move it.
## 12. Launch plan and growth potential, if the venture continues
First 90 days (offer, claims we can substantiate, test design feeding `playbooks/smoke-test.md`, budget, calendar, kill checkpoints day 30/60/90, founder approvals). Repeat rate, extensions, other cities, ceiling of a side-income business, economics fit (max CAC, contribution; hand-off to Finance).
## 13. Kill-criteria scorecard
Section 5 of this playbook, PASS / FAIL / UNKNOWN per criterion with number and source (one column per option if several).
## 14. Unknowns and next tests
Cheapest first; mark which need founder OK.
## 15. What we're missing
Gaps, wrong assumptions, ignored opportunities, ranked by impact.

Appendices (links only): customer-voice.md, sources.md, bench-test-spec.md, calc/, raw/, archive/. Add a short reconciliation table when a figure changed between drafts.
```

## 5. Kill criteria (defaults, tied to budget and goal; founder to confirm)

Founder context: **$10k (~₹8.5L) total, steady side income, proof of concept in 3 to 6 months**, small reversible tests. Side-income target is not yet stated by the founder; the default below is an assumption, flagged for confirmation.

| # | Criterion | Kill if | Must-pass? |
|---|---|---|---|
| 1 | **Side-income size** | Base-case SOM at month 12 cannot support net profit of about **₹50k/month (about $600)** in India (assumption; confirm with founder) | Yes |
| 2 | **Test affordability** | A smoke test needs more than **₹25k per product** of ad spend, or first inventory plus licences exceeds **35% of budget (about ₹3L)** before demand is proven | Yes |
| 3 | **CAC feasibility** | Plausible CPO (CPC / CVR benchmark range) is above the max CAC from unit economics even at the optimistic end | Yes |
| 4 | **Regulatory blocker** | A licence or certification is required that takes more than **3 months** or more than **10% of budget**, or the product cannot be sold without it | Yes |
| 5 | **Margin** | Contribution margin after tax, landed cost, shipping, fees and returns is below about **35%** of the tax-inclusive price (assumption; some categories justify less if repeat is proven) | No |
| 6 | **Competition** | No defensible wedge: a marketplace private label or incumbent already sells the same thing for less and we have no proof-led or niche angle | No |
| 7 | **Demand evidence** | No search, review or community evidence of the problem in the target country | No |
| 8 | **Claim risk** | The only differentiator is a claim we cannot legally or honestly make (health, ORS, unsubstantiated performance) | Yes |
| 9 | **Concentration** | More than half of the plausible SOM depends on one platform or a single supplier with no alternative | No |

Rule: any must-pass FAIL = NO-GO (Stage 1: KILL). Two or more non-must-pass FAILs = NO-GO unless the report names a specific fix and its cost. UNKNOWN on a must-pass = PARK with a named validation task, never GO. Pass thresholds in this table may be changed only by the founder; record changes in `decisions/`.

## 6. India go-to-market fit table (fill with sourced values; the "prior" column is a starting expectation to check, not a fact)

| Dimension | India prior | What to fill in | Verdict |
|---|---|---|---|
| Market size for the category | Very large population, price-sensitive | Sourced TAM/SAM/SOM in INR | |
| Customer value per order | Low-ticket sensitive | Median shelf price tax-incl., price ladder gaps | |
| Competition and marketplaces | Crowded: Amazon.in, Flipkart, Meesho, Nykaa, quick commerce, D2C brands | Top players, private label share, rating counts | |
| Paid acquisition cost | Lower CPM/CPC, lower AOV | CPM, CPC, CVR ranges with source | |
| Payments and checkout | UPI, cards, COD and RTO risk (prepaid-only per our rule) | Gateway fees | |
| Logistics and returns | Cheap but variable; pincode coverage, RTO | Per-order cost and delivery time | |
| Tax | GST (rate by HSN code; prices tax-inclusive per MRP rules) | Rate for this product, registration threshold | |
| Regulation for this category | FSSAI, BIS, CDSCO, Legal Metrology as relevant | Licence, time, cost, blocker | |
| Advertising rules | Meta policies, ASCI, CCPA | Constraints that affect the angle | |
| Installation and service | Dealer/plumber networks for plumbed goods | Who installs, who services | |
| Speed to a signal | | Days to 25 paid pre-orders at benchmark CPO | |
| Overall | | | Fit / no fit |

## 7. Keeping token use low
1. **Screen first.** Most ideas should die or park at Stage 1 (about 1 hour, 2 pages). Do not start Stage 2 without the CEO's confirmation.
2. **Standard-mode web search by default**; extended mode only for a question a decision depends on, and say why in the report.
3. **Budget the reading**: Stage 1 at most about 15 searches and 15 page fetches; Stage 2 at most about 40 searches and 25 fetches unless the CEO raises it. Use the search snippet when it contains the number; fetch only to confirm a number that matters.
4. **Prompt the fetch**: ask the page fetch tool for the specific fields (price, pack, claims, review count), not the whole page.
5. **Keep a ledger**: `research/sources.md` records what was read so nothing is fetched twice. Reuse category and country research across ventures (regulatory, CPM/CPC, payments, logistics are country facts: store them once under `playbooks/` or `research/` and update, not redo).
6. **Competitors**: profile the top 3 to 5 per sub-category with the quick-scan template (Stage 2: at least 15 players overall); deep profile only the closest one or two.
7. **No raw dumps** in the report: tables, ranges and one line of reasoning per row. Raw notes stay in `research/raw/`.
8. **Sonnet** for the Market Researcher (per the model decision). The CEO may name opus for a final go/no-go synthesis only with a stated reason.
9. **Do not re-run** a finished stage. Updating means changing the affected rows and dating them.
10. **No paid reports or data tools** without founder OK; free sources first (government and regulator sites, marketplace listings, Meta Ad Library, Google Trends, public reviews).

## 8. Hand-offs and records
- Market Researcher returns the report to the CEO, who reviews it against the brief and passes the verdict plus any pushback (with the CEO's own view) to the founder.
- Finance Analyst formalises the economics in `ventures/<venture>/finance/` once Stage 2 passes.
- Marketing Lead uses the customer language and channel findings for the smoke-test plan; Developer starts the landing page only after a founder GO.
- Chief of Staff logs the verdict in `decisions/YYYY-MM-DD-<venture>-market-research.md` and updates `ORG.md` and `ventures/README.md`.
- Outward-facing steps found during research (a supplier quote, a licence application, a paid report, a trademark search, customer interviews) are listed for founder OK, never taken by the researcher.

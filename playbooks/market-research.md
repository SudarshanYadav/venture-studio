# Playbook: market research (India and UAE) before any build or spend

Owner: Market Researcher (`.claude/agents/market-researcher.md`). Inputs: Finance Analyst (max CAC and margin check), Marketing Lead (customer language, channels). CEO reviews each stage; the founder decides go / no-go. Rule adopted 2026-11-26 ([decision](../decisions/2026-11-26-market-research-and-model-budget.md)).

## 1. When it runs
- Every **new venture or new product** gets market research **before** a landing page, ad plan, supplier order or any spend. No exceptions for "small" ideas; the screen is cheap.
- It comes **before** `playbooks/smoke-test.md` step 1. The research proposes the country, the price band, the claim risks and the test design; the smoke test then proves CAC.
- Existing ventures (Mrudu, Lavan) are covered only if the founder asks (open question in the decision log).
- Research is not a substitute for the smoke test. It cannot prove demand; it can kill ideas cheaply and narrow what the test must prove.

## 2. Two-step gate

| | Stage 1: Screen | Stage 2: Deep dive |
|---|---|---|
| Purpose | Kill bad ideas cheaply, pick country, list what Stage 2 must prove | Produce the go / no-go the founder can sign |
| Effort | About 1 hour of agent work. About 15 searches (standard mode), at most 8 page fetches, 2 pages out | Up to about 4 hours. Extended search only for a question a decision depends on |
| Output | `ventures/<venture>/research/screen.md` | `ventures/<venture>/research/market-research.md` (template, section 4) |
| Runs when | Always | Only if the screen passes **and** the CEO confirms (founder OK if it needs paid data) |
| Ends with | PASS / KILL / PARK, country lean, 3 open questions | GO / GO-NARROW / NO-GO, country first, launch plan |

### Stage 1 screen: contents (all on 2 pages)
1. Market definition in one sentence (country, buyer, use case, price band, what is out of scope).
2. Rough SOM range for each country from **one** method each, labelled Low confidence.
3. Top 5 competitors per country with shelf price and pack. Status quo alternative.
4. One-line regulatory flag per country: blocked / needs licence (time, cost) / free to sell.
5. Gross margin sanity check: shelf price (tax-incl.) minus tax, landed cost estimate, fees. Is the implied max CAC above what Meta CPCs in that country make plausible?
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

## 4. Report template: `ventures/<venture>/research/market-research.md`

```markdown
# <Venture>: market research (India and UAE)
Date: | Researcher: | Stage: screen / deep dive | Currency: INR and AED, converted at <rate, date>

## 0. Verdict (write last, put first)
GO / GO-NARROW / NO-GO. Country first: India / UAE / neither. Confidence: H/M/L.
SOM (12-month, deciding country): <range>. Deciding number: <x>. The one assumption that would change this: <y>, test: <z>.
Kill-criteria scorecard result: <n of m pass; must-pass failures: ...>

## 1. Market definition
One sentence: geography, buyer, use case, price band. Out of scope: ...

## 2. Market potential (TAM / SAM / SOM)
| | India | UAE | Method(s) | Confidence | Source |
|---|---|---|---|---|---|
| TAM (annual, INR/AED) | | | | | |
| SAM | | | | | |
| SOM, 12 months | | | | | |
Arithmetic shown below the table. Methods compared; if >3x apart, why. Biggest swing factor.
Market attractiveness score (market-sizing skill, /50): India __ UAE __.

## 3. Customers and demand
Who buys (segments, size), the pain in their own words (short sourced excerpts), triggers, what they do today, search demand (volume and trend if available), seasonality.

## 4. Competition
Landscape table per country: player, type (brand / marketplace private label / local), price, pack, price per use, channel, claims, review count and themes, ad activity. Status quo and substitutes.
Positioning whitespace. Their strengths we cannot match. Threat of marketplace private label or a big brand copying. Defensibility: low / medium / high and why.

## 5. Pricing benchmarks
Price ladder per country (tax-incl. shelf price, per unit and per use), discount depth, our implied price and margin structure, willingness-to-pay evidence.

## 6. Channels and acquisition cost
Where buyers are reachable (Meta, Google, marketplaces: Amazon, Flipkart, Noon, quick commerce, retail, communities). Indicative CPM / CPC / CVR per country with source and confidence. Implied CPO vs max CAC from the finance model. Cheapest honest test.

## 7. Regulatory and compliance snapshot
Per country: licences, labels, certifications (India: FSSAI, BIS, CDSCO, Legal Metrology, GST, CCPA/ASCI, E-Commerce Rules, DPDP; UAE: MOIAT, MOCCAE, Ministry of Economy, emirate food authority, trade licence, VAT, advertising permits). Time, cost, blocker yes/no, source and date. Claim risks (health, ORS-type reserved terms). Trademark status: not searched / searched. "Verify with a professional before launch."

## 8. India vs UAE comparison
(table in section 6 of the playbook, filled with sourced values and a winner per row)

## 9. Launch plan (first 90 days, one country first)
Offer and price, claims we can substantiate, test design (feeds playbooks/smoke-test.md), budget (INR/AED and share of the $10k), calendar with payday, supplier/inventory plan and minimum order, licences needed first, milestones, kill checkpoints at day 30 / 60 / 90, what the founder must approve.

## 10. Growth potential
Repeat and refill rate (assumption or sourced), product line extensions, second country, marketplace or retail, ceiling of a side-income business: monthly net profit at 12 and 24 months (low / base / high).

## 11. Economics fit
Max CAC and margin per unit from the finance model (link), contribution per order, inventory cash tied up vs budget, payback. Hand-off to Finance Analyst for the formal calculation.

## 12. Kill-criteria scorecard (playbook section 5), PASS / FAIL / UNKNOWN with number and source

## 13. Recommendation
GO / GO-NARROW / NO-GO, country first, why, the next step, the cost of that step.

## 14. Unknowns and validation tasks (cheapest first)
## 15. Source ledger (URL, date, what it gave, full read / snippet only / blocked)
## 16. Pushback raised / What I'd do differently / what we're missing
```

## 5. Kill criteria (defaults, tied to budget and goal; founder to confirm)

Founder context: **$10k (~₹8.5L) total, steady side income, proof of concept in 3 to 6 months**, small reversible tests. Side-income target is not yet stated by the founder; the default below is an assumption, flagged for confirmation.

| # | Criterion | Kill if | Must-pass? |
|---|---|---|---|
| 1 | **Side-income size** | Base-case SOM at month 12 cannot support net profit of about **₹50k/month (about $600)** in the deciding country (assumption; confirm with founder) | Yes |
| 2 | **Test affordability** | A smoke test needs more than **₹25k per product** of ad spend, or first inventory plus licences exceeds **35% of budget (about ₹3L)** before demand is proven | Yes |
| 3 | **CAC feasibility** | Plausible CPO (CPC / CVR benchmark range) is above the max CAC from unit economics even at the optimistic end | Yes |
| 4 | **Regulatory blocker** | A licence or certification is required that takes more than **3 months** or more than **10% of budget**, or the product cannot be sold without it | Yes |
| 5 | **Margin** | Contribution margin after tax, landed cost, shipping, fees and returns is below about **35%** of the tax-inclusive price (assumption; some categories justify less if repeat is proven) | No |
| 6 | **Competition** | No defensible wedge: a marketplace private label or incumbent already sells the same thing for less and we have no proof-led or niche angle | No |
| 7 | **Demand evidence** | No search, review or community evidence of the problem in the target country | No |
| 8 | **Claim risk** | The only differentiator is a claim we cannot legally or honestly make (health, ORS, unsubstantiated performance) | Yes |
| 9 | **Concentration** | More than half of the plausible SOM depends on one platform or a single supplier with no alternative | No |

Rule: any must-pass FAIL = NO-GO (Stage 1: KILL). Two or more non-must-pass FAILs = NO-GO unless the report names a specific fix and its cost. UNKNOWN on a must-pass = PARK with a named validation task, never GO. Pass thresholds in this table may be changed only by the founder; record changes in `decisions/`.

## 6. India vs UAE comparison table (fill with sourced values; the "prior" column is a starting expectation to check, not a fact)

| Dimension | India (prior) | UAE (prior) | What to fill in | Winner for this venture |
|---|---|---|---|---|
| Market size for the category | Very large population, price-sensitive | About 10 to 11 million people, mostly expats, high income | Sourced TAM/SAM/SOM in INR and AED | |
| Customer value per order | Lower price points, low-ticket sensitive | Higher price points tolerated | Median shelf price tax-incl. | |
| Competition and marketplaces | Crowded: Amazon.in, Flipkart, Meesho, Nykaa, quick commerce, D2C brands | Amazon.ae, Noon, Talabat, Carrefour, fewer D2C brands | Top players, private label share | |
| Paid acquisition cost | Lower CPM/CPC, lower AOV | Higher CPM/CPC, higher AOV | CPM, CPC, CVR ranges with source | |
| Payments and checkout | UPI, cards, COD and RTO risk (prepaid-only per our rule) | Cards, Apple Pay, BNPL (Tabby, Tamara), COD | Local norms, gateway fees | |
| Logistics and returns | Cheap but variable; pincode coverage, RTO | Fast but pricier; small country, last-mile couriers | Per-order cost and delivery time | |
| Tax | GST (rate by HSN code; prices tax-inclusive per MRP rules) | VAT 5%; corporate tax thresholds apply | Rate for this product, registration threshold | |
| Regulation for this category | FSSAI, BIS, CDSCO, Legal Metrology as relevant | MOIAT, MOCCAE, Ministry of Economy, emirate food authority as relevant | Licence, time, cost, blocker | |
| Advertising rules | Meta policies, ASCI, CCPA | Meta policies, UAE advertising and influencer permit rules | Constraints that affect the angle | |
| Setup to start selling | No entity change if the founder already operates in India | Trade licence (mainland or free zone), bank account, time and cost | Cost and weeks | |
| Founder fit | Founder can operate in either country | Founder can operate in either country | Where the founder can physically test (local demos, samples) | |
| Speed to a signal | | | Days to 25 paid pre-orders at benchmark CPO | |
| Overall | | | | India / UAE / neither |

## 7. Keeping token use low
1. **Screen first.** Most ideas should die or park at Stage 1 (about 1 hour, 2 pages). Do not start Stage 2 without the CEO's confirmation.
2. **Standard-mode web search by default**; extended mode only for a question a decision depends on, and say why in the report.
3. **Budget the reading**: Stage 1 at most about 15 searches and 8 page fetches; Stage 2 at most about 40 searches and 25 fetches unless the CEO raises it. Use the search snippet when it contains the number; fetch only to confirm a number that matters.
4. **Prompt the fetch**: ask the page fetch tool for the specific fields (price, pack, claims, review count), not the whole page.
5. **Keep a ledger**: `research/sources.md` records what was read so nothing is fetched twice. Reuse category and country research across ventures (regulatory, CPM/CPC, payments, logistics are country facts: store them once under `playbooks/` or `research/` and update, not redo).
6. **Competitors**: profile the top 3 to 5 per country with the quick-scan template; deep profile only the closest one or two.
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

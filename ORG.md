# ORG: venture-studio org chart and status

Last updated: 2026-11-26 by chief-of-staff (model allocation and market-research gate adopted; global quality bar adopted; Mrudu landing, brand and ads relabelled DRAFT after the quality audit).

**Rule: two-way street.** Every specialist challenges the brief and flags what the studio is missing; every report ends with "What I'd do differently / what we're missing"; the CEO passes material pushback to the founder with its own view alongside. See `CLAUDE.md` §5 and [decision](decisions/2026-11-25-two-way-street.md).

```
Founder (board: approves money, launches, publishing, contacts, GitHub pushes)
└── CEO: Chanakya (main Claude Code session: staffs, briefs, reviews, reports; does not do the work)
    ├── Chief of Staff   (.claude/agents/chief-of-staff.md)
    ├── Recruiter        (.claude/agents/recruiter.md)
    ├── Developer        (.claude/agents/developer.md)
    ├── Marketing Lead   (.claude/agents/marketing-lead.md)
    ├── Finance Analyst  (.claude/agents/finance-analyst.md)
    └── Market Researcher (being recruited)
```

## Roles

| Role | Remit | Skills / playbooks | Model |
|---|---|---|---|
| Chief of Staff | Keeps ORG.md, `decisions/`, venture folders and indexes current; onboards new agents; packages the org (git, zip). | `playbooks/smoke-test.md` | haiku |
| Recruiter | Finds existing expert skills/agents/plugins (catalogs, web, public repos); vets for safety + licence; installs into `.claude/skills/` with provenance in `SOURCES.md`; drafts new agent definitions. | `.claude/skills/SOURCES.md` | sonnet |
| Developer | Landing pages, refundable pre-order checkout (Razorpay), Meta Pixel + CAPI, deploys; verifies with Playwright. | frontend-design, cro, copywriting, conversion-tracking, offers | sonnet |
| Marketing Lead | Meta ad test plans, creatives, offline tests, tracking sheets, ad compliance. | ads, ad-creative, ab-testing, customer-research, marketing-psychology, offers, launch; `playbooks/smoke-test.md` | sonnet |
| Finance Analyst | Unit economics, max CAC / CPO go-no-go, payback, pricing, sensitivity; builds calculators. | ads/references/payback-period.md, pricing, ab-testing/references/sample-size-guide.md; `playbooks/smoke-test.md` | sonnet |
| Market Researcher (being recruited) | Deep market research for India and UAE (market potential, competition, launch plan, growth potential) before any landing page, ads or spend. | `playbooks/market-research.md` (being written) | sonnet |

## Current assignments

| Role | Assignment | Status | Output |
|---|---|---|---|
| Finance Analyst | Unit economics + go/no-go calculator for Mrudu and Lavan | **DONE** (reviewed by CEO) | `ventures/mrudu-shower-softener/finance/unit-economics.md`, `.../calculator.html`; published privately at https://claude.ai/artifact/CynyzBu2qb1XW1uxzsDFQ6 |
| Finance Analyst | Mrudu GST-inclusive, prepaid-only scenario | **DONE** (reviewed by CEO) | Section 0 of `ventures/mrudu-shower-softener/finance/unit-economics.md`. Bars: max CAC ₹730, GO ₹511, trusted GO ₹475, trusted KILL ₹1,096. [Decision](decisions/2026-11-25-mrudu-launch-bars-gst-prepaid.md) |
| Developer | Mrudu refundable pre-order landing page | **DRAFT: fails quality bar (see quality-audit.md)**: 6 of 21 checks pass. Not deployed, no keys. Checkout + Pixel logic tested with stubs; server code never run (Node not installed). | `ventures/mrudu-shower-softener/landing/` (`index.html`, `policies.html`, `server/`, `api/`, `README.md`, `screenshots/`) |
| Developer | Lavan landing page | **NOT STARTED** (Lavan is second test) | None. |
| Marketing Lead | Mrudu Meta test plan | **DRAFT: fails quality bar (see quality-audit.md)**: ads 6 of 14 checks pass. Verdict: do not launch until cartridge capacity is measured. | `ventures/mrudu-shower-softener/marketing/` (`test-plan.md`, `creatives.md`, `tracking.csv`, `offline-test.md`) |
| Marketing Lead | Mrudu brand kit | **DRAFT: fails quality bar (see quality-audit.md)**: 4 of 15 checks pass. Note: Developer has not yet applied the brand hand-off to the landing page (waiting until the capacity blocker is resolved); no stock images downloaded. | `ventures/mrudu-shower-softener/marketing/brand/` (`brand-kit.md`, `wordmark.svg`, `icon.svg`, `product-render.svg`, `ad-mockups.html`, `images.md`, `handoff-to-developer.md`) |
| Marketing Lead | Global-standard creative quality bar + audit | **DONE** (reviewed by CEO) | `playbooks/quality-bar.md`, `ventures/mrudu-shower-softener/marketing/quality-audit.md`. [Decision](decisions/2026-11-26-global-quality-bar.md) |
| Recruiter | Initial skill sourcing (12 marketing/design skills) | **DONE** (vetted by CEO) | `.claude/skills/`, `.claude/skills/SOURCES.md` |
| Chief of Staff | Set up persistent org pack + local git repo | **DONE** | This repository |
| Chief of Staff | Two-way-street rule | **DONE** | [Decision](decisions/2026-11-25-two-way-street.md) |
| Finance Analyst | Mrudu cartridge-capacity desk research | **STOPPED by founder 2026-11-26, then dropped for now**; no partial output | None. |
| Chief of Staff | Migration package for the founder's personal account | **DONE**: transferred and pushed to private GitHub repo SudarshanYadav/venture-studio on 2026-11-26 | `export/venture-studio-2026-11-26.zip`, [MIGRATION.md](MIGRATION.md), [founder-preferences.md](founder-preferences.md). [Decision](decisions/2026-11-26-migrate-to-personal-account.md) |
| Recruiter | Market-research agent + playbook | **IN PROGRESS** | `playbooks/market-research.md` (being written); Market Researcher agent not yet created. |
| Chief of Staff | Model allocation + new rules | **DONE** | `.claude/agents/*.md` (model lines), [CLAUDE.md](CLAUDE.md) §9 and §12. [Decision](decisions/2026-11-26-market-research-and-model-budget.md) |

**Quality bar (2026-11-26):** Founder feedback on 2026-11-26 was that the work was college-project quality and that "Mrudu" had no research behind it. The new bar is global standard: brand, website and ad work is DONE only when every must-pass item in [playbooks/quality-bar.md](playbooks/quality-bar.md) passes and at least 85% of all items pass ([decision](decisions/2026-11-26-global-quality-bar.md), [audit](ventures/mrudu-shower-softener/marketing/quality-audit.md)). Project tracked in Notion: https://app.notion.com/p/424309931dab8138a712cdac7679f104

**Blocker:** all Mrudu ad spend is blocked until cartridge capacity is measured ([decision](decisions/2026-11-25-mrudu-cartridge-capacity-blocker.md)). Founder said "Not yet" to the ~₹3–5k bench test on 2026-11-25.

**Git:** repo at https://github.com/SudarshanYadav/venture-studio (private, branch `main`). All studio work is committed and pushed (founder approved pushes to this repo on 2026-11-26). Note: the 2026-11-26 quality-bar work was pushed to branch `claude/sleepy-bardeen-45dzuq`, not `main`.

**Migration:** done 2026-11-26. The zip was unpacked in a Claude Code cloud session on the founder's personal account and pushed as commit `791d891`. Founder preferences live in [founder-preferences.md](founder-preferences.md), not per-machine memory. The calculator artifact link above is still on the old account and has not been republished; the local `ventures/mrudu-shower-softener/finance/calculator.html` is available.

## Next steps (awaiting founder direction)

1. **Founder OK on proposed agent-file changes** to enforce `playbooks/quality-bar.md` (pending).
2. **Marketing Lead pushback: buy 2–3 sample units and strips first (~₹3–5k).** One purchase unblocks the cartridge bench test, proof footage and product photography (see [quality-audit.md](ventures/mrudu-shower-softener/marketing/quality-audit.md)). Needs founder OK; blocker for all Mrudu spend.
3. **Customer research missing**: no `ventures/mrudu-shower-softener/marketing/research.md`; no hook traces to a real customer quote. Name research for "Mrudu" also missing.
4. **Benchmark sites not visited** because of the session's network limit.
5. Developer applies the brand hand-off once the capacity blocker clears and the brand passes the bar.
6. Founder OKs needed: Razorpay and Meta test accounts; the ship date; seller/grievance-officer details for the policies page; Mrudu trademark check.
7. Proposed CLAUDE.md tweaks from the Chief of Staff, awaiting founder OK: the "right job?" check becomes one line inside each brief; founder reports get a fixed "Pushback raised / CEO view / founder decision?" line.
8. **Founder decision needed:** should Mrudu and Lavan also get the market research, or only new ventures? Awaiting founder decision ([decision](decisions/2026-11-26-market-research-and-model-budget.md)).

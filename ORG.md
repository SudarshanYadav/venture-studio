# ORG: venture-studio org chart and status

Last updated: 2026-11-25 by chief-of-staff.

```
Founder (board: approves money, launches, publishing, contacts, GitHub pushes)
└── CEO (main Claude Code session: staffs, briefs, reviews, reports; does not do the work)
    ├── Chief of Staff   (.claude/agents/chief-of-staff.md)
    ├── Recruiter        (.claude/agents/recruiter.md)
    ├── Developer        (.claude/agents/developer.md)
    ├── Marketing Lead   (.claude/agents/marketing-lead.md)
    └── Finance Analyst  (.claude/agents/finance-analyst.md)
```

## Roles

| Role | Remit | Skills / playbooks |
|---|---|---|
| Chief of Staff | Keeps ORG.md, `decisions/`, venture folders and indexes current; onboards new agents; packages the org (git, zip). | `playbooks/smoke-test.md` |
| Recruiter | Finds existing expert skills/agents/plugins (catalogs, web, public repos); vets for safety + licence; installs into `.claude/skills/` with provenance in `SOURCES.md`; drafts new agent definitions. | `.claude/skills/SOURCES.md` |
| Developer | Landing pages, refundable pre-order checkout (Razorpay), Meta Pixel + CAPI, deploys; verifies with Playwright. | frontend-design, cro, copywriting, conversion-tracking, offers |
| Marketing Lead | Meta ad test plans, creatives, offline tests, tracking sheets, ad compliance. | ads, ad-creative, ab-testing, customer-research, marketing-psychology, offers, launch; `playbooks/smoke-test.md` |
| Finance Analyst | Unit economics, max CAC / CPO go-no-go, payback, pricing, sensitivity; builds calculators. | ads/references/payback-period.md, pricing, ab-testing/references/sample-size-guide.md; `playbooks/smoke-test.md` |

## Current assignments

| Role | Assignment | Status | Output |
|---|---|---|---|
| Finance Analyst | Unit economics + go/no-go calculator for Mrudu and Lavan | **DONE** (reviewed by CEO) | `ventures/mrudu-shower-softener/finance/unit-economics.md`, `.../calculator.html`; published privately at https://claude.ai/artifact/CynyzBu2qb1XW1uxzsDFQ6 |
| Developer | Refundable pre-order landing pages for Mrudu and Lavan | **STOPPED before delivery**: restart from scratch | None kept. Partial unreviewed code was deliberately not carried over. |
| Marketing Lead | Meta ad test plan for both products | **STOPPED before delivery**: restart from scratch | None. |
| Recruiter | Initial skill sourcing (12 marketing/design skills) | **DONE** (vetted by CEO) | `.claude/skills/`, `.claude/skills/SOURCES.md` |
| Chief of Staff | Set up persistent org pack + local git repo | **DONE** | This repository |

## Next steps (awaiting founder direction)

1. Developer: build Mrudu landing page (refundable paid pre-order, test-strip proof, no medical claims), then Lavan.
2. Marketing Lead: ad test plan per `playbooks/smoke-test.md` (~₹25k/product, ~10 days, ≥25 paid pre-orders).
3. Finance Analyst: add GST-inclusive and prepaid-only scenarios to the calculator (see `decisions/2026-11-25-finance-results.md`).
4. Before any launch: founder OK on spend, public pages and trademark check on brand names.

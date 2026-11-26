# ORG: venture-studio org chart and status

Last updated: 2026-11-26 by chief-of-staff (migration package built for the founder's personal account; founder preferences folded into the repo; capacity desk research stopped and dropped).

**Rule: two-way street.** Every specialist challenges the brief and flags what the studio is missing; every report ends with "What I'd do differently / what we're missing"; the CEO passes material pushback to the founder with its own view alongside. See `CLAUDE.md` §5 and [decision](decisions/2026-11-25-two-way-street.md).

```
Founder (board: approves money, launches, publishing, contacts, GitHub pushes)
└── CEO: Chanakya (main Claude Code session: staffs, briefs, reviews, reports; does not do the work)
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
| Finance Analyst | Mrudu GST-inclusive, prepaid-only scenario | **DONE** (reviewed by CEO) | Section 0 of `ventures/mrudu-shower-softener/finance/unit-economics.md`. Bars: max CAC ₹730, GO ₹511, trusted GO ₹475, trusted KILL ₹1,096. [Decision](decisions/2026-11-25-mrudu-launch-bars-gst-prepaid.md) |
| Developer | Mrudu refundable pre-order landing page | **DONE** (reviewed by CEO). Not deployed, no keys. Checkout + Pixel logic tested with stubs; server code never run (Node not installed). | `ventures/mrudu-shower-softener/landing/` (`index.html`, `policies.html`, `server/`, `api/`, `README.md`, `screenshots/`) |
| Developer | Lavan landing page | **NOT STARTED** (Lavan is second test) | None. |
| Marketing Lead | Mrudu Meta test plan | **DONE** (reviewed by CEO). Verdict: do not launch until cartridge capacity is measured. | `ventures/mrudu-shower-softener/marketing/` (`test-plan.md`, `creatives.md`, `tracking.csv`, `offline-test.md`) |
| Marketing Lead | Mrudu brand kit | **DONE** (reviewed by CEO). Note: Developer has not yet applied the brand hand-off to the landing page (waiting until the capacity blocker is resolved); no stock images downloaded. | `ventures/mrudu-shower-softener/marketing/brand/` (`brand-kit.md`, `wordmark.svg`, `icon.svg`, `product-render.svg`, `ad-mockups.html`, `images.md`, `handoff-to-developer.md`) |
| Recruiter | Initial skill sourcing (12 marketing/design skills) | **DONE** (vetted by CEO) | `.claude/skills/`, `.claude/skills/SOURCES.md` |
| Chief of Staff | Set up persistent org pack + local git repo | **DONE** | This repository |
| Chief of Staff | Two-way-street rule | **DONE** | [Decision](decisions/2026-11-25-two-way-street.md) |
| Finance Analyst | Mrudu cartridge-capacity desk research | **STOPPED by founder 2026-11-26, then dropped for now**; no partial output | None. |
| Chief of Staff | Migration package for the founder's personal account | **DONE** (founder does the transfer) | `export/venture-studio-2026-11-26.zip`, [MIGRATION.md](MIGRATION.md), [founder-preferences.md](founder-preferences.md). [Decision](decisions/2026-11-26-migrate-to-personal-account.md) |

**Blocker:** all Mrudu ad spend is blocked until cartridge capacity is measured ([decision](decisions/2026-11-25-mrudu-cartridge-capacity-blocker.md)). Founder said "Not yet" to the ~₹3–5k bench test on 2026-11-25.

**Git:** not installed on this machine, so nothing from today is committed.

**Migration:** package built 2026-11-26: `export/venture-studio-2026-11-26.zip` (studio files only; the `export/` folder itself is not inside it). Steps for the founder in [MIGRATION.md](MIGRATION.md). Founder preferences now live in [founder-preferences.md](founder-preferences.md), not per-machine memory. The calculator artifact link above belongs to the old account.

## Next steps (awaiting founder direction)

1. **Founder decides on the cartridge bench test** (~₹3–5k). Blocker for all Mrudu spend.
2. Developer applies the brand hand-off once the capacity blocker clears.
3. Founder OKs needed: Razorpay and Meta test accounts; the ship date; seller/grievance-officer details for the policies page; Mrudu trademark check.
4. Proposed CLAUDE.md tweaks from the Chief of Staff, awaiting founder OK: the "right job?" check becomes one line inside each brief; founder reports get a fixed "Pushback raised / CEO view / founder decision?" line.

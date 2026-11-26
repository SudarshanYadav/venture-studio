# 2026-11-26: Market-research gate for new ventures, and model and token budget

**Decision:** Two founder decisions, recorded together.

1. **Market-research gate.** For new ventures, deep market research for India and UAE (market potential, competition, launch plan, growth potential) must be done before any landing page, ads or spend. Method: `playbooks/market-research.md` (being written). Recorded in [CLAUDE.md](../CLAUDE.md) §9.
2. **Model and token budget.** Admin and records work runs on haiku (Chief of Staff). Research, build, marketing and finance work runs on sonnet (Recruiter, Developer, Marketing Lead, Finance Analyst, and the Market Researcher once recruited). Opus is used only by the CEO session, or when the CEO states a reason in the brief. Briefs stay tight, agents do cheap desk research first, and finished work is not re-run without a reason. Recorded in [CLAUDE.md](../CLAUDE.md) §12; per-role models in [ORG.md](../ORG.md).

**Context / why:** Agent files previously inherited the session model (`model: inherit`). The founder asked for a model allocation to reduce token use, and for market research before spend on new ventures. The Mrudu and Lavan work reached landing and ad drafts without customer or market research (see [ORG.md](../ORG.md) next steps).

**Numbers:**
- Model per role, as set in `.claude/agents/*.md` frontmatter: Chief of Staff haiku; Recruiter, Developer, Marketing Lead, Finance Analyst sonnet.
- Token savings: not measured. No before/after usage figures were recorded for this change.

**Status:** Adopted. Model lines and CLAUDE.md §9 and §12 edited locally. Not committed or pushed. The Market Researcher agent and `playbooks/market-research.md` are being recruited (IN PROGRESS).

**Open risks:**
- CLAUDE.md §9 points to `playbooks/market-research.md`, which does not exist yet.
- Open founder question: should Mrudu and Lavan also get the market research, or only new ventures? Awaiting founder decision.
- Sonnet on finance work may be weaker than opus for high-stakes go/no-go synthesis. Opus is allowed only with a stated reason in the brief.
- Not verified in this session that the frontmatter `model` change takes effect on the next agent start.

**Approved by:** Founder (board), as relayed by the CEO on 2026-11-26.

**Supersedes:** nothing. Earlier agent files used `model: inherit`, which this decision replaces.

# 2026-11-27: Feedback loop: agents learn from founder feedback

**Decision:** Founder feedback is written into the files agents read. Each agent file gets a "Lessons from the founder" section, and CLAUDE.md §13 sets the sorting and review rules. Agents keep no memory between jobs, so the files are the only learning channel.

**Approved by:** founder, 2026-11-27.

**Context / why:** Agents start every job with no memory of earlier feedback. The same founder points (research before build, India only, token use, global quality bar, no drawings presented as finished) had to be repeated across sessions. Writing them into the agent files makes each brief's reader carry them forward.

**Choice / rules (full text in [CLAUDE.md](../CLAUDE.md) §13):**
- Founder feedback is sorted by the CEO into: (a) agent-specific, goes in that agent's lessons section; (b) method, goes in `playbooks/*.md`; (c) studio-wide, goes in `CLAUDE.md` or `founder-preferences.md`; (d) one-off, not saved.
- The Chief of Staff writes each lesson in dated, with a one-line reason, and notes it in [ORG.md](../ORG.md).
- The CEO reviews every deliverable against that agent's lessons and sends it back if one is missed.
- At most about 15 lessons per agent. Monthly, the Chief of Staff merges duplicates and moves stable lessons into the playbooks.
- Briefs point agents at their own lessons section (CLAUDE.md §3).

**Numbers (lessons seeded today):**

| Agent | Lessons seeded | Count |
|---|---|---|
| All six agents | research before build; India only; watch tokens | 3 each |
| Market Researcher | one report per venture; cover players, prices, feedback, channels; read pages, mark snippets S; link every competitor | 4 more |
| Marketing Lead, Developer | global-standard bar; no drawings or placeholders as finished | 2 more each |
| Chief of Staff | write founder feedback into the right file per §13 | 1 more |

Files: `.claude/agents/*.md` (six files), [market-research playbook](../playbooks/market-research.md) (Link requirement for current players).

**Open risks:**
- Four seeded lessons have no "(why)" text, because the founder's wording did not give one: the market-researcher items on one report per venture, cover players and channels, read pages (S tags) and link every competitor, plus the marketing/developer quality-bar and no-drawings items. Add a reason at the next review.
- The loop depends on the CEO sorting feedback and on the review step. Nothing in the harness enforces it.
- No live job has yet been checked against the new lessons. Verify on the next job.
- Monthly merge is not scheduled; it depends on the Chief of Staff being asked.

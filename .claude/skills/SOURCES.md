# Skill sources and provenance

Every skill in this folder must be listed here with source, licence, date and vetting notes. Unlisted skills must not be used until the recruiter vets them and the CEO approves.

| Skill(s) | Source | Licence | Added | Vetted by | Notes |
|---|---|---|---|---|---|
| ab-testing, ad-creative, ads, conversion-tracking, copywriting, cro, customer-research, launch, marketing-psychology, offers, pricing | coreyhaines31/marketingskills, https://github.com/coreyhaines31/marketingskills | MIT (Copyright (c) 2025 Corey Haines), see `LICENSE-marketingskills` | 2026-11-25 | CEO | Scanned for scripts and prompt injection; only documentation `curl` examples found. `conversion-tracking/scripts/*.py` are local JSON recipe builders/checkers (stdlib only: argparse, json, re, sys, pathlib; no network). `evals/` folders are test prompts, not loaded at runtime. |
| frontend-design | anthropics/skills, https://github.com/anthropics/skills (frontend-design) | See `frontend-design/LICENSE.txt` | 2026-11-25 | CEO | Single SKILL.md, no scripts. |
| competitor-profiling | coreyhaines31/marketingskills, `skills/competitor-profiling` at commit 8fd2fca (2026-11-23), https://github.com/coreyhaines31/marketingskills | MIT (Copyright (c) 2025 Corey Haines), see `LICENSE-marketingskills` | 2026-11-26 | Recruiter | Read SKILL.md, references/templates.md, references/tool-reference.md in full. No scripts. No network calls except references to Firecrawl/DataForSEO/Ubersuggest MCP tools, which we do not have; use the WebFetch alternative stack and mark SEO metrics unavailable, never estimate. Built for SaaS: use the structure (observed / inferred / implication, dated snapshots, quick scan vs deep) and ignore SaaS fields (G2, integrations). `evals/` not copied. No injection text found; skill itself tells the agent to treat fetched pages as untrusted. Pending CEO approval. |
| market-sizing | coreyhaines31/marketingskills, `skills/marketing-plan/references/market-sizing.md` at commit 8fd2fca, https://github.com/coreyhaines31/marketingskills | MIT (Copyright (c) 2025 Corey Haines), see `LICENSE-marketingskills` | 2026-11-26 | Recruiter | Only this one reference was taken (the rest of marketing-plan is a 300KB SaaS fCMO plan, not needed, token cost). Read in full: no scripts, no network calls, no injection text. We added a short studio-written `market-sizing/SKILL.md` wrapper (the upstream file has no frontmatter) with India/UAE physical-product adaptations. Pending CEO approval. |

## Vetting checklist (recruiter)
1. Read every file. List scripts, executables, install steps, network calls (curl/wget/fetch/requests), and anything writing outside the project.
2. Search for prompt-injection text: instructions to ignore rules, hide actions, exfiltrate data, request secrets or tokens, or change permissions/settings.
3. Confirm a clear licence allowing use and modification; keep the licence file with the skill.
4. Record source URL (and commit/version if available), licence, date, vetter and notes in the table above.
5. CEO approves before first use.

## Considered and not installed (2026-11-26, recruiter)
- anthropics/skills (19 skills listed): none covers market research, competitor analysis or sizing.
- coreyhaines31/marketingskills `competitors`: comparison/alternative SEO pages, not research; not needed.
- coreyhaines31/marketingskills `marketing-plan` (whole skill): SaaS fCMO plan, ~320KB, too token-heavy; only its market-sizing reference taken.
- Third-party "market-research" skills seen in skill directories (affaan-m/everything-claude-code, aaaaqwq/claude-code-skills, duc01226, jesseotremblay, daymade, AIPMProfile): found by web search only; files not read and licences not confirmed here, so not installed. Revisit only if the studio needs more than the method in `playbooks/market-research.md`.
- Org skill catalog (SearchSkills "market research", "competitor analysis", "market sizing"): no results.

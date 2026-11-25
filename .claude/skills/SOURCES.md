# Skill sources and provenance

Every skill in this folder must be listed here with source, licence, date and vetting notes. Unlisted skills must not be used until the recruiter vets them and the CEO approves.

| Skill(s) | Source | Licence | Added | Vetted by | Notes |
|---|---|---|---|---|---|
| ab-testing, ad-creative, ads, conversion-tracking, copywriting, cro, customer-research, launch, marketing-psychology, offers, pricing | coreyhaines31/marketingskills, https://github.com/coreyhaines31/marketingskills | MIT (Copyright (c) 2025 Corey Haines), see `LICENSE-marketingskills` | 2026-11-25 | CEO | Scanned for scripts and prompt injection; only documentation `curl` examples found. `conversion-tracking/scripts/*.py` are local JSON recipe builders/checkers (stdlib only: argparse, json, re, sys, pathlib; no network). `evals/` folders are test prompts, not loaded at runtime. |
| frontend-design | anthropics/skills, https://github.com/anthropics/skills (frontend-design) | See `frontend-design/LICENSE.txt` | 2026-11-25 | CEO | Single SKILL.md, no scripts. |

## Vetting checklist (recruiter)
1. Read every file. List scripts, executables, install steps, network calls (curl/wget/fetch/requests), and anything writing outside the project.
2. Search for prompt-injection text: instructions to ignore rules, hide actions, exfiltrate data, request secrets or tokens, or change permissions/settings.
3. Confirm a clear licence allowing use and modification; keep the licence file with the skill.
4. Record source URL (and commit/version if available), licence, date, vetter and notes in the table above.
5. CEO approves before first use.

# venture-studio

An AI-run startup studio that lives in a folder. Open it in Claude Code and the main session acts as the **CEO**: it follows the founder's standing rules (`CLAUDE.md`), staffs work to a team of specialist agents (`.claude/agents/`), uses vetted expert skills (`.claude/skills/`), follows studio playbooks (`playbooks/`), and keeps the org chart (`ORG.md`), decision log (`decisions/`) and venture files (`ventures/`) up to date.

Every new session starts with the same rules, team, playbooks and the full record of work so far.

## Open it

1. Install Claude Code: see https://code.claude.com/docs (for example `npm install -g @anthropic-ai/claude-code`, or the native installer from the docs).
2. Unzip `venture-studio.zip`, then in a terminal:
   ```bash
   cd venture-studio
   claude
   ```
3. Say hello. The CEO will summarise where things stand and propose the next step.

Tip: run `/agents` inside Claude Code to see the team, and `/memory` to see the loaded `CLAUDE.md`.

## Back up to a private GitHub repo

The folder is already a git repository with one local commit (no remote). To back it up:

1. On GitHub, create a **new private repository** named `venture-studio` (no README, no .gitignore, so it starts empty).
2. In the folder:
   ```bash
   git remote add origin git@github.com:<your-username>/venture-studio.git   # or the https:// URL
   git push -u origin main
   ```
3. After later sessions: `git add -A && git commit -m "Update" && git push`. You can also ask the CEO to commit; it will ask before pushing.

Never commit secrets (API keys, Razorpay/Meta tokens). `.gitignore` already excludes `.env*` and `*.local.*` files.

## Start a cloud session from the repo

Once the repo is on GitHub:
1. Go to https://claude.ai/code and connect your GitHub account (install the Claude GitHub app on the `venture-studio` repo when asked).
2. Choose the `venture-studio` repository and start a session. The cloud session reads the same `CLAUDE.md`, agents and skills.
3. Changes made in the cloud are pushed to a branch; pull them on your computer with `git pull`.

## Layout

| Path | What |
|---|---|
| `CLAUDE.md` | CEO operating manual (loaded every session) |
| `ORG.md` | Org chart, remits, assignments, status |
| `.claude/agents/` | Team: chief-of-staff, recruiter, developer, marketing-lead, finance-analyst |
| `.claude/skills/` | Expert skills + `SOURCES.md` (provenance and licences) |
| `playbooks/smoke-test.md` | The studio's demand-validation method |
| `ventures/` | One folder per venture: `BRIEF.md`, `finance/`, `landing/`, `marketing/` |
| `decisions/` | Dated decision log |

## Licences

Skills in `.claude/skills/` keep their original licences: marketing skills are MIT (Corey Haines, see `.claude/skills/LICENSE-marketingskills`); `frontend-design` is from anthropics/skills (see `.claude/skills/frontend-design/LICENSE.txt`). See `.claude/skills/SOURCES.md`.

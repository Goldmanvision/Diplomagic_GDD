---
Title: Handoff Validation — Workflow Guide
Department: Mail
Codename: Postmaster
Date: 2025-08-17
Status: Active
---

# What it does
- Runs on PRs, pushes to `main`, daily cron, or manual dispatch.
- Diffs changed `.md` files excluding `Archive/` and `Backups/`.
- Applies Handoff gates G1–G6 and writes a Markdown report to `ops/reports/`.
- On PRs, posts the report as a comment and uploads it as an artifact.

# Gates
- **G1 Metadata**: `Department:`, `Codename:`, `Date:` present.
- **G2 ASCII-safe**: File path matches `[A-Za-z0-9_./-]+`.
- **G3 Scope/Deps**: Contains “Scope” and either “Inputs” or “Dependencies”.
- **G4 Blockers**: Has a “Blockers” section.
- **G5 Dept content**: Heuristics by path (`narrative/`, `ops/steam/`, `research/`, `departments/qa-ux/`).
- **G6 Sign-offs**: Mentions “Sign-off” or “Owner” lines.

# Review steps
1. Open the PR. Look for the “Handoff Validation Report” comment.
2. If any FAIL, fix or document a waiver in the PR body.
3. Ensure `DECISIONS.md` and `CHANGELOG.md` updates are present or queued.

# Manual run
- Actions tab → “Handoff Validate” → Run workflow.

# Local fallback
```bash
git fetch origin main
BASE=$(git merge-base HEAD origin/main)
git diff --name-only "$BASE" HEAD -- '*.md' ':!Archive/*' ':!Backups/*'
```

# Maintainers
- Owner: Postmaster
- Reviewers: Storymaster, Stationmaster, Taxonomist, Archivist

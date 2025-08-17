---
Title: PR Review Checklist — Freeze Track (SG-20250817 + Plan A)
Department: Mail
Codename: Postmaster
Date: 2025-08-17
Status: Use for PR {"freeze-track-batch-20250817"}
---

# Scope
Validate the Freeze Track batch PR for narrative freeze readiness.

# Identify
- Branch: `freeze-track-batch-20250817`
- Title contains: “SG-20250817” and “Plan A”
- Files touched (expected):
  - `narrative/scenes/scene_ids_prologue_ch1.md`
  - `narrative/reports/ch1_pacing_vs_spawns_20250819.md`
  - `data/spawn/spawn_tables_prologue_ch1.md`
  - `ops/steam/depot_branch_map_20250819.md`
  - `ops/steam/store_asset_checklist_20250819.md`
  - `research/refs/refs_seed_1994.md`
  - `departments/qa-ux/templates/bug-report.md`
  - `departments/qa-ux/templates/playtest-survey.md`
  - `departments/qa-ux/templates/severity-matrix.md`
  - `DECISIONS.md`, `CHANGELOG.md`

# Gates (G1–G6)
- **G1 Metadata**: Each `.md` has `Department`, `Codename`, `Date`.  
- **G2 ASCII-safe**: Paths and filenames match `[A-Za-z0-9._\/-]+`.
- **G3 Scope/Deps**: Each has Scope and inputs or dependencies.  
- **G4 Blockers**: Section present; empty uses “none”.  
- **G5 Dept content**: File-specific criteria below.  
- **G6 Sign-offs**: “Owner” and “Postmaster” present or handled in PR body.

# File-specific checks (G5)
- `scene_ids_prologue_ch1.md`
  - IDs match format `PRO-##`, `CH1-##`; names ASCII.
  - Stable after 2025-08-19 unless Suit override.
- `ch1_pacing_vs_spawns_20250819.md`
  - Contains **SG-20250817** rule block and references scene IDs.  
  - Pacing caps: Prologue ≤2 combats; Ch1 ≤3; spectral full ≤1.
- `spawn_tables_prologue_ch1.md`
  - Has `scene_id` column; uses IDs from the registry.  
  - Spectral “full” limited to ≤1 per chapter.
- `depot_branch_map_20250819.md`
  - **Plan A only**: Windows 10/11 x64; Deck via Proton.  
  - Notes `proton-qa` tag on beta.
- `store_asset_checklist_20250819.md`
  - “TBC” dimension fields present; crop constraints noted.
- `refs_seed_1994.md`
  - “TBD” URL placeholders flagged; scans path `/research/refs/scans/` used.
- QA templates
  - Present under `/departments/qa-ux/templates/` and labeled “Template”.

# Quick commands (optional)
```bash
# ASCII-safe paths
git diff --name-only origin/main...HEAD | grep -E -v '^[A-Za-z0-9_./-]+$' && echo "Non-ASCII found"

# SG-20250817 present
grep -Rin "SG-20250817" narrative/reports/

# scene_id references
grep -Rin "PRO-" narrative/ data/spawn | head
grep -Rin "CH1-" narrative/ data/spawn | head
```

# Acceptance
- All gates PASS or waivers documented in PR description.
- Narrative, Taxonomist, Stationmaster acks on their items.
- `DECISIONS.md` and `CHANGELOG.md` updated in the same PR or queued immediately after.

# Reviewer sign-off
- Storymaster: ___  Date: ___  
- Taxonomist: ___  Date: ___  
- Stationmaster: ___  Date: ___  
- Postmaster: ___  Date: ___

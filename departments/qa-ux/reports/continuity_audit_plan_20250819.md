---
Title: Continuity Audit Plan — Prologue & CH1
Department: QA & UX
Codename: Exterminator
Owner: QA Lead
Reviewer: Postmaster; Storymaster
Date: 2025-08-17
Status: Ready
---

# Scope
Re‑run continuity audit after Narrative and Adversary submissions land on `main`.

# Inputs
- `narrative/scenes/scene_ids_prologue_ch1.md`
- `narrative/reports/ch1_pacing_vs_spawns_20250819.md`
- `data/spawn/spawn_tables_prologue_ch1.md`

# Checks (mapped to Gate Map)
- G1: Playbook/Outline links resolve.
- G2: 1994/1989 terms validated against `research/checks/period_check_core_terms_1994.md`.
- G3: Goals, beats, assets, risks present.
- G4: Branch coverage and failstates present and cross‑referenced.
- G5: UI strings and controls listed.
- G6: Continuity clean: no MissingFields, Duplicate, or Conflict; seeds→payoffs valid; SG rules met.

# Outputs
- `/continuity_issues.csv` — master list at repo root.
- `/departments/qa-ux/reports/continuity_audit_20250819.md` — narrative notes.
- Diff summary embedded at top of the report.

# Sign‑off
Owner (QA): ___  Postmaster: ___  Date: ___

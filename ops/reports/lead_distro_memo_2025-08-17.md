---
Title: Lead Distro Memo — Narrative Freeze Track
Department: Mail
Codename: Postmaster
Date: 2025-08-17
Status: Send
---

# Summary
Narrative freeze target: 2025-08-24. SG-20250817 approved. Plan A OS: Windows 10/11 x64 + Steam Deck via Proton.

# Double-Confirm protocol (multi-file work)
1) Warning: risk of UI reset or token cap. Proceed? y/n
2) Confirm: this is your choice. Proceed now? y/n

# Actions by department

## Narrative & Canon — Storymaster
- Publish canonical scene IDs.
  - Download: /narrative_scene_ids_prologue_ch1.md → target `/narrative/scenes/` as `scene_ids_prologue_ch1.md`
- Review pacing with SG-20250817 applied; keep caps (Prologue <=2 combats; Ch1 <=3; spectral full <=1).
  - Download: /narrative/reports/ch1_pacing_vs_spawns_20250819.md → target `/narrative/reports/`
- Reply: ACK with any scene_id changes.

## Authenticity & Research — Archivist
- Replace TBD URLs and upload scans.
  - Download: /research/refs/refs_seed_1994.md → target `/research/refs/` (overwrite)
  - Scans dir: `/research/refs/scans/`
- Reply: ACK when complete; list conflicts if dates disagree.

## QA & UX — Exterminator
- Use seeded templates; prepare continuity telemetry.
  - Downloads: 
    - /departments/qa-ux/templates/bug-report.md → `/departments/qa-ux/templates/`
    - /departments/qa-ux/templates/playtest-survey.md → `/departments/qa-ux/templates/`
    - /departments/qa-ux/templates/severity-matrix.md → `/departments/qa-ux/templates/`
- After narrative batch, re-run continuity audit.

## Steam Operations — Stationmaster
- Plan A only. Finalize depot map and store checklist. Add Deck QA tag on beta.
  - Downloads:
    - /ops/steam/depot_branch_map_20250819.md → `/ops/steam/` (overwrite)
    - /ops/steam/store_asset_checklist_20250819.md → `/ops/steam/` (overwrite)
- Fill Steamworks dimensions and crop constraints.

## Adversary & NPC Systems — Taxonomist
- Freeze new enemy classes. Bind spawns to scene_ids.
  - Download: /data/spawn/spawn_tables_prologue_ch1.md → `/data/spawn/` (overwrite)
  - Download: /departments/adversary-npc-systems/verification/spawn-scene-bindings-notes-20250819.md → `/departments/adversary-npc-systems/verification/`

## Mail — Postmaster
- Logs updated.
  - /DECISIONS.md → `/` (overwrite)
  - /CHANGELOG.md → `/` (overwrite)
- Pack for suit:
  - /ops/reports/mail_outputs_pack_2025-08-17.zip → `/ops/reports/`

# SG-20250817 (for reference)
- Flicker: clue_threshold >= 1 and low-light present.
- Full: clue_threshold >= 2 and darkness condition. Max 1 per chapter.

# Reply format
- Dept: ACK / questions
- Risks: none | list
- ETA changes: none | new date

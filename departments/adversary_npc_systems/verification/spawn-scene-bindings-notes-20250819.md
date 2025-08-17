---
Title: Spawn ↔ Scene Bindings — Notes
Department: Adversary & NPC Systems
Codename: Taxonomist
Owner: Taxonomist
Reviewer: Storymaster; Postmaster
Date: 2025-08-17
Type: Verification Notes
Status: Standby
---

# Scope
Prepare verification notes to bind spawn table rows to narrative `scene_id`s for Prologue and Chapter 1. No new enemy classes until narrative lock.

# Inputs
- data/spawn/spawn_tables_prologue_ch1.md
- data/statblocks/schema_statblock.md
- narrative/reports/ch1_pacing_vs_spawns_20250819.md

# Scene ID scheme (pending Storymaster)
Proposed format: `PRO-01..n`, `CH1-01..n`. Final list required from Narrative.

# Provisional bindings (to be confirmed)
Table | d6 | Result | ADV IDs | Proposed scene_id(s) | Cap | Notes
--- | --- | --- | --- | --- | --- | ---
Prologue — Street | 1 | 2× Occult Cultists | ADV-0001 | PRO-01 | 1 | Light intro
Prologue — Street | 2 | 1× New Kadathi Cultist | ADV-0003 | PRO-01 | 1 | Ranged harass
Prologue — Street | 3 | 1× Mind‑Swapped Civilian | ADV-0002 | PRO-02 | 1 | Non‑lethal branch
Prologue — Street | 4 | Spectral flicker | ADV-0004 | PRO-02 | 1 | Tease only
Prologue — Basement | 1–2 | 2× Cultists | ADV-0001 | PRO-02 | 1 | Closed space
Prologue — Basement | 5 | 1× Mind‑Swapped Civilian | ADV-0002 | PRO-02 | 1 | Interruption
Prologue — Basement | 6 | 1× Spectral full | ADV-0004 | PRO-02 | 1 | Darkness gate

Chapter 1 — Alley | 1 | 2× Cultists | ADV-0001 | CH1-01 | 1 | Light
Chapter 1 — Alley | 2 | 1× Cultist + 1× Kadathi | ADV-0001, ADV-0003 | CH1-01 | 1 | Mixed
Chapter 1 — Alley | 3 | 1× Mind‑Swapped Civilian | ADV-0002 | CH1-02 | 1 | Conversation beat
Chapter 1 — Alley | 4 | Spectral flicker | ADV-0004 | CH1-02 | 1 | Tease only
Chapter 1 — Warehouse | 1 | 2× Cultists + 1× Kadathi | ADV-0001, ADV-0003 | CH1-03 | 1 | Medium
Chapter 1 — Warehouse | 2 | 1× Spectral full | ADV-0004 | CH1-03 | 1 | Boss‑like moment
Chapter 1 — Warehouse | 3 | 1× Mind‑Swapped Civilian | ADV-0002 | CH1-03 | 1 | Quiet tension

# Caps and pacing
- Prologue: ≤2 combats total; ≥1 non‑lethal engagement.  
- Chapter 1: ≤3 combats total; spectral full ≤1.

# QA checks
- IDs resolve to files in data/statblocks/.  
- Period‑correct equipment only.  
- No anachronistic terminology per research/checks/period_check_core_terms_1994.md.

# Blockers
- Final `scene_id` list from Narrative.
- Spectral gating rule confirmation.

# Actions
1) Storymaster: publish scene_id list for Prologue and Ch1.  
2) Taxonomist: add `scene_id` column to spawn tables and fill per binding.  
3) QA: verify spawn IDs cross‑link correctly.  
4) Archivist: re‑validate props per scene.

# Sign‑off
Owner (Taxonomist): ___  Date: ___  
Storymaster: ___  Date: ___  
Postmaster: ___  Date: ___

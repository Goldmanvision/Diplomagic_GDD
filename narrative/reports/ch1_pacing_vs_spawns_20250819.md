---
Title: Chapter 1 — Pacing vs Spawn Tables
Department: Narrative & Canon
Codename: Storymaster
Owner: Storymaster
Reviewer: Postmaster; Archivist; Taxonomist
Date: 2025-08-17
Due: 2025-08-19
Type: Validation Report
Status: Draft
---

# Scope
Validate Chapter 1 encounter pacing against current spawn tables. Identify deltas and propose fixes. 1994/1989 accuracy enforced.

# Inputs
- data/spawn/spawn_tables_prologue_ch1.md
- narrative/playbook.md  (source: DIPLOMAGIC Narrative Playbook.pdf)
- narrative/outline_2025.md  (source: Diplomagic Outline 2025.pdf)

# Summary
Prologue and Chapter 1 spawn tables define four adversary types (cultist, New Kadathi cultist, mind‑swapped civilian, spectral entity) with d6‑driven appearances across street/alley/interior/warehouse contexts. Pacing must support short scenes, low HP bloat, and investigative beats between conflicts.

# Encounter baseline (from spawn tables)
## Prologue
- Street: d6 1–4 can trigger 1–2 light encounters; spectral flicker on 4.
- Interior (basement): up to one encounter; spectral on 6 only.
- **Recommendation**: Max 2 encounters across Prologue. At least 1 non‑lethal resolution (mind‑swapped civilian).

## Chapter 1
- Alley: light to medium skirmishes; spectral flicker on 4.
- Warehouse: medium encounter on 1–2; otherwise quiet.
- **Recommendation**: 3 encounters total across Ch1, default order → light (alley) → investigation → medium (warehouse) → optional spectral tease.

# Deltas
1) **Scene identifiers missing** in Outline/Playbook mirrors. No canonical `scene_id` to bind spawn rows.
2) **Non‑combat pacing beats** not yet codified (investigation, dialogue, travel).
3) **Spectral entity gating** undefined. Flicker vs full manifestation criteria not tied to story beats.
4) **Fail‑forward paths** not mapped for missed morale checks or retreats.

# Proposed fixes
F1) Establish scene_id scheme: `PRO-01..n`, `CH1-01..n`.  
F2) Bind each spawn row to one or more scene_ids with weight and cap.

Example binding
```
PRO-01 street-intro: d6 1→ cultists x2; 2→ kadathi x1; 3→ mind-swapped x1; 4→ spectral flicker
PRO-02 basement-search: d6 1–2→ cultists x2; 5→ mind-swapped x1; 6→ spectral full
CH1-01 alley-sweep: d6 1→ cultists x2; 2→ mixed x2; 3→ mind-swapped x1; 4→ spectral flicker
CH1-03 warehouse-check: d6 1→ cultists x2 + kadathi x1; 2→ spectral full; 3→ mind-swapped x1
```
Caps: Prologue ≤2 total combats; Ch1 ≤3 total combats. Spectral full ≤1 per chapter.

F3) Add **non‑combat beats** per scene: clue discovery, witness interview, travel, restock.  
F4) Add **gating rule**: spectral full requires prior clue threshold ≥2 and darkness condition.  
F5) Define **fail‑forward**: on retreat or failed morale, drop clue stub or escalate later rumor.

# Validation
- HP and damage values remain modest per schema.  
- Weapons and props constrained to 1994 availability.  
- Spawn table IDs referenced: ADV-0001, ADV-0002, ADV-0003, ADV-0004.

# Gate check (this report)
- G1 Metadata: PASS
- G2 ASCII-safe path/name: PASS
- G3 Scope/Deps: PASS
- G4 Blockers listed: PASS
- G5 Dept content present: PASS (pacing plan + binding)
- G6 Sign-offs: PENDING (Storymaster, Postmaster)

# Blockers
- Need approved scene_id list from Storymaster to finalize binding.
- Need confirmation on spectral gating from Narrative.
- Optional: Outline scene durations to tune encounter weights.

# Actions
1) Storymaster: publish `scene_id` list for Prologue and Ch1.  
2) Taxonomist: add `scene_id` column to spawn tables and fill per binding.  
3) Archivist: sanity check period props in Ch1 scenes.  
4) QA&UX: define pacing telemetry (encounters per hour, time‑to‑first‑clue).

# Sign-off
Owner (Storymaster): ___  Date: ___  
Postmaster: ___  Date: ___

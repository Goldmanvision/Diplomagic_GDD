# [SEC-04-LOOPS] Core Gameplay Loops
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-01-FRONT` — Front Matter & Executive Summary
- `SEC-03-NARRATIVE` — Narrative
- `SEC-05-SYSTEMS` — Systems & Mechanics
- `SEC-06-WORLD` — World, Levels, & Content

## **4.1 Overview**

Loops connect investigation, stealth/combat, and narrative progression. Avery \= procedural agency within ROE. Clara \= survival agency under scarcity. Both feed the shared world state and ending matrix.

## **4.2 Moment‑to‑Moment Loop**

Primary verbs: observe, collect, infer, act, record, move.

[Observe] → [Collect Evidence] → [Evaluate Risk] → [Act (Stealth/Combat/Dialogue)]

         ↘                                          ↗

           [Record in FieldPad] ← [Update World/AI State] ← [Relocate]

**Guardrails**

* Evidence first. Action without intel raises risk and cost.

* Devices are the UI. Non‑diegetic assists stay minimal.

**Success Criteria**

* Player logs evidence in ≥80% of missions before major actions.

## **4.3 Mission Loop (POV‑specific)**

**Avery (FBI)**

[Brief/Case Intake] → [Legal Prep (warrant/ROE)] → [Travel/Loadout]

      → [Recon] → {Branch: Infiltrate | Knock/Breach} → [Secure/Arrest]

      → [Scene Processing] → [Debrief/Casefile]

**Clara (Survival)**

[Immediate Need (Protect Reddy)] → [Scavenge/Route Plan] → [Infiltrate/Bypass]

      → [Avoid/Disable Threat] → [Extract] → [Recuperate/Journal]

**Checkpoints**

* Autosave at **Brief**, **Branch**, **Outcome**. Manual save outside combat.

## **4.4 Meta‑Progression**

* **Caseboard (shared):** pins, threads, suspects; reflects cross‑POV state.

* **Devices:** apps unlock by story beats; upgrades change verbs (ex: TAPLINE → passive scan → targeted decode).

* **Skills:** separate tracks; no shared XP. Avery favors procedure/tactics. Clara favors stealth/improvisation.

* **Reputation/Heat:** systemic response to arrests, kills, noise.

## **4.5 Evidence System**

* **Tiers:** A (forensic), B (eyewitness/analysis), C (circumstantial).

* **Quality score:** affects dialog gates, warrant success, and combat modifiers.

* **Chain of custody (Avery):** must bag, tag, and log. Breaks invalidate A‑tier gates.

* **Reddy care (Clara):** stress and noise modify encounter density.

* Outcomes write to the **Consequences Matrix** used by Epilogue.

## **4.6 Stealth & Combat Loops**

**Stealth**

[Shadow/Noise Mgmt] → [Intel Peek] → [Path/Create Distraction] → [Bypass/Isolate]

        ↖——————————————————————[Break LOS]/[Hide]———————————————————————↗

**Avery Combat**: cover, decoupled aiming, arrests \> lethal. Suppression and team calls supported by MEDSTAT.  
 **Clara Combat**: last resort. Limited firearms, improvised traps, sprint windows. Fewer bullets, more routes.

## **4.7 Failure & Recovery**

* **Soft fail:** blown stealth raises heat and spawns reinforcements; fallback to escape routes.

* **Hard fail:** incapacitation → checkpoint reload; injury debuffs persist until treated in MEDSTAT.

* **Case fail‑forward:** poor evidence locks some branches but preserves continuity; alternate endings remain reachable.

## **4.8 Difficulty & Pacing**

* **Dynamic pressure:** AI alertness and patrol density scale with noise/heat.

* **Assist options:** aim assist, slower clue timers, enhanced device hints.

* **Encounter budgets:** readable silhouettes, limited simultaneous threats.

## **4.9 UI Touchpoints (Devices)**

* **FieldPad:** capture photos, tag, annotate, chain‑of‑custody, caseboard.

* **TAPLINE:** scan bands, log intercepts, decode, triangulate.

* **MEDSTAT:** health states, status effects, team telemetry, triage.

## **4.10 Telemetry Targets (for tuning)**

* Evidence logged before breach ≥70%.

* Arrest:kill ratio for Avery ≥2:1 in mid‑game.

* Clara stealth resolution rate ≥60%.

* Average mission length 25–40 min on Standard.

## **4.11 Content Hooks (Templates)**

* **Recon → Infiltrate → Extract**

* **Stakeout → Warrant → Breach**

* **Escort/Protect (Reddy) → Diversion → Evade**

## **4.12 Accessibility Notes**

* Color‑blind safe palettes in device UIs.

* Subtitles by default.

* Remappable inputs.

* Toggle for reduced camera shake and flashing.

## **4.13 Deliverables**

* Loop diagrams (final art).

* Caseboard schema and save‑state spec.

* KPI dashboard definitions.

## **4.14 Approvals**

On approval: archive to MASTER as `[SEC-04-LOOPS] v0.1` and update manifest. Next section: **SEC‑05 Systems & Mechanics**.

# **Patch Instructions for Existing MASTER — SEC-05**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-05-SYSTEMS |` and replace the entire line with:

`| SEC-05-SYSTEMS | Systems and mechanics | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

# SEC-04 — CH6 Lore: Splinter of Azathoth
Repo dir: /Patches

## Provenance (diegetic)
- **AEC relic** boxed during Cold War anomaly study; archived under D‑LAMP.  
- **DOE era:** custody drift; Order re‑discovers object in the 1980s.  
- **Cult doctrine:** splinter = “breath of the Sleeper”; chant carries line “the stars are right tonight.”

## Physical
- Obelisk shard in suspension gimbal; emits low‑band hum; distorts geometry at surge.

## Effects
- **Spatial fold:** corridors loop; doors re‑map.  
- **Perceptual drift:** time stamps desync; Polaroid confirms truth.  
- **Biological:** necrotic urge (zombies), predatory flock (night gaunts).

## Handling
- No direct touch; use pole clamps.  
- Shield/Valve cycle stabilizes; charges sever link; photos/samples feed Black File.

## Evidence hooks (1994)
- Typed memos, stamped crates, logbook notations; Polaroid plates of gimbal.

## Redactions
- Never quote chants beyond ambient phrase. No modern tech references.

# Inline Patch — SEC-04 CH1 Integration
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑04 — CH1 Loops Integration

### 4.Y Chapter 1 Integration
Map CH1 objectives to loops with gates and outputs.

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Emit events per `Trackers/QATelemetry_CH1.md`.

## END PATCH

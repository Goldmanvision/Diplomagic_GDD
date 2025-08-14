# Inline Patch — SEC-04 Loops: Prologues Hook-in
Version: v0.1 — 2025-08-14 10:57:09 UTC
Owner: Nick Goldman
Paste into SEC-04 under Core Loops (recommended new subheading).

---
## BEGIN PATCH: SEC-04 — Prologue Tutorials Integration

### 4.X Prologues Integration (0A/0B)
Wire tutorial objectives into core loops with clear gates and outputs.

**IDs**
- OBJ-0A-CHALLENGE, OBJ-0A-CUFF, OBJ-0A-SEARCH, OBJ-0A-CUSTODY, OBJ-0A-RANGE, OBJ-0A-NONL, OBJ-0A-ESCORT, OBJ-0A-DEBRIEF
- OBJ-0B-VITALS, OBJ-0B-CARE, OBJ-0B-POV, OBJ-0B-PIN, OBJ-0B-WRAP
- TUT-* = on-screen prompts (≤14 chars) from TutorialCopy docs

**Loop mapping**
| Loop | Tutorial step | IDs | Gate | Output flags/events |
|---|---|---|---|---|
| Investigate→Act→Record | 0A custody | OBJ-0A-CUSTODY | Locker handoff confirm | `custody_complete=true` |
| Arrest loop | 0A contact | OBJ-0A-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |
| Combat practice | 0A range | OBJ-0A-RANGE | `range_dual_done && range_decouple_done` | `range_score` |
| Non‑lethal | 0A takedown/escort | OBJ-0A-NONL/ESCORT | `nonlethal_ammo_trained==true` | `nonlethal_takedown_done`, `escort_done` |
| Caregiving | 0B vitals/care | OBJ-0B-VITALS/CARE | `vitals_logged==3` | `care_tasks_done` |
| Narrative beat | 0B POV | OBJ-0B-POV | none | `reddy_pov_played` |
| Discovery | 0B pin | OBJ-0B-PIN | none | `brightstar_pin_found` |

**Award gate**
- Hauser pistol award path unlocks only if `range_score ≥ 90` and `roe_violations == 0`.

**Telemetry**
Emit events per QATelemetry trackers. Persist flags to Systems (SEC‑05).

## END PATCH

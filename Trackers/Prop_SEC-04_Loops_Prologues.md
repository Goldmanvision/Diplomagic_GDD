# Propagation — SEC-04 Loops: Prologues Hook-in
Version: v0.1
Date: 2025-08-14 10:49:18 UTC
Owner: Nick Goldman
Scope: Wire 0A/0B tutorials into Core Loops. IDs, gates, and triggers.

## IDs
- OBJ-0A-CHALLENGE, OBJ-0A-CUFF, OBJ-0A-SEARCH, OBJ-0A-CUSTODY, OBJ-0A-RANGE, OBJ-0A-NONL, OBJ-0A-ESCORT, OBJ-0A-DEBRIEF
- OBJ-0B-VITALS, OBJ-0B-CARE, OBJ-0B-POV, OBJ-0B-PIN, OBJ-0B-WRAP
- TUT-* = prompts (≤14 chars) from TutorialCopy files
- TRG-* = trigger volumes/actors

## Loop mapping
| Loop | 0A / 0B step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | 0A custody | OBJ-0A-CUSTODY | TRG-LOCKER handoff | `custody_complete=true` |
| Arrest loop | 0A contact | OBJ-0A-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |
| Combat practice | 0A range | OBJ-0A-RANGE | `range_dual_done && range_decouple_done` | `range_score` |
| Non-lethal | 0A takedown/escort | OBJ-0A-NONL/ESCORT | `nonlethal_ammo_trained` | `nonlethal_takedown_done`, `escort_done` |
| Caregiving | 0B vitals/care | OBJ-0B-VITALS/CARE | `vitals_logged==3` | `care_tasks_done` |
| Narrative beat | 0B POV | OBJ-0B-POV | none | `reddy_pov_played` |
| Discovery | 0B pin | OBJ-0B-PIN | none | `brightstar_pin_found` |

## Gates
- G-0A-AWARD: `score≥90 && roe_violations==0` → unlock Hauser pistol award path.
- G-0A-ESCORT: `nonlethal_ammo_trained==true` → escort drill unlocks.
- G-0B-WRAP: `vitals_logged==3 && reddy_pov_played==true`.

## Triggers (examples)
- TRG-CHALLENGE: cone + proximity; TRG-CUFF: behind-back socket; TRG-SEARCH: item sockets.
- TRG-CAMERA: camera actor; TRG-LOCKER: window overlap + UI confirm.
- TRG-RANGE: lane start; TRG-DUAL/DECOUPLE: UI toggles.
- TRG-POV: doorframe spline; TRG-PIN: table inspect hotspot.

## Outputs → Systems
- Telemetry: per QATelemetry files.
- Flags: `hauser_pistol_awarded`, `brightstar_pin_found`, `cult_symbol_link_active` (derived later).
- Score: `range_score` int; `roe_violations` int.

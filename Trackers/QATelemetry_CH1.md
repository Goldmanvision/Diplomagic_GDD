# CH1 — “Simple Curiosity” QA + Telemetry Matrix
Version: v0.1
Date: 2025-08-14 11:57:29 UTC
Owner: Nick Goldman
Scope: Coverage for Clara Brightstar leg and Avery roadside stop.

## Entry/Exit
**Entry:** Build boots; maps load; smoke pass.  
**Exit:** P1=0, P2≤5; perf within SEC‑11; crash‑free P90 ≥ target.  
Clara: `medstat_upgrade_card_inserted==true`; `ch1_clara_complete`.  
Avery: `custody_complete==true`; `ch1_avery_complete`.

## Suites
- TS-UI-CH1: prompts ≤14 chars; subtitles; remap; UI scale 0.85–1.50.
- TS-CLARA-NOTES: find card → insert → toast; CaseNote created; flags set.
- TS-CLARA-STEALTH: patrol cone pass; admonish on spot; resume.
- TS-CLARA-CARE: simple care task; optional path recorded.
- TS-AVERY-ROE: challenge→cuff→search; unjustified shot admonish; continue.
- TS-AVERY-CUSTODY: photo→bag→tag→log; mobile locker handoff.
- TS-PERF: perf spots CSVs (foyer, storage hall, exit; roadside stop).
- TS-AX: high‑contrast skins; non‑color cues; hold↔press.

## Telemetry Events
Common fields: `ts`, `build_id`, `session_id`, `map`, `player_pov`, `diff`.

Clara leg
- `medstat_upgrade_card_found` (bool)  
- `medstat_upgrade_card_inserted` (bool)  
- `pin_auto_log_created` (bool)  
- `stealth_pass_bool` (bool)  
- `care_task_done_bool` (bool)  
- `ch1_clara_complete` (time_s)

Avery leg
- `arrest_performed` (suspect_id, nonlethal_bool)  
- `custody_complete` (photo, bag, tag, log, locker)  
- `roe_violations` (count)  
- `debrief_viewed` (bool)  
- `ch1_avery_complete` (time_s)

## AX Matrix
- Subtitles ON w/ tags. Pass if visible by default.
- UI scale extremes OK. No clipping on MEDSTAT panels.
- High‑contrast theme persists.
- No color‑only cues.

## Perf & Stability
- GPU ≤ 14 ms @1080p mid tier each perf spot; med/95p logged.
- Soak 2h; memory growth <5%; save/load loop.

## Evidence to capture
- Screens: card insert toast, CaseNote UI, custody checklist.  
- Videos: 20–30 s stealth pass; 20–30 s ROE stop.  
- CSVs: perf med/95p for all spots.

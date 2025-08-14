# 0B — Clara Prologue Beat→Objective Walkthrough
Version: v0.1
Date: 20250814T0941Z
Owner: Nick Goldman

## Objectives
- Teach MEDSTAT vitals and logging.
- Teach light caregiving loop.
- Stage Reddy-POV beat.
- Place Brightstar pin discovery.

## Flow
1) Arrival via buzzer/landline → greet Betsy.
2) MEDSTAT vitals: pulse-ox → BP → temperature.
3) Care tasks: tea, pills, tidy.
4) Reddy-POV beat; knife unseen by Clara.
5) Discover Brightstar pin; note on paper chart.
6) Schedule follow-up via landline note.

## Beats → Objectives
| Beat | Objective | Success | Failure | Notes |
|---|---|---|---|---|
| Arrival | **BUZZER**/**CALL** | Door opens | Locked out | Dialogue tags |
| Intro | **GREET** | Betsy calms | Escalates | Soft timeout |
| Pulse-ox | **P-OX** | Stable reading | Timeout | Retry tip |
| BP cuff | **BP** | Two readings | Fault | Re-seat cuff |
| Temp | **TEMP** | Reading logged | Wrong input | Hint |
| Pills | **PILLS** | Organizer set | Wrong slot | Undo allowed |
| Tea | **TEA** | Cup delivered | Spilled | Wipe mini-step |
| Tidy | **TIDY** | Table clear | Miss item | Optional |
| Reddy POV | **SWAP POV** | Cut plays | Skipped | Rewatchable |
| Pin | **PIN FOUND** | Note on paper | Ignored | Flag false |
| Schedule | **CALL** | Date written | None | Landline only |

## Checkpoints
- CP1 Entry complete.
- CP2 Vitals complete.
- CP3 Care complete.
- CP4 Reddy-POV played.
- CP5 Pin logged.
- CP6 Follow-up noted.

## Fail/Reset
- Repeated rough actions → soft admonish, no hard fail.
- Optional later: outside walk test → if used, failure flag = job lost (not here).

## UI prompts (≤14 chars)
- BUZZER
- CALL
- GREET
- P-OX
- BP
- TEMP
- PILLS
- TEA
- TIDY
- SWAP POV
- PIN FOUND

## Telemetry
- prologue_clara_complete
- vitals_logged
- care_tasks_done
- reddy_pov_played
- brightstar_pin_found

## AX checks
- Subtitles default ON; speaker tags.
- UI scale 0.85–1.50 no clip.
- High-contrast skin OK.

## Period
- 1994. **MEDSTAT handheld + RF wrist-band only.** No FieldPad/TAPLINE.

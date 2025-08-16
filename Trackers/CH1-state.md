# CH1 State Tracker — DIPLOMAGIC

## Dependencies
- `PROLOGUE_COMPLETE == TRUE` gates CH1 activation.

## Core Flags
- `CH1_ACTIVE` (bool), `CH1_COMPLETE` (bool).
- Clara:
  - `CLARA_NOISE_LEVEL` (int, running).
  - `REDDY_CRYING` (bool).
  - `CLARA_EXITED` (bool).
- Avery:
  - `AVERY_ARRESTS` (int ≥ 0).
  - `AVERY_KILLS` (int ≥ 0).
  - `EVIDENCE_COUNT` (int ≥ 0).
  - `GROMLEY_STATUS` ∈ {ARRESTED, KILLED, ESCAPED} (exactly one).

## Scoring (TBD thresholds)
- `FS_CLARA_NOISE_MAX = TBD`
- `FS_AVERY_KILL_PENALTY = TBD`
- `FS_AVERY_ARREST_BONUS = TBD`
- `FS_EVIDENCE_BONUS_PER = TBD`

## Validation Invariants
- `CH1_ACTIVE == TRUE` implies `PROLOGUE_COMPLETE == TRUE`.
- Exactly one of `GROMLEY_STATUS` is set when `CH1_COMPLETE == TRUE`.
- `CLARA_EXITED == TRUE` before setting `CH1_COMPLETE`.
- Score deltas computed once per save for CH1.

## Outputs
- `CH1_SCORE_CLARA` (int), `CH1_SCORE_AVERY` (int), `CH1_SCORE_GLOBAL` (int)
- Forward tags: `GROMLEY_OUTCOME`, `CH1_EVIDENCE_LEVEL`

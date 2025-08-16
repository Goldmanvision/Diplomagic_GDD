# CH2 State Tracker — DIPLOMAGIC

## Dependencies
- Requires `CH1_COMPLETE==TRUE`.

## Core Flags
- `CH2_ACTIVE` (bool), `CH2_COMPLETE` (bool)
- Clara:
  - `SAFE_HARBOR` (bool)
  - `CLARA_RESOURCE_COUNT` (int)
  - `ROLODEX_CALL` (bool)
  - `REDDY_STATS_OK` (bool)
- Avery:
  - `SECURITY_CLEARANCE ∈ {NONE, LEVEL_X}`
  - `KRILL_CONTACT` (bool)
  - `ARCHIVE_ACCESS` (bool)
  - `AVERY_METHOD ∈ {ARREST, LETHAL}`

## Scoring (TBD thresholds)
- Clara: `ROLODEX_CALL_BONUS`, `REDDY_STATS_BONUS`
- Avery: `ARREST_BONUS`, `LETHAL_PENALTY`

## Validation Invariants
- On `CH2_COMPLETE==TRUE`: must have `SAFE_HARBOR==TRUE` and `SECURITY_CLEARANCE==LEVEL_X`.
- If `AVERY_METHOD==LETHAL`, penalize score.
- Enum fields must have exactly one value set.

## Outputs
- `CH2_SCORE_CLARA`, `CH2_SCORE_AVERY`, `CH2_SCORE_GLOBAL`

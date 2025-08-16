# EPILOGUE State Tracker — DIPLOMAGIC

## Dependencies
- `CH6_COMPLETE == TRUE` gates Epilogue entry.
- All required Ch.6 device nodes disabled or final boss resolved.

## Inputs to Final Score (canonical)
- Arrests vs. Kills delta (Avery-heavy weight).
- Rescues and Intel collected (Clara-weighted; global bonus).
- Reddy care statistics.
- Key Ch.5–6 choices (e.g., banish vs destroy Elder splinters).

## Core Flags
- `EPILOGUE_ACTIVE` (bool) — set when entering Epilogue.
- `NGP_UNLOCKED` (bool) — set if Final Score ≥ NG+ threshold or secret conditions met.
- `META_UNLOCKED` (bool) — set by hidden meta chain completion.
- `CLARA_GOOD` / `CLARA_BAD` (mutually exclusive).
- `AVERY_GOOD` / `AVERY_BAD` (mutually exclusive).

## Thresholds (tune in balancing pass)
- `FS_CLARA_GOOD_MIN = TBD`  # e.g., high rescues + Reddy care
- `FS_AVERY_GOOD_MIN = TBD`  # e.g., low kills + high arrests
- `FS_GLOBAL_GOOD_MIN = TBD` # combined minimum for overall “good world state”
- `FS_NG_PLUS_MIN = TBD`     # unlocks Azathoth dream variant
- `META_CHAIN_COMPLETE` (bool) — unlocks Meta ending

## Resolution Matrix
- If `FinalScore ≥ FS_GLOBAL_GOOD_MIN` → prefer **Good/Good** montage.
- Else evaluate per-character minima:
  - `FinalScore_Clara ≥ FS_CLARA_GOOD_MIN` → `CLARA_GOOD = TRUE` else BAD.
  - `FinalScore_Avery ≥ FS_AVERY_GOOD_MIN` → `AVERY_GOOD = TRUE` else BAD.
- Mixed outcomes allowed; apply combined montage rules:
  - `CLARA_GOOD + AVERY_GOOD` → Ambassador offer scene.
  - `CLARA_BAD + AVERY_GOOD` → Refugee status scene.
  - `CLARA_GOOD + AVERY_BAD` → Neutralize-Clara tension scene.
  - `CLARA_BAD + AVERY_BAD` → Dual dark-power montage.

## Variant Selection
- If `NGP_UNLOCKED` → append Azathoth stinger and enable NG+.
- If `META_UNLOCKED` → swap credits bridge to meta sequence.

## Validation
- CI must assert:
  - `CH6_COMPLETE` before Epilogue activation.
  - Exactly one of `CLARA_GOOD/CLARA_BAD` and `AVERY_GOOD/AVERY_BAD` true.
  - `EPILOGUE_ACTIVE` implies no open critical-path tasks.
  - Ending montage chosen is consistent with flags and thresholds.

## Outputs
- `EPILOGUE_ENDING_KEY` ∈ {CLARA_GOOD|BAD}×{AVERY_GOOD|BAD}
- `POSTGAME_WORLD_STATE` tags for free-roam population.

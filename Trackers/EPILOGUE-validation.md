# EPILOGUE — Validation Invariants

Scope: enforce narrative and state integrity for the Epilogue, derived from canon.

## Canon Endings (summary)
- Clara: **GOOD** → bestselling author; **BAD** → cult leader.
- Avery: **GOOD** → ambassador; **BAD** → cult enforcer.
- NG+ variants: Azathoth dream; Meta awareness.
- False endings: on failure, chaos, or exiting after warning.

## Required Gating
- `CH6_COMPLETE == TRUE` before `EPILOGUE_ACTIVE`.
- Exactly one of `CLARA_GOOD` / `CLARA_BAD` is `TRUE`.
- Exactly one of `AVERY_GOOD` / `AVERY_BAD` is `TRUE`.
- `NGP_UNLOCKED` only if `FinalScore >= FS_NG_PLUS_MIN` (or secret chain satisfied).
- `META_UNLOCKED` only if `META_CHAIN_COMPLETE == TRUE`.
- False endings must be mutually exclusive with the four main outcomes.

## Thresholds (to be tuned later)
- `FS_CLARA_GOOD_MIN = TBD`
- `FS_AVERY_GOOD_MIN = TBD`
- `FS_GLOBAL_GOOD_MIN = TBD`
- `FS_NG_PLUS_MIN = TBD`

## Outputs
- `EPILOGUE_ENDING_KEY` ∈ {CLARA_GOOD|BAD}×{AVERY_GOOD|BAD}
- `POSTGAME_WORLD_STATE` tags for free-roam population.

## Checklist
- [ ] `Trackers/EPILOGUE-state.md` includes the flags above and marks `GOOD/BAD` pairs as **mutually exclusive**.
- [ ] `Patches/EPILOGUE.md` contains a Beat Sheet and Ending Branches section matching the canon summary.
- [ ] Thresholds either have values or are explicitly `TBD` (advisory mode).

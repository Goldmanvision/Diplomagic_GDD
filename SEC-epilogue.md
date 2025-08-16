# SEC — Epilogue Narrative Validation Notes

Purpose: document non-functional rules the CI enforces for the Epilogue.

## Invariants
1. **Chapter gating** — Epilogue can activate only if `CH6_COMPLETE == TRUE`.
2. **Outcome exclusivity** — exactly one of `CLARA_GOOD/CLARA_BAD` and one of `AVERY_GOOD/AVERY_BAD` must be true.
3. **NG+ / Meta gating** — `NGP_UNLOCKED` requires `FS_NG_PLUS_MIN` (or secret route). `META_UNLOCKED` requires `META_CHAIN_COMPLETE`.
4. **False endings** — exclusive to their triggers; cannot co-exist with main four outcomes.
5. **Outputs** — set `EPILOGUE_ENDING_KEY` and `POSTGAME_WORLD_STATE` for postgame.

## Ops Guidance
- Thresholds may start as `TBD`; CI will warn but not fail until values are assigned.
- Keep all endings period-accurate to 1994 technology and media surfaces in delivery.
- Do not introduce mechanics in the Epilogue; resolve narrative and tally final score.

## Files
- `Patches/EPILOGUE.md`
- `Trackers/EPILOGUE-state.md`
- `Trackers/EPILOGUE-validation.md`
- `.github/workflows/epilogue-validate.yml`

## CI Behavior
- Fails PRs when required files or core flags/sections are missing.
- Warns on `TBD` thresholds to allow iterative balancing.

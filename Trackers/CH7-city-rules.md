# CH7 City Rules — State & Validation

## Invariants
- `FF_KILL_FORBIDDEN == TRUE`
- `FRIENDLY_HIT_NONLETHAL == TRUE`
- `CIV_DEATH_COUNT == 0` within CH7 scope
- Lethal outcomes limited to `COMBATANT == TRUE` and explicit `LETHAL_ALLOWED` encounters (none in this placeholder).

## Flags & Counters
- `CIV_DEATH_COUNT` (int, must remain 0)
- `CIV_INJURY_COUNT` (int, advisory only)
- `FF_INCIDENT_COUNT` (int, advisory only)
- `URBAN_SAFEZONE_ACTIVE` (bool) — when TRUE, force non-lethal clamp on `COMBATANT == FALSE`

## Validation
- CI asserts presence of `FF_KILL_FORBIDDEN` and `FRIENDLY_HIT_NONLETHAL` in CH7 docs.
- CI warns if thresholds marked TBD; fails if any invariant missing.

## Outputs
- Audit log entries for any friendly-fire incident with automatic non-lethal resolution.

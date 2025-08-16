# CH7 Placeholder Patch — DIPLOMAGIC

## Title
**CH7: Systems Fallout (Packaging Only)**

## Purpose
Packaging-only placeholder to bridge **CH6: Glorious Quest** to **Epilogue: Reorientation**.

## City Ruleset (Hard Requirements)
- **FF_KILL_FORBIDDEN = TRUE**: Friendly/civilian hits can never be lethal.
- **FRIENDLY_HIT_NONLETHAL = TRUE**: Engine clamps result to non-lethal state (stun/medical) for any `COMBATANT == FALSE` target.
- **CIV_DEATH_COUNT == 0** must hold for CH7 scope.
- **HOSTILE_DEFINITION**: Lethal resolutions only permitted when `COMBATANT == TRUE` and encounter is marked `LETHAL_ALLOWED` by mission design (not applicable to this CH7 placeholder).

## Function
- Provides linkage flags only; **no combat encounters** or mission content are introduced.
- Ensures build continuity and final tally gates.

## Notes
- All Epilogue triggers depend on `CH6_COMPLETE == TRUE`.
- CH7 must not introduce any lethal outcomes; CI will fail if CH7 docs allow lethal on friendlies/civilians.

# CH7 Placeholder Patch — DIPLOMAGIC

## Title
**CH7: Systems Fallout (Packaging Only)**

## Purpose
Packaging-only placeholder to bridge **CH6: Glorious Quest** to **Epilogue: Reorientation**.

## City Ruleset (Hard Requirements)
- **FF_KILL_FORBIDDEN = TRUE** — friendly and civilian targets cannot be killed.
- **FRIENDLY_HIT_NONLETHAL = TRUE** — all hits on non‑combatants resolve as non‑lethal (stun/medical).
- **CIV_DEATH_COUNT == 0** for the entire CH7 scope.
- **HOSTILE_DEFINITION** — lethal resolutions apply only to `COMBATANT == TRUE` in encounters explicitly marked `LETHAL_ALLOWED` (none exist in this placeholder).

## Function
- Provides linkage flags only; **no combat encounters** or mission content are introduced.
- Ensures build continuity and final tally gates.

## Notes
- All Epilogue triggers depend on `CH6_COMPLETE == TRUE`.
- CH7 introduces no lethal outcomes.
- CI will fail if these invariants are not respected.

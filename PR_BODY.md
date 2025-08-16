# CH7 Packaging Placeholder

Purpose: add a non-content Chapter 7 placeholder so CI and narrative flow validate cleanly between **CH6: Glorious Quest** and **Epilogue: Reorientation**.

## Contents
- `Patches/CH7-placeholder.md` — placeholder notes and constraints
- `Trackers/CH7-state.md` — dependency flags to gate Epilogue

## Constraints
- No missions, beats, NPCs, or branching states are introduced.
- Activation requires `CH6_COMPLETE == TRUE`.
- Sets `EPILOGUE_ACTIVE == TRUE` and `EPILOGUE_READY == TRUE` when placeholder is active.
- May only be expanded with explicit narrative approval.

## Rationale
Outline and Playbook contain no Chapter 7. This PR prevents dangling chapter references in tools and CI and keeps Epilogue gating explicit.

## Validation
- Lints: docs only
- CI: should detect CH7 presence and pass placeholder checks

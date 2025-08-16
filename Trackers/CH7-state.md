# CH7 State Tracker — DIPLOMAGIC

## Dependencies
- Requires CH6 completion flag (`CH6_COMPLETE == TRUE`).
- Unlocks Epilogue (`EPILOGUE_ACTIVE == TRUE`).

## States
- `CH7_PLACEHOLDER_ACTIVE`: TRUE when CH6 is completed.
- `CH7_HAS_CONTENT`: FALSE (no missions or beats defined).
- `EPILOGUE_READY`: TRUE when CH7 placeholder activates.

## Validation
- CI checks pass if CH7 placeholder exists.
- No branching states or false endings in CH7.

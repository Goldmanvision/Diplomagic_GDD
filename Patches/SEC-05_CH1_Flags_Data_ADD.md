# SEC-05 — CH1 Flags & Data ADD
Version: v0.1
Date: 2025-08-14 12:15Z
Owner: Nick Goldman

Paste under Save/Data and Systems Flags.

## Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

## CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

## Telemetry
Emit `pin_auto_log_created` when CaseNote is created.

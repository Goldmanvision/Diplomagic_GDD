# Inline Patch — SEC-05 CH1 Flags & Data
Version: v0.1 — 2025-08-14 22:50:08 UTC
Owner: Nick Goldman

## BEGIN PATCH: SEC‑05 — CH1 Flags & Data

### Save keys (extend)
- `medstat_upgrade_card_found` (bool)
- `medstat_upgrade_card_inserted` (bool)

### CaseNote on insert
Create `CaseNote` with `symbol_id:"SYM-001"` and text from Prologue pin when card inserted. Does not affect WS.

### Telemetry
Add `pin_auto_log_created` on CaseNote creation.

## END PATCH

# SEC-07 — CH1 MEDSTAT Notes UI ADD
Version: v0.1
Date: 2025-08-14 12:42Z
Owner: Nick Goldman

Paste under SEC‑07 UI (Devices → MEDSTAT).

## Notes panel (unlocks via note‑card)
- Tabs: Vitals (P‑OX/BP/TEMP) and **NOTES**.
- List: Time, Title (≤14), Source, Tag (SYM‑001 icon). Row ≥32 px @1080p.
- Detail: Title/time/source; body ≤140 chars; actions: PIN TO CASEBOARD (disabled), CLOSE.
- Strings: ui.medstat.notes.tab=NOTES; ui.medstat.notes.toast_logged=Note logged from earlier chart.
- AX: AA contrast; scale 0.85–1.50; focus ring; high‑contrast skin.
- Telemetry: medstat_upgrade_card_inserted; pin_auto_log_created; medstat_notes_opened (opt).

## Flow
1) Insert card → unlock Notes tab → toast.  
2) Auto‑create CaseNote for Prologue pin (SYM‑001), read‑only.  
3) Later chapters: enable edit and FieldPad sync.

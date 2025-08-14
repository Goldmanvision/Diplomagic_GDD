# SEC-07 — MEDSTAT Notes UI (CH1)
Version: v0.1
Date: 2025-08-14 22:50:08 UTC
Owner: Nick Goldman
Scope: Add Notes panel unlocked by note‑card; ≤14‑char labels.

## Panels
- Vitals (existing): P‑OX, BP, TEMP.
- **Notes (new):** list view + detail pane.

## Notes List
- Columns: Time, Title (≤14), Source (icon), Tag (SYM‑001 icon if present).
- Row height 32 px @1080p; tap target ≥32×32.
- Focus ring visible; high‑contrast skin supported.

## Note Detail
- Header: Title; time; source.
- Body: up to 140 chars; wrap at 24–28 chars.
- Actions: PIN TO CASEBOARD (disabled until FieldPad appears), CLOSE.
- Read‑only in CH1; edit later when FieldPad syncs.

## Strings
- ui.medstat.notes.tab → NOTES
- ui.medstat.notes.toast_logged → Note logged from earlier chart.
- ui.medstat.notes.title.pin → Pin note
- ui.medstat.notes.action.pin_to_caseboard → PIN TO CASEBOARD
- ui.medstat.notes.action.close → CLOSE

## Card/Hardware spec
- Slot: PCMCIA Type II (68‑pin), 5V linear flash; **Newton‑compatible** software card.
- Optional media: CF Type I via PCMCIA adapter.
- Scope: enables **Notes** only; **no camera, no internet stack** on MEDSTAT.
- Networking note: **SENTINEL** satellite hop syncs with **linked MEDSTATs** only; no wide internet.

## Flow
1) Insert card → unlock Notes tab → toast.
2) Auto‑create **CaseNote** from Prologue pin (SYM‑001), read‑only.
3) Later chapters: allow new Notes and FieldPad sync → Casefile.

## AX/L10N
- Text contrast WCAG AA; slider scale works.
- All labels ≤14 chars; provide short forms for target langs.

## Telemetry
- medstat_upgrade_card_inserted
- pin_auto_log_created
- medstat_notes_opened (optional)

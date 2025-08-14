# Propagation — TDD: Evidence + FieldPad Hooks from Prologues
Version: v0.1
Date: 2025-08-14 10:49:18 UTC
Owner: Nick Goldman
Scope: Device flows affected by 0A/0B.

## 0A (1989) — No FieldPad
- Analog-only custody: paper forms; locker window handoff.
- No digital evidence created. No JSON writes in 0A.

## 0B (1994) — MEDSTAT-only
- Device set: MEDSTAT handheld + RF wrist-band. No FieldPad, no TAPLINE.
- Interaction: vitals panels; paper chart notes.

## CH1 Upgrade (Clara)
- Pickup: MEDSTAT **note-card** unlocks **Notes** feature on MEDSTAT.
- On insert:
  - Create **CaseNote** per SEC-05 (symbol SYM-001).
  - Telemetry: `medstat_upgrade_card_inserted`, `pin_auto_log_created`.
  - UI: show “Note logged from earlier chart” toast.

## FieldPad (later chapters)
- When FieldPad is first available, sync CaseNotes to Casefile; no EvidenceItem created unless player later photographs the symbol in-world.
- If the player photographs a matching symbol later, create EvidenceItem normally; WS unaffected by the earlier note.

## Save/Load
- Bump `evidence_schema_ver` minor. Default new keys to false/null for old saves.
- Integrity: checksum includes `prologue_flags` and CaseNotes.

## String keys (examples)
- `ui.tut.0a.challenge`, `ui.tut.0a.cuff`, … as in TutorialCopy 0A.
- `ui.tut.0b.pox`, `ui.tut.0b.bp`, `ui.tut.0b.temp`, `ui.tut.0b.pin`.
- `toast.note_logged_from_chart`.

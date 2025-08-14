# Inline Patch — TDD: Evidence + FieldPad Hooks from Prologues
Version: v0.1 — 2025-08-14 10:57:09 UTC
Owner: Nick Goldman
Paste into TDD under device flows and save/load contracts.

---
## BEGIN PATCH: TDD — Prologue Device Hooks

### 0A (1989) — No FieldPad
- Analog custody only (paper forms; locker window handoff). No digital EvidenceItem writes.

### 0B (1994) — MEDSTAT‑only
- Device set: MEDSTAT handheld + RF wrist‑band. Notes on **paper chart** only. No FieldPad/TAPLINE.

### CH1 MEDSTAT upgrade (Clara)
- Pickup: MEDSTAT **note‑card** enables **Notes** feature on MEDSTAT.
- On insert:
  - Create **CaseNote** per SEC‑05 with `symbol_id:"SYM-001"` referencing the Prologue pin.
  - Telemetry: `medstat_upgrade_card_inserted`, `pin_auto_log_created`.
  - UI toast: “Note logged from earlier chart.”

### FieldPad (later chapters)
- Sync CaseNotes into Casefile when FieldPad first appears. Do **not** retro-create EvidenceItems.

### Save/Load
- Include new `prologue_flags` and CaseNotes in checksum; bump schema minor.

## END PATCH

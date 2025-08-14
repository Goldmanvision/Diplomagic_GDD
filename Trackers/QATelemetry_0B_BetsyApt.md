# 0B — Clara Prologue QA + Telemetry Matrix (Betsy’s Apt, 1994)
Version: v0.1
Date: 2025-08-14 10:41:59 UTC
Owner: Nick Goldman
Scope: QA coverage, AX checks, telemetry events, and pass/fail gates for Clara’s home‑visit tutorial.

## 1) Entry/Exit Criteria
**Entry:** Latest dev build boots; Betsy apt map loads clean.  
**Exit (Prologue 0B):**
- P1=0, P2≤3 in scope; **Crash-free P90 ≥ target**, perf within SEC‑11 budgets.
- Tutorial completion **P75 ≤ 20 min**; `vitals_logged == 3` (P‑OX, BP, TEMP).
- `brightstar_pin_found` recorded or explicitly skipped; **no hard fail paths** here.

## 2) Test Suites (subset)
- **TS-BOOT-0B:** boot→menu→load apt; crash reporter check.
- **TS-UI-0B:** prompts (≤14 chars), subtitles, input remap, UI scale.
- **TS-MEDSTAT-0B:** pulse‑ox → BP → temp flows; retry tips; values log.
- **TS-CARE-0B:** tea, pills, tidy; optional hallway chat; chart note.
- **TS-POV-0B:** **Reddy‑POV** cut triggers and is not rewatchable in Prologue.
- **TS-PIN-0B:** pin inspect/collect; note on paper chart.
- **TS-PERF-0B:** perf spots captures (living room table; doorway); med/95p.
- **TS-LOC-0B:** pseudo‑loc glyphs, truncation checks on little labels.
- **TS-AX-0B:** see §4 AX matrix.

## 3) Telemetry Events (authoritative keys)
Storage: local JSON; opt‑in upload; anonymized session_id.

### Common fields
`ts` (ISO‑8601Z), `build_id`, `session_id`, `map`, `player_pov` ("Clara"), `diff`, `device`.

### Events
- `prologue_clara_complete` → fields: `time_s`, `vitals_logged`, `care_tasks_done`.
- `vitals_logged` → `pox_bool`, `bp_bool`, `temp_bool`.
- `care_tasks_done` → `tea_bool`, `pills_bool`, `tidy_bool`.
- `reddy_pov_played` → `played_bool`.
- `brightstar_pin_found` → `found_bool`.
- `cult_symbol_link_active` → set **true only when** both `brightstar_pin_found` and later `hauser_pistol_awarded` are true (cross‑chapter).

## 4) Accessibility (AX) Matrix
- AX‑001 Subtitles ON with speaker tags. **Pass:** visible by default.
- AX‑002 UI scale 0.85–1.50; no clipping on MEDSTAT panels. **Pass:** no overlap.
- AX‑003 High‑contrast device skin selectable; persists. **Pass.**
- AX‑004 No color‑only cues for vitals status; shapes/icons used. **Pass.**
- AX‑005 Hold↔toggle options available for interactions. **Pass.**

## 5) Compliance/Period Checks
- **No FieldPad/TAPLINE** in 0B; MEDSTAT handheld + RF wrist‑band only. **Pass.**
- Landline/buzzer period‑correct; Caller ID not guaranteed. **Pass.**
- CRT/VHS are background only; no modern devices. **Pass.**

## 6) Performance & Stability Targets
- Interior perf spots: **GPU ≤ 14 ms @1080p** mid‑tier; draws and tris within SEC‑11/09 caps.
- Soak: 2h idle/traversal; save/load loop every 10 min; **no memory growth** > 5%.

## 7) Pass/Fail Gates
- Gate‑G1: `vitals_logged == 3` before care tasks marked complete.
- Gate‑G2: `reddy_pov_played == true` before scene wrap.
- Gate‑G3: If pin skipped, set `brightstar_pin_found = false` and allow continuation.

## 8) Evidence (what to capture)
- Screenshots: MEDSTAT panels, pin inspect, paper chart note.
- CSV: perf med/95p at living room/doorway spots.
- Video: 30–60s pass of vitals; Reddy‑POV cue.

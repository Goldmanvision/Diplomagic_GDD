# 0A — Avery Prologue QA + Telemetry Matrix (Quantico, 1989)
Version: v0.1
Date: 2025-08-14 10:41:59 UTC
Owner: Nick Goldman
Scope: QA coverage, AX checks, telemetry events, and pass/fail gates for Hogan’s Alley (night).

## 1) Entry/Exit Criteria
**Entry:** Latest dev build boots; TS-BOOT smoke pass; range and alley maps load.  
**Exit (Prologue 0A):**
- P1=0, P2≤3 in scope; **Crash-free P90 ≥ target**, perf within SEC‑11 budgets. 
- Tutorial completion **P75 ≤ 20 min**; **arrest:kill ≥ 2:1**; custody_complete rate ≥ 95%.
- **Award rule**: pistol award path triggers only when **score ≥ 90 AND ROE violations = 0**.

## 2) Test Suites (subset)
- **TS-BOOT-0A:** boot→menu→load Hogan’s Alley; save path perms; crash reporter check.
- **TS-UI-0A:** HUD prompts (≤14 chars), subtitles on, input remap, hold↔toggle.
- **TS-ROE-0A:** challenge→cuff→search; unjustified shot admonish; rewind.
- **TS-CUSTODY-0A:** 35mm photo; bag→tag→log; locker handoff; missing-step handling.
- **TS-RANGE-0A:** basic → dual‑wield → decoupled aim; **non‑lethal ammo tutorial**.
- **TS-ESCORT-0A:** non‑lethal takedown + escort loop to safe zone.
- **TS-PERF-0A:** perf spots captures (lane, alley corner); med/95p frame times.
- **TS-LOC-0A:** pseudo‑loc glyphs, truncation checks on posters/labels (if any).
- **TS-AX-0A:** see §4 AX matrix.

## 3) Telemetry Events (authoritative keys)
Storage: local JSON; opt‑in upload; anonymized session_id.

### Common fields
`ts` (ISO‑8601Z), `build_id`, `session_id`, `map`, `player_pov` ("Avery"), `diff`, `device`.

### Events
- `prologue_avery_complete` → fields: `time_s`, `arrests`, `shots_total`, `shots_on_compliant`, `roe_violations`, `score`.
- `arrest_performed` → `suspect_id`, `location`, `nonlethal_bool`.
- `custody_complete` → `photo_bool`, `bag_bool`, `tag_bool`, `log_bool`, `locker_bool`.
- `range_dual_done` → `hits_pct`.
- `range_decouple_done` → `hits_pct`.
- `nonlethal_ammo_trained` → `hits_pct`.
- `nonlethal_takedown_done` → `clean_bool` (no injury).
- `escort_done` → `time_s`, `breaks`.
- `hauser_pistol_awarded` → `score`, `roe_violations`.
- `cult_symbol_link_active` → always `false` in 0A (set later when 0B also true).

## 4) Accessibility (AX) Matrix
- AX‑001 Subtitles ON with speaker tags. **Pass:** visible by default.
- AX‑002 Input remap and hold→press toggle works for CHALLENGE/CUFF. **Pass:** remap persists.
- AX‑003 UI scale 0.85–1.50; no clipping in prompts/inventory. **Pass:** no overlap.
- AX‑004 High‑contrast prompt theme available. **Pass:** toggle persists.
- AX‑005 No color‑only cues for ROE states. **Pass:** icon/glyph present.

## 5) Compliance/Period Checks
- 1989 analog only: no FieldPad/TAPLINE; no digital tagging. **Pass:** device audit clean.
- Telephonic warrant timing referenced only; no call UI. **Pass:** text only.
- Signage and props period‑correct (posters, radios, SLR). **Pass:** audit per PERIOD‑ACCURACY.

## 6) Performance & Stability Targets
- Range lane / alley perf spots: **GPU ≤ 14 ms @1080p** mid‑tier; draws and tris within SEC‑11/09 caps.
- Soak: 2h idle/traversal; save/load loop every 10 min; **no memory growth** > 5%.

## 7) Pass/Fail Gates
- Gate‑G1: `roe_violations == 0` when `score ≥ 90` to open award path.
- Gate‑G2: `custody_complete` must be true before debrief.
- Gate‑G3: `nonlethal_ammo_trained == true` before escort drill unlocks.

## 8) Evidence (what to capture)
- Screenshots: prompts, custody checklist complete, award/no‑award debrief cards.
- CSV: perf med/95p, range hits_pct logs.
- Video: 30–60s of each drill; non‑lethal tutorial segment.

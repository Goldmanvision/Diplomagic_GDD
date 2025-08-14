# [SEC-11-QA] QA, Localization, Accessibility
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-13-APPENDICES — Appendices`
- `SEC-08-ARTAUDIO — Art Direction & Audio`

## **11.1 QA Strategy**

### Goals
Ship a stable, readable, fair game that meets perf budgets and accessibility baselines.

### Approach
Risk‑based testing on core loops (SEC‑04), systems (SEC‑05), UI (SEC‑07), art/audio (SEC‑08), and tech (SEC‑09).

### Test types
- **Smoke (per build):** boot, load, start mission, exit.
- **Functional:** devices, evidence chain, ROE, stealth, combat, save/load, caseboard.
- **Systems:** AI perception, heat, reputation, telemetry events.
- **Performance:** FPS, frametime, draw calls, VRAM, CPU/GPU budgets.
- **Stability:** long‑session soak (2–3 h), repeated save/load, memory growth.
- **Regression:** checklist per feature after fixes.
- **Compatibility:** min/rec PC configs, gamepad parity.

### Entry/Exit gates
Slice/EA/Beta builds require: crash‑free P90 ≥ target, KPI deltas reported, no Blockers/Criticals open.

## **11.2 Bug Policy**

### Severity & SLAs

| Severity | Definition | SLA |
|---|---|---|
| **Blocker** | Crash/data loss, progress stop | Fix/rollback same day |
| **Critical** | Major system broken, mission cannot complete | 48–72 h |
| **High** | Significant feature defect or perf miss | Within sprint |
| **Medium** | Noticeable defect, workaround exists | As capacity allows |
| **Low** | Cosmetic, minor text, non‑blocking | Backlog |

### Status flow
New → Triaged → In‑Progress → Fixed → Verified → Closed.

### Repro format
Build, map, steps, expected/actual, logs, attachments.

## **11.3 Test Matrices (core)**

### Devices
- **FieldPad:** Photo → Tag → Chain, links, warrant score, judge pass/fail.
- **TAPLINE:** Scan/Record/Triangulate/Decode/Spoof; warrant gating.
- **MEDSTAT:** status effects, triage actions, team telemetry (Avery), self‑care (Clara).

### Loops
- Investigate → Act → Record; evidence used before action ≥70%.
- Clara stealth resolution ≥60%; Avery arrest:kill ≥ 2:1.
- Save/Load persists caseboard, evidence chain, heat/reputation, device unlocks.

### Performance
- Interior: ≤ 0.8 M tris, ≤ 1,200 draws, GPU ≤ 14 ms @1080p min‑spec.
- Exterior: ≤ 1.5 M tris, ≤ 1,800 draws, GPU ≤ 14 ms @1080p.
- Audio voices ≤ 48; VFX caps per SEC‑08.

## **11.4 Telemetry & Crash**

### Events
Evidence logged, warrant pass/fail, arrest/kill, stealth resolves, mission time, deaths, crashes.

### Storage
Local JSON logs; opt‑in upload; anonymized session ID.

### Crash reporter
Enabled; symbols stored per build.

## **11.5 Accessibility (Checklist)**

### Global
- Subtitles on by default with speaker tags.
- UI scale slider; minimum body size ≥ 12 px @1080p.
- Color‑blind safe glyphs; high‑contrast device skin (Gray).
- Toggle hold‑to‑press; remap all inputs.
- Reduce camera shake/flash options.
- Content warnings pre‑scene; skip with summary.

### Devices/UI
- Tap targets ≥ 32×32 px @1080p; focus ring visible.
- WCAG AA text contrast per SEC‑08 pairs.
- Latency modeled but input buffered for accessibility mode.

### Audio
- Dynamic range presets (Night/TV/Cinema).
- SFX ducking under dialogue; subtitle timing aligned.

### Difficulty
- Aim assist, clue timers, device hinting, stealth forgiveness toggles.
- No forced QTEs without remap/hold options.

### QA acceptance
Accessibility smoke on every milestone build; defects tracked like functional bugs.

## **11.6 Localization Plan**

### Scope
UI, HUD, device text, tutorials, subtitles, store copy.

### Pipeline
UE Localization Dashboard → string tables; resource keys for device labels.

### Length constraints
Device labels ≤ 14 chars; wrap at 24–28 chars.

### Languages
Start en‑US → add by demand (e.g., de, fr, es‑LA, ja, zh‑CN).

### Schedule
String freeze at Beta; LQA before Gold.

### Deliverables
- Master string table (CSV/PO).
- Glossary + style guide.
- Font fallback sets per SEC‑08.
- LQA test cases: device flows, HUD truncation, right‑to‑left audit if added.

## **11.7 Compliance & Ratings**
- ESRB M / PEGI 18 content guidance in SEC‑02.
- Privacy: clear telemetry consent; no PII logged.
- Licenses: fonts and SFX licenses tracked in SEC‑08.

## **11.8 Milestone QA Passes**
- **Pre‑EA:** full functional + perf + accessibility baseline.
- **Pre‑Beta:** regression, content‑complete sweep, LQA round 1.
- **Pre‑Gold:** stability soak, perf locks, LQA final, accessibility sign‑off.

## **11.9 Approvals**
On approval: archive to MASTER as `[SEC-11-QA] v0.1` and update manifest. Next: **SEC‑12 Risks, Legal, Ratings**.

# [SEC-14-QA] Quality Assurance Test Plan
Version: v0.1  
Date: 2025-08-12  
Owner: Nick Goldman

### Related sections
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-13-APPENDICES — Appendices`

## **Scope**
End‑to‑end QA for PC builds. Aligns with SEC‑06/07/08/09/11/13 and PKG‑BUILD‑SOP.

## **14.0 Objectives**

* Find and prevent regressions that block play, performance, or accessibility.
* Keep shipping confidence high through automated and manual coverage.
* Produce repeatable evidence for compliance and marketing capture.

## **14.1 Definitions**

* **P1/P2/P3** severity; **Blocker/Major/Minor**.
* **Golden Path**: curated story progression per level for perf capture.
* **Perf Spot**: fixed coordinates/angles for comparable captures.

## **14.2 Test Types**

* **Automation**: boot, menu flows, devices (FieldPad/TAPLINE/MEDSTAT), save/load, controller hot‑swap.
* **Functional**: mission flows, evidence chain steps, warrants, TAPLINE, MEDSTAT.
* **Compatibility**: min/mid/high PC configs; windowed/fullscreen; input devices.
* **Performance**: frame time median/95p at perf spots; streaming boundaries.
* **Stability**: long‑run soak; save/load loops.
* **Localization/LQA**: layout, truncation, glyph coverage.
* **Accessibility**: AX‑matrix from SEC‑11; subtitles, UI scale, reduced‑horror, color‑independent cues.
* **Compliance**: CM‑matrix from SEC‑11.

## **14.3 Environments**

* **OS**: Windows 10/11.
* **Hardware tiers**:
  * **Min**: GTX 970 / RX 570, 8 GB RAM, HDD/SSD SATA.
  * **Mid**: GTX 1660 / RX 6600, 16 GB RAM, SATA SSD.
  * **High**: RTX 3060+ / RX 6700+, 16–32 GB, NVMe.
* **Displays**: 1080p required; check 1440p/4K scaling.
* **Input**: KBM, Xbox/PS controller; hot‑plug tests.

## **14.4 Tools & Data**

* UE automation framework; replay recorder; stat dumps; CSV exporters.
* Crash reporter with symbols; minidumps stored.
* Telemetry staging endpoint for canary events (SEC‑13).
* Screenshot script for shotlist (press kit).

## **14.5 Bug Workflow**

* **Tracker states**: New → Triaged → In‑Progress → Ready‑for‑QA → Verified/Failed → Closed.
* **Required fields**: build ID, map, steps, expected, actual, severity, repro rate, attachments.
* **SLA targets**: P1 fix attempt ≤ 48h; P2 within next sprint; P3 on backlog.

## **14.6 Entry/Exit Criteria**

* **Sprint Entry**: latest dev build boots; smoke tests pass.
* **Sprint Exit**: P1=0, P2≤10, perf within budgets on mid tier, CM/AX reds=0.
* **Milestone Exit**: all sprint exits + capture pack updated + SEC‑11 evidence archived.

## **14.7 Test Suites (high level)**

* **TS‑BOOT**: cold boot to menu; crash reporter check; save path permissions.
* **TS‑UI**: HUD prompts, menus, options, remap, glyph swap.
* **TS‑DEV‑FIELD**: FieldPad camera→Tag→Bag→Log; Caseboard; Warrant Builder WS.
* **TS‑DEV‑TAPLINE**: ping→triangulate→seize; icon state changes; toasts.
* **TS‑DEV‑MEDSTAT**: self‑care, Reddy check, stabilize.
* **TS‑MISSIONS**: per‑level objective flow, stealth/breach alt paths, re‑entry states.
* **TS‑SAVE**: slot create/load/delete; atomic write; backup restore.
* **TS‑PERF**: perf spots captures; heatmap boundaries.
* **TS‑AX**: subtitles, UI scale, high‑contrast skin, reduced‑horror, color‑independent cues.
* **TS‑LOC**: pseudoloc, truncation, font fallback.
* **TS‑COMPLIANCE**: CM matrix runs.

## **14.8 Perf Spots (initial)**

| ID | Map | Coords | Notes |
|---|---|---|---|
| PS‑L01‑LOT | L‑01 Kids Kamp lot | (x,y,z) TBD | Exterior cones/fog check |
| PS‑L03‑RD | Backwoods road bend | (x,y,z) TBD | Streaming boundary |
| PS‑L06‑TUN | NYC steam tunnel hub | (x,y,z) TBD | Dynamic lights |
| PS‑L07‑ASC | Transdimensional complex | (x,y,z) TBD | Kadath VFX |

## **14.9 Accessibility Tests (AX)**

* **AX‑001**: Subtitles default ON; size slider works; speaker tags visible.
* **AX‑002**: UI scale 0.85–1.50; no clipping at extremes.
* **AX‑003**: High‑contrast device skin selectable; persists.
* **AX‑004**: Status uses shapes/icons not color alone.
* **AX‑005**: Reduced‑horror swaps audio/visual spikes; summary page on skip.
* **AX‑006**: Hold→Press/Toggle available and functional.
* **Evidence**: screenshots + short videos archived to `/Compliance/AX/`.

## **14.10 Compliance Tests (CM)**
Follow SEC‑11 CM‑001..010; evidence archived to `/Compliance/CM/` with build ID and date.

## **14.11 Localization & LQA**

* Pseudoloc pass before LQA.
* LQA smoke on Beta: layout, truncation, context tags, cultural flags logged.

## **14.12 Soak & Stability**

* 2‑hour idle and traversal; memory growth monitored; save/load loop every 10 min.

## **14.13 Regression Strategy**

* Tag failing tests; auto‑replay affected missions; compare perf spot CSVs.
* Diff localization assets after string changes.

## **14.14 Reporting**

* **Daily**: open bugs by severity, crash rate, perf median/95p deltas.
* **Weekly**: CM/AX status, risk list, burn‑down chart.

## **14.15 Deliverables**

* Test plan DOCX, suites checklist CSV, perf capture CSV templates, evidence folder tree.

## **Approvals**
On approval: export DOCX (full + subsections) and ZIP with templates.

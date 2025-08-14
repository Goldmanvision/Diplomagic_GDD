# Patches — UPDATE_LOG
Version: v0.1
Date: 2025-08-14 09:31:00 UTC
Owner: Nick Goldman

This log records narrative and GDD patch files and how to apply them.

---

## 2025-08-14 — Prologues canonical addendum for SEC-03
**Files**
- `Patches/SEC-03_3.4_Synopsis_Prologues_ADD.md`

**Apply**
- Open `SEC-03-NARRATIVE` and **prepend** section **3.4 Synopsis** with the content of this file under a new subheading:
  `## **3.4 Synopsis — Prologues (Canonical)**`

**Scope / Rationale**
- Locks Prologue canon v0.3: 0A Avery (1989 Quantico), 0B Clara (1994 Betsy apt). 
- Clara Prologue uses **Reddy‑POV**; Clara finds **Brightstar pin**.
- 0B has **MEDSTAT handheld + RF wrist‑band only** (no FieldPad/TAPLINE).

**Cross‑refs**
- Trackers: `Trackers/NARR-TRACKER_Prologues_v0.3.md`, `Trackers/NARR-TRACKER_Playbook-Outline_Sync_v0.1.md`

**Telemetry/QA impacts**
- Add events: `prologue_avery_complete`, `prologue_clara_complete`, `brightstar_pin_found`.
- KPI: Prologue completion P75 ≤ 20 min; Avery arrest:kill ≥ 2:1.

**Notes**
- `Patches/0001-add-trackers.patch` is **parked** for reference only (not applied).

---

## Template for future entries
**Files**
- `Patches/<section>_<part>_<verb>.md`

**Apply**
- Replace/append details here.

**Scope / Rationale**
- One‑line purpose.

**Cross‑refs**
- Other files/sections touched.

**Telemetry/QA impacts**
- Events/KPIs/AX hooks if any.

**Notes**
- Anything operational.

## 2025-08-14T11:02Z — SEC-04/05/TDD Prologues propagation

**Files**
- `Trackers/InlinePatch_SEC-04_Prologues.md`
- `Trackers/InlinePatch_SEC-05_Prologues.md`
- `Trackers/InlinePatch_TDD_Prologues.md`

**Apply**
- Paste each block into its target doc:
  - SEC-04: add subheading “4.X Prologues Integration (0A/0B)” under Core Loops.
  - SEC-05: insert under Save/Data Schemas and Systems Flags.
  - TDD: insert under device flows and save/load contracts.
- After pasting, bump section versions in `MANIFEST.md` and record this log entry link.

**Scope / Rationale**
- Wires 0A/0B tutorials into loops, save flags, and device flows.
- Adds award gate (C96) and CaseNote vs Evidence behavior for pin symbol.

**Cross-refs**
- `Trackers/NARR-TRACKER_Prologues_v0.3.md`
- `Trackers/QATelemetry_0A_Quantico.md`, `Trackers/QATelemetry_0B_BetsyApt.md`

**Telemetry/QA impacts**
- Events/flags per QA matrices; `cult_symbol_link_active` derived when both pin+award are true.

**Notes**
- Keep file paths stable; track version in headers. Do not timestamp filenames.

## 2025-08-14T11:24Z — SEC-03 finalize (3.2 replace, 3.4 prepend)

**Files**
- `Patches/SEC-03_3.2_Chapter_List_REPLACE.md`
- `Patches/SEC-03_3.4_Synopsis_Prologues_ADD.md` (existing)
- `Patches/MANIFEST_Addendum_SEC-03_Prologues.md`

**Apply**
- Replace §3.2 entirely.
- Prepend §3.4 with the Prologues canonical block.
- Bump SEC-03 minor version in MANIFEST; paste addendum block.

**Scope / Rationale**
- Locks Prologues beats and canon in SEC-03. Aligns with trackers and QA matrices.

**Cross-refs**
- Trackers/NARR-TRACKER_Prologues_v0.3.md
- Trackers/QATelemetry_0A_Quantico.md, Trackers/QATelemetry_0B_BetsyApt.md

**Notes**
- Keep filenames stable; version lives in headers.

## 2025-08-14T12:08Z — CH1 trackers and inline patches

**Files**
- `Trackers/Shotlist_CH1_Brightstar.md`
- `Trackers/Shotlist_CH1_Roadside.md`
- `Trackers/InlinePatch_SEC-04_CH1.md`
- `Trackers/InlinePatch_SEC-05_CH1.md`
- `Trackers/InlinePatch_TDD_CH1.md`

**Apply**
- Paste inline patches into SEC‑04/05/TDD under CH1 sections.
- Use shotlists for press/compliance capture planning.

**Scope / Rationale**
- Establish CH1 capture and integrate CH1 loops, flags, and device hooks.

**Cross‑refs**
- `Trackers/CH1_Outline_SimpleCuriosity.md`
- `Trackers/CH1_Beat2Objective.md`
- `Trackers/AssetList_CH1_Brightstar.md`
- `Trackers/QATelemetry_CH1.md`

**Notes**
- Keep filenames stable. Version in headers.

## 2025-08-14T12:15Z — CH1 integration addenda for SEC-04/05/TDD

**Files**
- `Patches/SEC-04_CH1_Integration_ADD.md`
- `Patches/SEC-05_CH1_Flags_Data_ADD.md`
- `Patches/TDD_CH1_Device_Hooks_ADD.md`
- `Patches/MANIFEST_Addendum_CH1.md`

**Apply**
- Paste each addendum into the named sections; bump minor versions; link this entry in MANIFEST.

**Scope / Rationale**
- Integrates CH1 loops, save flags, and device hooks into core docs.

**Cross-refs**
- Trackers/CH1_Outline_SimpleCuriosity.md
- Trackers/CH1_Beat2Objective.md
- Trackers/AssetList_CH1_Brightstar.md
- Trackers/QATelemetry_CH1.md

## 2025-08-14T12:42Z — CH1 SEC‑06/07 addenda

**Files**
- `Patches/SEC-06_CH1_World_Layouts_ADD.md`
- `Patches/SEC-07_CH1_MEDSTAT_Notes_ADD.md`
- `Patches/MANIFEST_Addendum_CH1_Layouts_UI.md`

**Apply**
- Paste into SEC‑06/07 as new CH1 subsections; bump minor versions; link this entry in MANIFEST.

**Scope / Rationale**
- Locks CH1 world blockouts and MEDSTAT Notes UI.

**Cross‑refs**
- Trackers/SEC06_CH1_WorldLayouts.md
- Trackers/SEC07_CH1_MEDSTAT_Notes_UI.md

## 2025-08-14T12:52Z — SEC-03 add: 3.5 Chapter 1 synopsis

**Files**
- `Patches/SEC-03_3.5_CH1_SimpleCuriosity_ADD.md`
- `Patches/MANIFEST_Addendum_SEC-03_CH1.md`

**Apply**
- Insert as §3.5 in SEC-03; bump minor; add MANIFEST note.

**Scope / Rationale**
- Locks CH1 narrative beats consistent with trackers and QA.

**Cross-refs**
- Trackers CH1 outline, beat→objective, assets, QA/telemetry.

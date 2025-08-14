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

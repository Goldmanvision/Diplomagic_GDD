# Project: DIPLOMAGIC — Narrative Review + GDD Patches
Version: v0.1
Date: 2025-08-14 09:27:32 UTC
Owner: Nick Goldman

## Scope
- Chapter-by-chapter narrative audit; patch SEC-03.
- Maintain 1989/1994 period accuracy.
- Prologue canon v0.3: 0A Avery (1989 Quantico), 0B Clara (1994 Betsy apt).

## Canon & Rules
- Devices: 0A analog only; 0B **MEDSTAT handheld + RF wrist-band only** (no FieldPad/TAPLINE).
- Tech era (1994 later chapters): FieldPad uses **PCMCIA Type-II / CF Type-I via adapter**.
- POV/cinematics: **strict in-character**; Clara Prologue uses **Reddy-POV** for face/knife beat.
- Possession: **event-driven**; day/night only tunes spawns.
- Chapter 6 legs: **Clara→SRS**, **Avery→UN**; interleaved single mission.
- Conan homage: post-release, PD-safe; no trademarked name or actor likeness; alt concept OK.

## Source of Truth
- GitHub repo: `Goldmanvision/Diplomagic_GDD` (Markdown only).
- `Trackers/` holds working docs. `MANIFEST.md` logs versions.

## Active Canvases (max 3–5)
- **NARR-TRACKER — Prologues v0.3 (canonical)**
- **NARR-TRACKER — Playbook+Outline Sync v0.1**
- Temporary: SEC-03 patch plan (deprecate on merge)

## Process
- Approvals as y/n or numbers. Warn before heavy ops.
- Batch edits; one commit per scope; include summary/description.
- Do not regenerate combined export unless requested.

## Outputs
- File naming: `Trackers/<name>_vX.Y.md`
- Commit style:
  - Summary (≤50 chars): `<scope>: <concise change>`
  - Description: bullet files + one‑liners; notes; next steps.

## QA/Telemetry Hooks
- Events: `prologue_avery_complete`, `prologue_clara_complete`, `brightstar_pin_found`.
- KPIs: tutorial P75 ≤ 20m; Avery arrest:kill ≥ 2:1.

## Limits
- Keep active canvases ≤ 5. Prefer Git files. Avoid large attachments.

---
Title: Bind CH1 Scenes to Spawn Tables
Author: Postmaster
Date: 2025-08-17
Target: data/spawn/spawn_tables_prologue_ch1.md
Type: Patch
Status: Draft
---

# Rationale
Ensure encounters obey pacing caps and are traceable to scene_ids.

# Proposed changes
- Add `scene_id` column and populate per verification notes.
- Add spectral gating rule: darkness + ≥2 prior clues.

# Impacts
- Narrative report must finalize scene_id list.
- QA telemetry references scene_ids.
- Archivist validates props per scene.

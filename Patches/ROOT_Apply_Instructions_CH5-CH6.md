# Root Apply Instructions — CH5–CH6 Merge
Repo dir: /Patches

## Scope
Manual merge of CH5–CH6 into root docs: Narrative, Systems, World, UI. No binaries. Safe op.

## Files to paste
1) `ROOT_SEC-03_Narrative_CH5-CH6_Merge.md` → `SEC-03-NARRATIVE - Narrative.md`
2) `ROOT_SEC-05_Systems_Merge_Additions_CH5-CH6.md` → `SEC-05-SYSTEMS - Systems & Mechanics.md`
3) `ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md` → (`SEC-06-WORLD - World, Levels, & Content.md`) and (`SEC-07-UI - UI-UX (Devices, HUD, Menus).md`)

## Steps
1) Create a new branch, e.g., `feat/ch5-6-root-merge`.
2) Open each root doc. Find anchors (see anchors file). Replace the CH5 and CH6 sections with the content from the root merge patches.
3) Append Systems/World/UI sections as indicated.
4) Verify constraints:
   - 1994 period lock.
   - Prompts ≤14 chars.
   - Ambient phrase only: “the stars are right tonight.”
   - CH6 ROE: raid, lethal authorized, BlueOnBlue fail.
   - Evidence cap: CH6 total 3.
5) Run QA checklist in `/Trackers/CH5-6_Build_Verification.md`.
6) Commit with summary+description from this chat.
7) Open PR using the template in this batch.

## Notes
- Heavy-op warning: none. These are text edits only.

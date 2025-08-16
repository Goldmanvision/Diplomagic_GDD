# ROOT_Practical_Paste_Steps.md
> Apply these on branch `feat/ch5-6-root-merge`. Keep exports ≤3 files/turn.

## 1) SEC-03 — Replace CH5/CH6

- Replace Chapter 5 content with `/Patches/ROOT_SEC-03_CH5_Narrative_Paste.md`.

- Replace Chapter 6 content with `/Patches/ROOT_SEC-03_CH6_Narrative_Paste.md`.

Checklist:

- [ ] Headings match existing anchors.

- [ ] Cross-refs to SEC-05/06/07 intact.

## 2) SEC-05 — Insert systems snippets

Insert all blocks from `/Patches/ROOT_Systems_Snippet_Replacements.md` at the designated snippet IDs.

Checklist:

- [ ] No duplicate snippet IDs.

- [ ] Spells, Deputy randomization, HUD, camera rules present.

## 3) SEC-06/07 — Append world + UI

Append from `/Patches/ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md`.

- Link the ASCII map from `/Patches/SEC-06-CH6_Ascii_Map.md` inside SEC-06.

## 4) SEC-07 — Replace prompts

Replace with `/Patches/ROOT_SEC-07_UI_Prompts_Master.md`.

- Validate all prompts ≤14 chars.

## 5) README/ToC — Update

Add bullets from `/Patches/ROOT_Readme_ToC_CH5-CH6_Insert.md`.

## 6) Commit + PR

Commit summary (<50): `Integrate CH5–CH6 into root narrative/systems/world+UI`

Body: use `/Patches/PR_CH5-CH6_Root_Merge.md`

Labels: `period-1994, prompt-≤14, roe-raid, blue-on-blue, evidence-cap-3`

Milestone: `v0.6-ch5-6-merge`


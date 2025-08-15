# Practical Paste Steps — CH5–CH6
Repo dir: /Patches

1) Open `SEC-03-NARRATIVE - Narrative.md`.
2) Find `## CH5`. Select down to before `## CH6`. Delete.
3) Paste from `/Patches/ROOT_SEC-03_CH5_Narrative_Paste.md`.
4) Find `## CH6`. Select down to before `## CH7` (or EOF). Delete.
5) Paste from `/Patches/ROOT_SEC-03_CH6_Narrative_Paste.md`.
6) Open `SEC-05-SYSTEMS - Systems & Mechanics.md`. Paste blocks from `/Patches/ROOT_Systems_Snippet_Replacements.md` at noted headings.
7) Open `SEC-06-WORLD` and `SEC-07-UI`. Append from `/Patches/ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md` and `/Patches/ROOT_SEC-07_UI_Prompts_Master.md`.
8) Update README/ToC from `/Patches/ROOT_README_ToC_CH5-CH6_Insert.md`.
9) Run checks: `/Patches/ROOT_Validation_Grep_Patterns.md` and `/Trackers/ROOT_Merge_Smoke_Checks.md`.
10) Commit using messages in `/Patches/ROOT_Merge_Commit_Messages.md`. Open PR with template.

Constraints: 1994, ≤14 prompts, ambient phrase only: “the stars are right tonight.”

# GitHub Desktop — CH5–CH6 Root Merge Guide
Repo dir: /Patches

## Branch
1) New branch: **feat/ch5-6-root-merge**

## Stage 1 — Root patches
1) Open each root doc and paste from these files:
   - `ROOT_SEC-03_Narrative_CH5-CH6_Merge.md`
   - `ROOT_SEC-05_Systems_Merge_Additions_CH5-CH6.md`
   - `ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md`
2) Commit with:
```
Integrate CH5–CH6 into root narrative/systems/world+UI
```
Description:
```
Merged CH5–CH6 into three root-ready patches: (1) Narrative replacement for CH5–CH6 with rogue pivot, deep D-LAMP, Iron Highway, and CH6 raid + Splinter Vault endings; (2) Systems additions for phrase/scroll equip, raid ROE with Blue-on-Blue fail, cameras, AI FSMs, combat tuning, scoring; (3) World + UI merges with ≤14-char prompts and 1994 locks. Ambient phrase retained: “the stars are right tonight.”
```

## Stage 2 — Helpers (optional commit)
Add helper files (apply steps, anchors, checklists). Commit with:
```
Root merge helpers: apply steps, anchors, PR template
```
Description: copy from `ROOT_Merge_Commit_Messages.md`.

## Validate
Run through `/Patches/ROOT_Validation_Grep_Patterns.md` and `/Trackers/CH5-6_Build_Verification.md`.

## Open PR
Use `/Patches/ROOT_PR_Template_CH5-CH6_Merge.md` as the body. Assign narrative/systems/QA.

## After merge
Tag `v0.6-ch5-6-merge`. Open polish issues if needed.

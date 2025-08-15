# PR Open Runbook — CH5–CH6 Root Merge (Desktop + CLI)
Repo dir: /Patches

Safe op. Text-only.

## GitHub Desktop
1) Create branch: **feat/ch5-6-root-merge**.
2) Paste root patches per `/Patches/ROOT_Practical_Paste_Steps.md`.
3) Commit 1: root patches.
   Summary:
   ```
   Integrate CH5–CH6 into root narrative/systems/world+UI
   ```
   Description: see `/Patches/ROOT_Merge_Commit_Messages.md` (block 1).
4) Commit 2: helper docs (optional).
   Summary:
   ```
   PR kit for CH5–CH6 merge
   ```
5) Push branch. Open Pull Request.
6) PR body: paste from `/Patches/PR_CH5-CH6_Root_Merge.md`.
7) Attach files listed in `/Patches/PR_Attachments_CH5-CH6.md`.
8) Assign reviewers. Apply labels/milestone from `/Patches/PR_GitHub_Labels_and_Milestones.md`.
9) Run validations. Record results in `/Trackers/PR_Validation_Results_Summary_CH5-CH6.md`.

## Git CLI (optional)
```bash
git checkout -b feat/ch5-6-root-merge
# paste files per steps, then:
git add .
git commit -m "Integrate CH5–CH6 into root narrative/systems/world+UI"
git commit -m "PR kit for CH5–CH6 merge"  # if separate helpers commit
git push -u origin feat/ch5-6-root-merge
# open PR on GitHub and use the PR body/attachments listed above
```

Constraints: 1994 period; prompts ≤14; ambient phrase “the stars are right tonight.”

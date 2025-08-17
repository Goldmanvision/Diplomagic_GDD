# v0.1-docs-structure — Release notes

**Release:** v0.1-docs-structure
**Date:** 2025-08-16
**Merge evidence:** bea534b9ce4d1abc941c2bb10d7633a0c7a018e2

## Summary
Consolidates narrative playbooks, archive packs, and compliance fixes required to validate CH2/CH6/CH7 rules. Archive packs and CI assertions are included for provenance.

## Key changes
- Enforce CH2 compliance rules and update related validation tests.
- Add CH6 raid rules and CH7 city rules fixes.
- Large narrative and documentation import (archive packs). See `/Archive` for f  --reviewer "design-lead,qa"y.md \e release notes and repo snapshot" \structure
Switched to a new branch 'docs/release-v0.1'
warning: in the working copy of 'Archive/release_notes_v0.1-docs-structure.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'Archive/repo_snapshot.md', LF will be replaced by CRLF the next time Git touches it
[docs/release-v0.1 8807180] docs: add release notes and repo snapshot for v0.1-docs-structure
 2 files changed, 53 insertions(+)
 create mode 100644 Archive/release_notes_v0.1-docs-structure.md
 create mode 100644 Archive/repo_snapshot.md
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.51 KiB | 1.51 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'docs/release-v0.1' on GitHub by visiting:
remote:      https://github.com/Goldmanvision/Diplomagic_GDD/pull/new/docs/release-v0.1
remote:
To https://github.com/Goldmanvision/Diplomagic_GDD.git
 * [new branch]      docs/release-v0.1 -> docs/release-v0.1
branch 'docs/release-v0.1' set up to track 'origin/docs/release-v0.1'.

Creating pull request for docs/release-v0.1 into main in Goldmanvision/Diplomagic_GDD

could not add label: 'release/docs' not found

nicka@MiCon MINGW64 /f/Diplomagic_GDD_MASTER/Updated_GDD/Diplomagic_GDD_git (docs/release-v0.1)
$ # merge via GitHub CLI (preferred)
gh pr merge <PR_NUMBER_or_branch> --squash --body-file merge-body.md

# or locally then push
git checkout main
git pull origin main
git merge --squash fix/ch2-compliance
git commit -m "Merge fix/ch2-compliance: enforce CH2/CH6/CH7 compliance"
git push origin main
bash: PR_NUMBER_or_branch: No such file or directory
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 2), reused 4 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 2.43 KiB | 85.00 KiB/s, done.
From https://github.com/Goldmanvision/Diplomagic_GDD
 * branch            main       -> FETCH_HEAD
   4850ed5..33ff21b  main       -> origin/main
Updating 4850ed5..33ff21b
Fast-forward
 .release_pr_body.md                          | 14 +++++++++++++
 Archive/release_notes_v0.1-docs-structure.md | 30 ++++++++++++++++++++++++++++
 Archive/repo_snapshot.md                     | 23 +++++++++++++++++++++
 3 files changed, 67 insertions(+)
 create mode 100644 .release_pr_body.md
 create mode 100644 Archive/release_notes_v0.1-docs-structure.md
 create mode 100644 Archive/repo_snapshot.md
merge: fix/ch2-compliance - not something we can merge
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Everything up-to-date

nicka@MiCon MINGW64 /f/Diplomagic_GDD_MASTER/Updated_GDD/Diplomagic_GDD_git (main)
$ # create the file in repo root
cat > merge-body.md <<'MD'
Merge fix/ch2-compliance

- Enforce CH2 compliance rules
- Add CH6 raid rules and CH7 city rules fixes
- Update evidence-cap values and validation tests
- See ARCHIVE_PACK: GDD Rebuild 2025-08-16 for context.

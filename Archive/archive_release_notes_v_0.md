---
# Archive: release_notes_v0.1-docs-structure.md

**Release:** v0.1-docs-structure
**Date:** 2025-08-16
**Merge evidence:** `bea534b9ce4d1abc941c2bb10d7633a0c7a018e2`

## Summary
Consolidates narrative playbooks, archive packs, and compliance fixes required to validate CH2/CH6/CH7 rules. Archive packs and CI assertions are included for provenance.

## Key changes
- Enforce CH2 compliance rules and update related validation tests.
- Add CH6 raid rules and CH7 city rules fixes.
- Large narrative and documentation import (archive packs). See `/Archive` for full MD packs.

## CI / Validation
- CI smoke and validation checklist executed (local + CI).
- Evidence-cap tests referenced in archive packs. Verify CI artifacts attached.

## Known issues
- Large backup/combined docs included in merge. Consider pruning or moving backups to `/Archive/backups`.
- `ci/epilogue-asserts` artifacts may need final packaging and QA confirmation.

## Artifacts and links
- Archive packs: `/Archive/ARCHIVE_PACK_GDD_Rebuild_2025-08-16_1831ET.md`
- Merge commit: `bea534b9ce4d1abc941c2bb10d7633a0c7a018e2`

## Next steps
1. Finalize `ci/epilogue-asserts` packaging and attach CI artifacts.
2. Commit `repo_snapshot.md` to `/Archive`.
3. QA sign-off on CH2/CH6/CH7 inplay verification.

---

# Archive: repo_snapshot.md

**Repository:** Goldmanvision/Diplomagic_GDD
**Snapshot date:** 2025-08-16

## Main tag
- `v0.1-docs-structure` = `a94ff2a1…`

## Active PRs (as recorded in archive)
- `fix/ch2-compliance` — https://github.com/Goldmanvision/Diplomagic_GDD/compare/main...fix/ch2-compliance
- `ci/epilogue-asserts` — https://github.com/Goldmanvision/Diplomagic_GDD/compare/main...ci/epilogue-asserts
- `docs/steam-prep`
- `feat/epilogue-packaging`

## Branch SHAs (recorded)
- `main (tag: v0.1-docs-structure)` = `a94ff2a1…`
- `feat/epilogue-packaging` = `13c8f6f…`
- `ci/epilogue-asserts` = `d12827c4…`
- `docs/steam-prep` = `cd9923c5…`
- historical: `feat/ch6-rules-hotfix` = `b010cba6b1de33a10aa3123fe70666c4e34566a1`

## Notes
- Large merged docs increase CI artifact size. Monitor storage.
- Archive packs stored in `/Archive`. Use these as canonical provenance for narrative and compliance decisions.

## Commit instructions (suggested)

Create a branch, add the two files to `/Archive`, and open a PR:

```bash
# create branch
git fetch origin
git checkout -b docs/release-v0.1
mkdir -p Archive
# copy the two files into Archive/ (use editor or echo >)

# stage and commit
git add Archive/release_notes_v0.1-docs-structure.md Archive/repo_snapshot.md
git commit -m "docs: add release notes and repo snapshot for v0.1-docs-structure"

git push -u origin docs/release-v0.1
```

Suggested PR title: `docs: v0.1-docs-structure release notes and repo snapshot`

Suggested PR body:
- Purpose: add release notes and snapshot for v0.1-docs-structure.
- Includes: `/Archive/release_notes_v0.1-docs-structure.md`, `/Archive/repo_snapshot.md`.
- Merge requirements: CI green, 1 maintainer approval.

---

# Commit message (one-line + body)

**One-line:** `docs: add release notes and repo snapshot for v0.1-docs-structure`

**Body:**
```
Add release notes for v0.1-docs-structure and a repo snapshot file.
- Reference merge evidence: bea534b9
- Archive packs: ARCHIVE_PACK_GDD_Rebuild_2025-08-16_1831ET.md
- Purpose: preserve provenance and reduce active chat UI load by storing canonical kickoff artifacts in /Archive.
```

---

# QA / Verification
After opening the PR:
1. Ensure CI artifacts are attached to PR run.
2. Confirm files render correctly on GitHub.
3. Tag PR with `release/docs` label and request review from `@design-lead` and `@qa`.

---

*End of snapshot.*


# v0.1-docs-structure — Release notes

**Release:** v0.1-docs-structure
**Date:** 2025-08-16
**Merge evidence:** bea534b9ce4d1abc941c2bb10d7633a0c7a018e2

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
- Archive packs: /Archive/ARCHIVE_PACK_GDD_Rebuild_2025-08-16_1831ET.md
- Merge commit: bea534b9ce4d1abc941c2bb10d7633a0c7a018e2

## Next steps
1. Finalize `ci/epilogue-asserts` packaging and attach CI artifacts.
2. Commit `repo_snapshot.md` to `/Archive`.
3. QA sign-off on CH2/CH6/CH7 inplay verification.

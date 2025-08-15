# Rollback Plan — CH5–CH6 Root Merge
Repo dir: /Patches

Safe op. Text-only.

## Strategy
1) Create backup branch before merge: `git branch backup/pre-ch5-6-merge`
2) If revert needed:
```
git checkout backup/pre-ch5-6-merge
git checkout -b fix/revert-ch5-6
```
3) Restore root files from backup branch or previous commit:
- `SEC-03-NARRATIVE - Narrative.md`
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`

4) Open PR “Revert CH5–CH6 root merge” with reason and links.

## Validation after rollback
Run `/Patches/ROOT_Validation_Grep_Patterns.md` to ensure no stray lines remain.

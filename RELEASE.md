# Release Process

Version tags use the pattern `v<major>.<minor>-<codename>` for docs-structure milestones.

## Steps
1. Ensure `main` is up to date.
2. Update `CHANGELOG.md` with the new entry.
3. Tag and push:
   ```bash
   git checkout main && git pull
   git tag -a vX.Y-codename -m "summary of changes"
   git push origin vX.Y-codename
   ```

## Example
- `v0.1-docs-structure` — epilogue packaging, CH7 placeholder, CH6 fixes, validation rerun, period sweep, StarTAC→MicroTAC.

## Notes
- Prefer PR merges even if branch protection is disabled.
- Re-enable protections before public collaboration.
- Keep tags immutable. For corrections, create a new tag.

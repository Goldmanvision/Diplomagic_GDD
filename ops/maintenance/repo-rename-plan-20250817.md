# Repo Rename Plan — ASCII-safe rollout (20250817)

## Preconditions
1. Extract `ascii-safe-20250817.zip` at repo root. This creates `ascii-safe/` with duplicates.
2. Place this mapping at `ops/maintenance/ascii-safe-mapping-20250817.md`.

## One-liner (Git Bash)
```
bash scripts/apply-ascii-safe-renames.sh ops/maintenance/ascii-safe-mapping-20250817.md
```

## PowerShell (Windows)
```
powershell -ExecutionPolicy Bypass -File scripts/apply-ascii-safe-renames.ps1 ops/maintenance/ascii-safe-mapping-20250817.md
```

## Notes
- Script prefers `git mv`/`git rm` and falls back to OS moves.
- ascii-safe non-ASCII files are removed after moving the ASCII-safe duplicates.
- Mapping is kept at `ops/maintenance/`. ZIP can be stored at `ops/artifacts/`.
- Run `git status` and review before commit.

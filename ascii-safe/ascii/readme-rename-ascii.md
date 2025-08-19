# ascii-safe Rename Plan
Date: 2025-08-17

## What this does
Renames Markdown files to ascii-safe names and folders using `git mv` to preserve history.

## Usage (Bash)
```bash
# From repo root
bash ascii/git_rename_ascii.sh
git status
git commit -m "ascii-safe rename pass"
```

## Usage (PowerShell)
```powershell
# From repo root
powershell -ExecutionPolicy Bypass -File ascii\git_rename_ascii.ps1
git status
git commit -m "ascii-safe rename pass"
```

## Notes
- This creates directories as needed, then moves files.
- Review changes with `git status` before committing.
- If a path in the mapping doesn't exist in your repo, the script will fail on that line.

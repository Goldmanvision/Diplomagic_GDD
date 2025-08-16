# Archive Process Guide

## Purpose
Save chat transcripts as timestamped markdown files, push them to the repo for provenance, and restart project workflows in a fresh chat using kickoff macros.

## Prerequisites
- Local clone of `Goldmanvision/Diplomagic_GDD` with push rights.
- `git` installed.
- `gh` (GitHub CLI) installed and authenticated (recommended). Or GitHub web UI and a PAT for API calls.
- PowerShell (Windows) or Bash (Linux/macOS/Git Bash/WSL) access.

## Key macros
- `exmdcb` (EXPORT_AS_MD_AND_PREPARE_COPYBLOCK)
  - Run inside an **archived chat**.
  - Outputs two fenced blocks: Copy Block A (full `.md` file) and Copy Block B (minimal kickoff header).
- `ptstamp`
  - Generates new chat title: `GDD Rebuild <YYYY-MM-DD HHmm ET>` in America/New_York time.
- `kickoff`
  - Run in the new chat to start repo actions and checklist.

## Quick flow
1. Open archived chat. Paste `exmdcb` and send. Receive two copy blocks.
2. Save Copy Block A as `Archive/GDD_Rebuild_<YYYY-MM-DD_HHMM_ET>.md`.
3. Commit and push to `main` (or create a short branch and open a PR if preferred).
4. Create a new chat. Run `ptstamp` to get the canonical title. Set chat title accordingly.
5. Paste Copy Block B as the first message in the new chat.
6. Run `kickoff` (or reply `y`) in the new chat to trigger snapshot and sprint prep.

## Markdown frontmatter template
```md
# ARCHIVE PACK — <Chat Title>
ptstamp: GDD Rebuild <YYYY-MM-DD HHmm ET>
date: <YYYY-MM-DDTHH:MM:SS-04:00>
tags: [archive, exported]
repo: Goldmanvision/Diplomagic_GDD
notes: <one-line summary>

## Summary
<one-line summary>

## Active PRs / SHAs / Links
<list>

## Full chat transcript / notes
<paste transcript>
```

## Git commands (bash)
```bash
# save file locally
mkdir -p Archive
cat > "Archive/GDD_Rebuild_YYYY-MM-DD_HHMM_ET.md" <<'MD'
<PASTE COPY BLOCK A>
MD

# commit and push (branch or main)
git checkout -b archive/add-chat-exports-YYYY-MM-DD
git add Archive/GDD_Rebuild_YYYY-MM-DD_HHMM_ET.md
git commit -m "archive: add chat export YYYY-MM-DD"
git push --set-upstream origin archive/add-chat-exports-YYYY-MM-DD
# open PR in UI or:
# gh pr create --title "archive: add chat exports (YYYY-MM-DD)" --body-file pr_body.md
```

## Git commands (PowerShell)
```powershell
New-Item -ItemType Directory -Force -Path Archive
@'
<PASTE COPY BLOCK A>
'@ | Out-File -FilePath "Archive\GDD_Rebuild_YYYY-MM-DD_HHMM_ET.md" -Encoding utf8

git checkout -b archive/add-chat-exports-YYYY-MM-DD
git add Archive\GDD_Rebuild_YYYY-MM-DD_HHMM_ET.md
git commit -m "archive: add chat export YYYY-MM-DD"
git push -u origin archive/add-chat-exports-YYYY-MM-DD
```

## PR body template
```md
Adds exported chat archives to /Archive for provenance and repo retention.

Files:
- Archive/GDD_Rebuild_YYYY-MM-DD_HHMM_ET.md

Checklist:
- [ ] Verify frontmatter timestamps
- [ ] Confirm no sensitive data
- [ ] Merge and tag archive-YYYY-MM-DD
```

## Release / Tag snapshot
- Tag example: `git tag -a archive-YYYY-MM-DD -m "archive: chat exports YYYY-MM-DD" && git push origin archive-YYYY-MM-DD`
- Release: use GitHub web UI or `gh release create` from the repo root.

## Secrets & safety checks
- Always run: `git grep -nE "password|token|secret|ssn|credit|api_key" Archive || true`
- For deeper scans use `git-secrets` or `trufflehog`.
- Do not include PII. Redact before committing if present.

## Common issues & fixes
- **`gh` not found**: install via `winget` (Windows) or package manager. Run `gh auth login` in PowerShell. Avoid MinTTY for `gh auth login` (use PowerShell or `winpty`).
- **Heredoc errors**: On Windows use PowerShell here-strings or use bash/WSL for `<<'EOF'` heredocs.
- **Tag already exists**: choose a unique archive tag or `gh release edit` to update release notes.
- **Running commands outside repo**: ensure working directory contains `.git`.

## Naming & retention policy (recommended)
- File name: `GDD_Rebuild_<YYYY-MM-DD_HHMM_ET>.md` (ET timezone).
- Keep last 6 months in `Archive/` on `main`. Move older archives to compressed releases or cloud storage quarterly.
- Do not export more than 3 large files at once to avoid sandbox/UI limits.

## Troubleshooting checklist
- If `exmdcb` returns malformed blocks, confirm you pasted macro exactly.
- If Copy Block A is truncated, run `exmdcb` again in the same archived chat.
- If GH operations fail, run commands from repo root and verify `gh --version`.

## Appendix: quick copy-paste shells
- Bash save template (single line):
```bash
printf '%s' "<PASTE COPY BLOCK A>" > "Archive/GDD_Rebuild_$(date -u +'%Y-%m-%d_%H%M_ET').md"
```

End of guide.


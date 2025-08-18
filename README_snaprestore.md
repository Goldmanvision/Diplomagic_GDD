# DIPLOMAGIC Backup Kit

This backs up a project folder into timestamped, restorable snapshots.
It cannot duplicate ChatGPT's internal project state. It preserves your files, canvases exported to disk, macros, and docs.

## Files
- `snapshot.sh` — create a snapshot and archive, optional GPG encryption and retention.
- `restore.sh` — restore a snapshot into a target directory.
- `verify.sh` — verify snapshot integrity via SHA-256 manifest.

## Quick start
```bash
# 1) Pick a canonical project directory on disk
export SRC="$HOME/projects/DIPLOMAGIC_GDD"

# 2) Run a snapshot (keeps last 14 snapshots)
bash snapshot.sh -s "$SRC" -n DIPLOMAGIC_GDD -o "$HOME/backups" -k 14

# 3) Verify
bash verify.sh "$(tail -n1 <<< "$(bash snapshot.sh -s "$SRC" -n test -o /tmp | tail -n1)")"  # example

# 4) Restore later
bash restore.sh "$HOME/backups/DIPLOMAGIC_GDD/20250101T120000Z/archive.tar.gz" "$HOME/restore/DIPLOMAGIC_GDD"
```

## Encryption options
- Public-key: `--encrypt your@email` uses your GPG key.
- Symmetric: `--passphrase-file /path/to/secret.txt`.

## Scheduling
- Linux/macOS cron example:
  `0 */6 * * * /usr/bin/bash /path/to/snapshot.sh -s "$HOME/projects/DIPLOMAGIC_GDD" -n DIPLOMAGIC_GDD -o "$HOME/backups" -k 14`
- Windows: run in Git Bash or WSL and schedule with Task Scheduler.

## What to include in SRC
- Your GDD, source assets, exported canvases, and any docs that represent the "base state."
- Export chat threads or summaries to files if you want them versioned.

## Limits
This does not snapshot ChatGPT memory, automations, or model tuning. Treat the backed-up folder as the source of truth for restore.

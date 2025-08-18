# DIPLOMAGIC Workspace Rebuild Guide
Version: 20250818T042050Z UTC

This guide enables an exact, repeatable rebuild of the DIPLOMAGIC Project Workspace in ChatGPT‑5 using the provided bootstrap kit and backup scripts.

## Scope
- Recreate the Project Workspace with department threads and seeds.
- Restore working behavior: naming, macros, quiet‑period protocol.
- Pair with file‑level backups and Git for data integrity.

## Inputs Required
- ChatGPT‑5 access.
- `workspace_bootstrap/` folder from the bundle.
- GitHub repo URL to the GDD/source (or your local folder).
- Optional: `diplomagic_backup_kit/` to snapshot after rebuild.

## Folder Map (from the bundle)
- `workspace_bootstrap/INSTRUCTIONS.md` — Workspace Instructions to paste verbatim.
- `workspace_bootstrap/MEMORY.md` — Long‑lived facts seed, pin in Admin thread.
- `workspace_bootstrap/MACROS.md` — Macro definitions and outputs.
- `workspace_bootstrap/NAMING.md` — Thread titles, codename map.
- `workspace_bootstrap/AUTOMATIONS.md` — Schedules and prompt texts.
- `workspace_bootstrap/REBUILD.md` — Runbook reference.
- `workspace_bootstrap/GUIDE_FOR_DAD.md` — Short version.
- `workspace_bootstrap/THREAD_SEEDS/*.md` — One seed per department.
- `diplomagic_backup_kit/` — `snapshot.sh`, `restore.sh`, `verify.sh`, README.

## TL;DR (10 steps)
1. Create a new Project Workspace named **DIPLOMAGIC GDD**.
2. Open **Instructions** and paste `INSTRUCTIONS.md` verbatim.
3. Create chats for departments in this order:
   Mail; Steam Ops; QA/UX; Combat & Systems; Authenticity & Research; Narrative & Canon; Publishing; Adversary & NPC Systems.
4. In each new chat, paste the matching file from `THREAD_SEEDS/` as the first message. Pin it.
5. Create an **Admin** chat. Paste `MEMORY.md`. Pin it.
6. In Mail, post the Stand‑by notice from its seed. Collect ACKs from each department. Then post Resume.
7. Restore or pull your local files from ZIP/Git. Confirm the repo remote is correct.
8. Optional: run `snapshot.sh` to create a baseline backup.
9. Recreate automations listed in `AUTOMATIONS.md`.
10. Validate using `CHECKLISTS/VALIDATION.md`.

## Department Seeding Order and Codenames
- Mail :: Integration & Validation — codename Postmaster
- Steam Operations — codename Stationmaster
- QA & UX — codename Exterminator
- Combat & Systems — codename Armorer
- Authenticity & Research — codename Archivist
- Narrative & Canon — codename Storymaster
- Publishing Studio — codename The Suit
- Adversary & NPC Systems — codename Taxonomist
- Macro Managers — Tech Support — nickname McMa (optional support thread)

## Quiet‑Period Protocol
- Stand‑by freezes non‑critical work.
- Critical hotfix requires Double Confirm: reply `y` then token `HOTFIX`.
- Mail posts Stand‑by and Resume templates included in the Mail seed.
- Keep ASCII‑safe paths and 72‑char wrap for mail templates.

## Naming Policy
- New office titles follow: `GDD Rebuild <YYYY-MM-DD HHmm ET>` using America/New_York.
- Use `NAMING.md` for consistent thread names and topology.

## Macro Sanity Check
- `ptstamp` returns the formatted project title string.
- `deptcode` returns:
  Department: Mail
  Codename: Postmaster.
- `mydept` returns the department codename line for the current chat.

## Backup and Restore (optional but recommended)
- Create a snapshot:
  ```bash
  bash diplomagic_backup_kit/snapshot.sh -s ~/projects/DIPLOMAGIC_GDD -n DIPLOMAGIC_GDD -o ~/backups -k 14
  ```
- Verify a snapshot:
  ```bash
  bash diplomagic_backup_kit/verify.sh ~/backups/DIPLOMAGIC_GDD/<timestamp>/archive.tar.gz
  ```
- Restore later:
  ```bash
  bash diplomagic_backup_kit/restore.sh ~/backups/DIPLOMAGIC_GDD/<timestamp>/archive.tar.gz ~/restore/DIPLOMAGIC_GDD
  ```

## Troubleshooting
- If departments do not ACK, re‑post the Mail seed and ensure the Stand‑by was pinned.
- If macros do not resolve, copy `MACROS.md` contents into an Admin note and test tokens.
- If naming diverges, correct titles to the policy above and proceed.
- Historical transcripts cannot be imported. Attach important exports as files in the relevant threads.

## Validation Checklist
- Instructions pasted and pinned.
- Admin thread seeded with MEMORY and pinned.
- All department chats created, seeded, and pinned.
- Stand‑by → ACKs → Resume cycle completed.
- Macros `ptstamp`, `deptcode`, `mydept` respond as defined.
- One baseline snapshot created with `snapshot.sh`.
- Git remote linked and pull clean.
- Naming visible on new threads.

## Versioning
- Tag the repo after rebuild: `bootstrap-<YYYYMMDD>`.
- Record OS, app version, and script versions in a `VERSIONS.txt` in the repo root.

---

Prepared for reproducible operations by combining the bootstrap kit with the backup scripts. Keep this guide alongside the bundle.

# itch_io_setup_wizard
**Macro name:** `itch_io_setup_wizard`  
**Trigger:** `wiz itch`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Project page, channels, builds via butler, privacy/keys, and release hygiene.  
**Risks:** Wrong project slug, bad archive layout, missing redistributables, HTML5 memory limits.

---

## Step 1 — Account and project creation
**Goal:** Create the Diplomagic project shell.

Actions
```text
• Sign in to itch.io.
• Create new project → Type: Game → Classification: Downloadable (and/or HTML5 if web demo).
• Title: DIPLOMAGIC. URL slug: diplomagic (adjust if taken).
• Visibility: Draft.
• Platforms: check Windows; add Linux/macOS only when verified.
```
Success: Draft page exists with the intended slug.  
Prompt: `y` / `n`.

---

## Step 2 — Page baseline
**Goal:** Minimum viable store page.

Actions
```text
• Upload cover image and 3–5 screenshots.
• Short text and long description. Add tags and genre.
• Pricing: Free (for demo) or set a price for full game later.
• Community: disable comments until moderation is ready.
• Save.
```
Success: Page saves without errors. Preview loads.  
Prompt: `y` / `n`.

---

## Step 3 — Channel plan
**Goal:** Decide deployment channels before first push.

Suggested channels
```text
windows-live      → public release
windows-beta      → invite-only testing
demo-windows      → public demo
html5             → web demo (optional)
```
Rule: one platform + intent per channel. Keep names ASCII-safe.  
Success: Channel names chosen.  
Prompt: `y` / `n`.

---

## Step 4 — Package the build
**Goal:** Create clean zips with proper layout.

Windows zip layout
```text
Diplomagic_Win64_v0.1.0.zip
  Diplomagic.exe
  /Content ... (game data)
  vcredist_x64.exe (optional) or note dependency in README.txt
  LICENSE.txt
  README.txt
```
Rules
```text
• No extra top-level folder inside the zip unless your engine needs it.
• ASCII paths only. Keep zip under 2–3 GB when possible.
• Include version in filename (SemVer or date).
```
Success: Zip created locally.  
Prompt: `y` / `n`.

---

## Step 5 — Install butler (CLI)
**Goal:** Have the itch.io uploader ready on the build machine.

Windows setup
```powershell
# Download butler from https://broth.itch.ovh/butler/
# Extract butler.exe somewhere on PATH, e.g. C:\Tools\butler\
butler -V
```
Expected: version prints.  
Prompt: `y` / `n`.

---

## Step 6 — Authenticate butler
**Goal:** Cache credentials for non-interactive pushes.

Options
```bash
butler login                     # opens browser once; caches token
# OR set env before CI:
# setx BUTLER_API_KEY "<your-api-key>"
```
Success: `butler whoami` shows your account.  
Prompt: `y` / `n`.

---

## Step 7 — First push (beta)
**Goal:** Upload zip to the beta channel.

Commands (replace account and slug)
```bash
butler push Diplomagic_Win64_v0.1.0.zip goldmanvision/diplomagic:windows-beta \
  --userversion v0.1.0
butler status goldmanvision/diplomagic
```
Expected: channel appears with build ID.  
Prompt: `y` / `n`.

---

## Step 8 — Promote to live
**Goal:** Make a public release when ready.

Options
```text
• Push to windows-live directly:
  butler push <zip> goldmanvision/diplomagic:windows-live --userversion v0.1.0
• Or use the project dashboard → Builds → Promote beta build to live channel.
```
Success: windows-live lists a build.  
Prompt: `y` / `n`.

---

## Step 9 — Demo channel
**Goal:** Provide a limited demo without affecting paid builds.

Actions
```bash
butler push Diplomagic_Demo_Win64_v0.1.0.zip goldmanvision/diplomagic:demo-windows \
  --userversion demo-0.1.0
```
Set page pricing/visibility so demo is public and full game remains paid or restricted.  
Success: Demo install works.  
Prompt: `y` / `n`.

---

## Step 10 — HTML5 web demo (optional)
**Goal:** Upload a web build folder.

Rules
```text
• Folder must contain index.html at its root.
• Keep total size small. Memory budgets are tight for web.
```
Command
```bash
butler push web_build_dir goldmanvision/diplomagic:html5 --userversion web-0.1.0
```
Success: Play in browser loads and runs.  
Prompt: `y` / `n`.

---

## Step 11 — Access control and keys
**Goal:** Control who can see and download.

Options
```text
• Keep page Draft for private review.
• Set Restricted and generate download keys for testers.
• Use “Press access keys” for media.
• Flip to Published when ready.
```
Success: Intended users can access the right channels.  
Prompt: `y` / `n`.

---

## Step 12 — Updates and rollback
**Goal:** Manage versions cleanly.

Commands
```bash
# New version to beta:
butler push <zip> goldmanvision/diplomagic:windows-beta --userversion v0.1.1
# Inspect channels/builds
butler status goldmanvision/diplomagic
```
Rollback: Use the dashboard → Builds → select prior build → Promote to channel.  
Success: Version history visible; correct build live.  
Prompt: `y` / `n`.

---

## Step 13 — Release hygiene
**Goal:** Keep installs stable and communicative.

Checklist
```text
• Include CHANGELOG.txt in each build.
• Keep save file location stable; document paths in README.
• If you ship redistributables, prefer on-demand web installers.
• Test install/uninstall on a clean VM before live.
```
Success: QA sign-off achieved.  
Prompt: `y` to finish, `n` for help on any sub-step.

---

## Troubleshooting quick refs
```text
• “No such channel” → typo in owner/slug/channel.
• “Nothing changed” → push zip after changing files or add --fix-permissions.
• “Game won’t start” → wrong zip root; .exe buried in subfolder.
• HTML5 black screen → memory too high or missing index.html.
```

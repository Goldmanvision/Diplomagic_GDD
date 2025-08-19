# steamworks_setup_wizard
**Macro name:** `steamworks_setup_wizard`  
**Trigger:** `wiz steam`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Store setup, depots/branches, SteamPipe builds, achievements, review, and go‑live.  
**Risks:** Rate limits, 2FA prompts, file path issues, asset spec drift. Avoid hard dates. Use ASCII‑safe paths.

---

## Step 1 — Access and roles
**Goal:** Ensure Partner access and correct permissions.

Actions
```text
• Sign in to Steamworks Partner site.
• Create or select the Diplomagic app. If not created, request an AppID.
• Add team members. Roles to grant:
  - Edit Store
  - Edit Marketing
  - Manage Pricing & Packages
  - Edit Steamworks Settings
  - Publish App Changes
  - Edit Depots & Builds
```
Success: AppID visible. Team listed with roles.  
Prompt: `y` to continue, `n` to fix.

---

## Step 2 — Store presence baseline
**Goal:** Create a minimally complete store page.

Actions
```text
• Fill App name, short description, long description.
• Upload capsule art per the current Steam UI (verify sizes on the page).
• Set categories/tags, content descriptors, supported languages.
• Set supported platforms (Windows first).
• Add at least 4 screenshots and 1 trailer placeholder (or skip trailer for now).
• Save as “Coming Soon” (not released).
```
Notes: Asset spec may change. Follow the on‑page requirements.  
Success: Store page saves without errors. “Coming Soon” visible in preview.  
Prompt: `y` / `n`.

---

## Step 3 — Packages and pricing
**Goal:** Define what customers buy.

Actions
```text
• Create the “Base Game” package and assign the AppID.
• Set regional pricing (use Steam’s suggested prices or set custom).
• Optional: Create a “Demo” or “Playtest” App and link to the store.
• Save.
```
Success: Base package shows a price table.  
Prompt: `y` / `n`.

---

## Step 4 — Branches and depots plan
**Goal:** Plan technical layout before builds.

Layout (suggested)
```text
Branches: public (default), beta, internal, demo
Depots:  win64 (content), win64_symbols (optional), demo_win64 (if using demo)
```
Rules
```text
• Keep binaries and PDBs separated (symbols depot optional).
• Use ASCII‑safe paths and stable root folder names.
```
Success: Branch and depot names decided.  
Prompt: `y` / `n`.

---

## Step 5 — Create depots
**Goal:** Define depots in Steamworks.

Actions
```text
• Steamworks → Depots → Add depot(s):
  - <APPID>: win64 (Windows 64‑bit content)
  - <APPID>: win64_symbols (optional)
  - <APPID>: demo_win64 (optional)
• For each depot, set OS = Windows.
```
Success: Depot IDs exist (note their numeric IDs).  
Prompt: `y` / `n`.

---

## Step 6 — Prepare SteamPipe build scripts (VDF)
**Goal:** Author VDF files for app build and depot mapping.

Create `scripts/app_build_<APPID>.vdf` (example):
```vdf
"AppBuild"
{
    "AppID"        "1234560"
    "Desc"         "CI build %DATE%"
    "BuildOutput"  "C:/build/_steampipe_out"
    "ContentRoot"  "C:/build/Diplomagic"   // repo staging root
    "SetLive"      "beta"                  // or "public", "internal"
    "Depots"
    {
        "1234561"  "scripts/depot_build_win64.vdf"
        // "1234562"  "scripts/depot_build_win64_symbols.vdf"
    }
}
```

Create `scripts/depot_build_win64.vdf`:
```vdf
"DepotBuildConfig"
{
    "DepotID"      "1234561"
    "ContentRoot"  "C:/build/Diplomagic"
    "FileMapping"
    {
        "LocalPath"  "*"
        "DepotPath"  "."
        "Recursive"  "1"
    }
    "FileExclusion"  "*.pdb"
}
```

(Optional) `scripts/depot_build_win64_symbols.vdf` excludes everything but symbols.  
Success: VDFs saved with correct numeric IDs and valid paths.  
Prompt: `y` / `n`.

---

## Step 7 — SteamCMD one‑time setup
**Goal:** Install `steamcmd` and cache Steam Guard on the build machine.

Actions
```bash
# Windows example
mkdir C:\steamcmd && cd C:\steamcmd
# Download steamcmd from official site and extract here.

# First interactive login once to cache sentry (avoid non‑interactive 2FA failures):
steamcmd +login <user> +quit
# Enter Steam Guard code when prompted.
```
Notes: Too many failed 2FA attempts trigger temporary locks. Keep this machine trusted.  
Success: Login completes without 2FA prompts on subsequent non‑interactive runs.  
Prompt: `y` / `n`.

---

## Step 8 — Run a test build to the beta branch
**Goal:** Upload content to Steam and set it live on `beta`.

Commands
```bash
# From a Windows shell (paths must match your VDFs)
"C:\steamcmd\steamcmd.exe" ^
  +login <user> <password> ^
  +run_app_build "C:\build\scripts\app_build_<APPID>.vdf" ^
  +quit
```
Checks
```text
• Build log in BuildOutput folder shows success.
• Steamworks → Builds shows a new build tied to the beta branch.
• Opt into the beta branch in Steam client and install.
```
Success: The beta branch downloads and runs.  
Prompt: `y` / `n`.

---

## Step 9 — Achievements, stats, and Steam Deck
**Goal:** Wire basic platform features.

Actions
```text
• Define Achievements (name, icon, API ID). Keep initial set small.
• If using stats/leaderboards, add entries and note API IDs.
• Steam Deck: declare support status and add a compatibility note if needed.
• Controller glyphs and input notes: confirm defaults or provide layout notes.
```
Success: Feature entries saved; IDs recorded in your design docs.  
Prompt: `y` / `n`.

---

## Step 10 — Visibility and review tasks
**Goal:** Prepare the page for public preview and later release.

Actions
```text
• Complete all store checklists until no blockers remain.
• Request page preview review if required by current policy.
• Keep “Coming Soon” live for wishlists until release is ready.
```
Notes: Policies and required checklists evolve. Work through the on‑page tasks until green.  
Success: No outstanding store checklist errors.  
Prompt: `y` / `n`.

---

## Step 11 — Playtest or Demo (optional but recommended)
**Goal:** Gather testers without exposing the full release.

Options
```text
• Steam Playtest app: gate access with requests; no price.
• Demo app: separate depot/branch; linked to the main store.
• Create beta keys for external testers if needed.
```
Success: Testers can install and run a limited build.  
Prompt: `y` / `n`.

---

## Step 12 — Pre‑release hardening
**Goal:** Lock settings and content paths before launch.

Checklist
```text
• Default branch → public. Beta stays for hotfixes.
• Verify packages → correct app + depots + pricing.
• Rebuild with final version number; tag in VCS.
• Enable crash reporting and logging flags for release build.
```
Success: Final RC build staged and downloadable from public branch (not yet released).  
Prompt: `y` / `n`.

---

## Step 13 — Go‑live
**Goal:** Publish without surprises.

Actions
```text
• Confirm store checklists are green.
• Press the release control per current Steamworks UI.
• Monitor downloads, crash telemetry, and reviews.
• If needed, hotfix: push to beta, test, then SetLive → public.
```
Success: Store is live. Build installs from public branch.  
Prompt: `y` to finish, `n` for help on any sub‑step.

---

## Troubleshooting quick refs
```text
• Build fails immediately → wrong paths in VDF or depot IDs.
• Clients can’t download → branch not SetLive or package missing depot.
• 2FA loop in CI → perform an interactive steamcmd login once on the runner.
• Store blocked → incomplete checklist item; open each section and resolve.
• Large patch size → review FileMapping and exclusions; keep symbols separate.
```

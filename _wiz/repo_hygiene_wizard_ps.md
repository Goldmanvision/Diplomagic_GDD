# Diplomagic GDD — Repository Hygiene Wizard (PowerShell)

**Purpose.** Clean duplicates, remove old MkDocs, stage UE5.6 structure, and sort docs per rules.
**Mode.** Step-by-step. After each step, reply `y` to continue or `n` to retry.

---

## Safety notes
- Creates a backup ZIP before any move.
- Uses `git mv` when possible to preserve history. Falls back to `Move-Item` + `git add` if file is untracked.
- All changes occur on a new branch: `hygiene/cleanup_{date}`.
- Nothing touches `/Archive`. MkDocs content is removed. SEC files go to `MASTER_GDD/`. Wizards go to `_wiz/`.
- Unreal directories are created empty and .gitignore is updated.

---

## Step 0 — Preconditions
```powershell
# Run in repo root PowerShell
git status
git remote -v
# Ensure clean worktree
if ((git status --porcelain).Trim().Length -ne 0) { throw "Uncommitted changes present. Commit or stash first." }
```

---

## Step 1 — Create branch and backup ZIP
```powershell
$stamp = Get-Date -Format "yyyyMMdd-HHmm"
$branch = "hygiene/cleanup_$stamp"
git switch -c $branch

# Backup (excludes .git folder). Adjust path if needed.
$zip = "backup_before_hygiene_$stamp.zip"
Compress-Archive -Path (Get-ChildItem -Force | Where-Object {$_.Name -ne '.git'}) -DestinationPath $zip -Force
Write-Host "Backup created: $zip"
```

---

## Step 2 — Helpers and target folders
```powershell
# Helper: test if a path is tracked by Git
function IsTracked([string]$p) { (git ls-files -- "$p") -ne "" }

# Helper: move preserving history if possible
function SafeMove([string]$src,[string]$dstDir) {
  if (!(Test-Path $src)) { return }
  if (!(Test-Path $dstDir)) { New-Item -ItemType Directory -Force -Path $dstDir | Out-Null }
  $name = Split-Path $src -Leaf
  $dst = Join-Path $dstDir $name
  if (IsTracked $src) { git mv -k -- "$src" "$dst" }
  else { Move-Item -Force -- "$src" "$dst" ; git add -A -- "$dst" }
}

# Targets
$WIZ = "_wiz"
$GDD = "MASTER_GDD"
$LEG = "legacy"
$UE  = @("Binaries","Config","Content","Plugins","Saved","Source")  # Intermediate is ignored

# Create targets
New-Item -ItemType Directory -Force -Path $WIZ,$GDD,$LEG | Out-Null
$UE | ForEach-Object { New-Item -ItemType Directory -Force -Path $_ | Out-Null }
```

---

## Step 3 — Move SEC-* into MASTER_GDD
```powershell
Get-ChildItem -LiteralPath . -Filter "SEC-*.md" -File | ForEach-Object {
  SafeMove $_.FullName $GDD
}
# Also catch SEC-epilogue.md if present
if (Test-Path ".\SEC-epilogue.md") { SafeMove ".\SEC-epilogue.md" $GDD }
```

---

## Step 4 — Collect wizards into _wiz
```powershell
$wizGlobs = @("*_wizard.md","*_wizard.docx","*wizard*.md","*wizard*.docx","*_wizard*.pdf")
foreach($g in $wizGlobs) {
  Get-ChildItem -Recurse -File -Include $g -ErrorAction SilentlyContinue | ForEach-Object {
    # keep existing sub-structure? for now flatten to _wiz top-level
    SafeMove $_.FullName $WIZ
  }
}
```

---

## Step 5 — Remove broken MkDocs and generated site artifacts
```powershell
# Entire old site tree
if (Test-Path ".\ops\site") { git rm -r -f -- ".\ops\site" }

# Root artifacts commonly from old exports
$rootArtifacts = @("index.html","sitemap.xml","sitemap.xml.gz","mirror.lst","mkdocs.yml","requirements.txt",
                   "deploy_ghpages.sh","deploy_with_cname_diplomagic.sh","setup.sh")
foreach($f in $rootArtifacts) { if (Test-Path $f) { git rm -f -- $f } }
```

---

## Step 6 — Park obvious legacy items to /legacy
```powershell
$legacyDirs = @("ascii-safe","_zips","mnt","Downloads","ci_validation_files")
$legacyFiles = @(
  "ascii-safe-*.zip","ascii-safe-mapping-*.md","dashboards_pack_*.zip",
  "Diplomagic_GDD_MkDocs_Starter.zip","python-*.exe","ci_validation_files.tar",
  ".tracked_md.lst",".report.csv","converted_index.csv","run.log","run_after_rerun.log",
  "manifest.csv","rename-map-*.csv"
)

foreach($d in $legacyDirs) { if (Test-Path $d) { SafeMove $d $LEG } }
foreach($g in $legacyFiles) {
  Get-ChildItem -File -Filter $g -ErrorAction SilentlyContinue | ForEach-Object { SafeMove $_.FullName $LEG }
}
```

---

## Step 7 — UE .gitignore hardening
```powershell
$ueIgnore = @"
# Unreal
/Intermediate/
/DerivedDataCache/
/Saved/
/Binaries/*
!/Binaries/README.keep
/Content/**/*.uasset
/Content/**/*.umap
*.VC.db
*.VC.opendb
*.sln
"@

# Ensure .gitignore contains entries (append once)
$gi = ".gitignore"
if (!(Test-Path $gi)) { New-Item -ItemType File $gi | Out-Null }
if (-not (Select-String -Path $gi -Pattern "# Unreal" -Quiet)) {
  Add-Content $gi "`r`n$ueIgnore"
}
# keep placeholder so empty Binaries/ can exist
$binKeep = ".\Binaries\README.keep"
if (!(Test-Path $binKeep)) { "placeholder" | Set-Content -Encoding utf8 $binKeep }
git add -A
```

---

## Step 8 — Commit and push
```powershell
git status
git commit -m "chore(hygiene): repo cleanup, remove old MkDocs, add UE scaffolding, organize SEC and wizards"
git push -u origin HEAD
```

---

## Step 9 — Open PR
```powershell
gh pr create --fill --base main --title "repo hygiene: structure cleanup + UE scaffolding"
```

---

## Step 10 — Post-checks
```powershell
# Quick tree of top-level
ls -Force | Select-Object Mode,Name,LastWriteTime,Length

# Confirm no ops/site remains
Test-Path .\ops\site

# Show MASTER_GDD and _wiz counts
(Get-ChildItem MASTER_GDD -File -ErrorAction SilentlyContinue).Count
(Get-ChildItem _wiz -File -ErrorAction SilentlyContinue).Count
```

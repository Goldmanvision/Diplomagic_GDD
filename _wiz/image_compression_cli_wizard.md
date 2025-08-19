# image_compression_cli_wizard
**Macro name:** `image_compression_cli_wizard`  
**Trigger:** `wiz compress-img`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Deterministic, offline optimization for PNG/JPEG/WebP; Windows-first with PowerShell helpers.  
**Risks:** Irreversible loss if you overwrite masters, color profile shifts, alpha loss on JPEG.

---

## Step 1 — Tools
**Goal:** Install CLI utilities.

Pick any:
```text
• pngquant  → lossy+dithering for PNG (quantization). Keep alpha.
• oxipng    → lossless PNG optimizer.
• mozjpeg   → cjpeg/jpegtran for high-quality JPEGs.
• webp      → cwebp/dwebp for WebP.
• (optional) ffmpeg for image2 sequences; ImageMagick for quick probes.
```
Windows: place EXEs in `F:\tools\img\bin\` and add that folder to PATH.  
Success: `pngquant --version` prints.  
Prompt: `y` / `n`.

---

## Step 2 — Repo layout
**Goal:** Stable locations and backups.
```
/assets/images/          # working images
/assets/_masters/        # uncompressed originals (never touched)
/ops/tools/img/          # scripts live here
```
Copy current originals to `_masters` before optimizing.  
Success: `_masters` populated.  
Prompt: `y` / `n`.

---

## Step 3 — PNG workflow
**Goal:** Smallest safe PNGs.

One-shot examples
```powershell
# lossy quantization (excellent default)
pngquant --speed 1 --quality=60-85 --force --output ".\out.png" ".\in.png"

# then lossless structural optimization
oxipng -o max --strip all --zopfli ".\out.png"
```

Batch PowerShell `ops/tools/img/opt_png.ps1`:
```powershell
param(
  [string]$In = ".\assets\images",
  [string]$Out = ".\assets\images"
)
$pngs = Get-ChildItem $In -Recurse -Include *.png
foreach ($f in $pngs) {
  $tmp = [System.IO.Path]::ChangeExtension([System.IO.Path]::GetTempFileName(), ".png")
  & pngquant --speed 1 --quality=60-85 --force --output $tmp -- "$($f.FullName)"
  if (!(Test-Path $tmp)) { continue }
  & oxipng -o max --strip all --zopfli -- $tmp | Out-Null
  if ((Get-Item $tmp).Length -lt (Get-Item $f.FullName).Length) {
    Copy-Item $tmp $f.FullName -Force
    Write-Host "PNG optimized: $($f.FullName)"
  } else {
    Remove-Item $tmp -Force
  }
}
```
Success: Sample PNG shrinks without visible artifacts.  
Prompt: `y` / `n`.

---

## Step 4 — JPEG workflow
**Goal:** High quality at smaller size. Never for alpha.

Examples (mozjpeg)
```powershell
# encode new JPEG
cjpeg -quality 82 -progressive -optimize -sample 2x2 -outfile out.jpg in.png

# lossless optimize existing
jpegtran -copy none -optimize -progressive -outfile out.jpg in.jpg
```
Batch PowerShell `ops/tools/img/opt_jpg.ps1`:
```powershell
param([string]$In = ".\assets\images")
$jpgs = Get-ChildItem $In -Recurse -Include *.jpg,*.jpeg
foreach ($f in $jpgs) {
  $tmp = [IO.Path]::ChangeExtension([IO.Path]::GetTempFileName(), ".jpg")
  & jpegtran -copy none -optimize -progressive -outfile $tmp -- "$($f.FullName)"
  if (Test-Path $tmp) {
    if ((Get-Item $tmp).Length -lt (Get-Item $f.FullName).Length) {
      Copy-Item $tmp $f.FullName -Force
      Write-Host "JPEG optimized: $($f.FullName)"
    } else { Remove-Item $tmp -Force }
  }
}
```
Success: JPEGs shrink and remain progressive.  
Prompt: `y` / `n`.

---

## Step 5 — WebP (optional)
**Goal:** Alt format for web docs only (do not replace store assets).

```powershell
# lossless from PNG
cwebp -lossless in.png -o out.webp

# quality target for photos
cwebp -q 82 in.jpg -o out.webp
```
Success: .webp smaller than original.  
Prompt: `y` / `n`.

---

## Step 6 — Bulk runner with safety
**Goal:** One entry point, logs, size guard, skip tiny files.

Create `ops/tools/img/opt_all.ps1`:
```powershell
param(
  [string]$Root = ".\assets\images",
  [int]$MinKB = 8,         # skip tiny files
  [switch]$DryRun
)
$log = ".\ops\tools\img\_opt_log.txt"
New-Item -ItemType File -Force $log | Out-Null

function Smaller($a,$b){ (Get-Item $a).Length -lt (Get-Item $b).Length }

# PNGs
Get-ChildItem $Root -Recurse -Include *.png | Where-Object { $_.Length/1KB -ge $MinKB } | ForEach-Object {
  $src = $_.FullName; $tmp = [IO.Path]::ChangeExtension([IO.Path]::GetTempFileName(), ".png")
  & pngquant --speed 1 --quality=60-85 --force --output $tmp -- "$src"
  if (Test-Path $tmp) { & oxipng -o max --strip all --zopfli -- $tmp | Out-Null }
  if (-not $DryRun -and (Test-Path $tmp) -and (Smaller $tmp $src)) {
    Copy-Item $tmp $src -Force; "PNG OK: $src" | Add-Content $log
  } else { if (Test-Path $tmp) { Remove-Item $tmp -Force } }
}

# JPEGs
Get-ChildItem $Root -Recurse -Include *.jpg,*.jpeg | Where-Object { $_.Length/1KB -ge $MinKB } | ForEach-Object {
  $src = $_.FullName; $tmp = [IO.Path]::ChangeExtension([IO.Path]::GetTempFileName(), ".jpg")
  & jpegtran -copy none -optimize -progressive -outfile $tmp -- "$src"
  if (-not $DryRun -and (Test-Path $tmp) -and (Smaller $tmp $src)) {
    Copy-Item $tmp $src -Force; "JPG OK: $src" | Add-Content $log
  } else { if (Test-Path $tmp) { Remove-Item $tmp -Force } }
}

Write-Host "Done. Log: $log"
```
Success: Log shows optimized files; originals in `_masters` remain.  
Prompt: `y` / `n`.

---

## Step 7 — CI guard (optional)
**Goal:** Fail PR if images grow too much.

`.github/workflows/img_guard.yml`:
```yaml
name: Image Guard
on: [pull_request]
jobs:
  guard:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: {fetch-depth: 0}
      - name: Check size deltas
        run: |
          set -e
          git diff --name-status origin/${{ github.base_ref }}... | awk '$1 ~ /A|M/ {print $2}' | \
          grep -Ei '\.(png|jpe?g|webp)$' | while read f; do
            sz=$(stat -c%s "$f" 2>/dev/null || echo 0)
            if [ "$sz" -gt 5242880 ]; then
              echo "Large image (>5MB): $f ($sz bytes)"; exit 1
            fi
          done
```
Success: Oversized images flag in PR checks.  
Prompt: `y` / `n`.

---

## Step 8 — Usage
**Goal:** Run safely.

```powershell
# one-off
powershell -File ops\tools\img\opt_png.ps1
powershell -File ops\tools\img\opt_jpg.ps1

# bulk with dry-run
powershell -File ops\tools\img\opt_all.ps1 -Root ".\assets\images" -DryRun

# bulk with write
powershell -File ops\tools\img\opt_all.ps1 -Root ".\assets\images"
```
Success: Size drops repo-wide with no visual regressions.  
Prompt: `y` to finish, `n` for help.

---

## Troubleshooting quick refs
```text
• “command not found” → add F:\tools\img\bin to PATH or use full paths.
• Alpha vanished → you encoded to JPEG; keep PNG/WebP for alpha.
• Bigger file after optimize → script keeps original if not smaller.
• Color shift → ensure color management off in viewer; prefer PNG for UI assets.
```

param(
  [string]$MapPath = "ops/maintenance/ascii-safe-mapping-20250817.md"
)

if (-not (Test-Path $MapPath)) {
  Write-Error "Mapping not found: $MapPath"
  exit 1
}

if (Test-Path "ascii-safe/ascii-safe-mapping-20250817.md") {
  New-Item -ItemType Directory -Force -Path "ops/maintenance" | Out-Null
  Move-Item -Force "ascii-safe/ascii-safe-mapping-20250817.md" $MapPath
}
if (Test-Path "ascii-safe-20250817.zip") {
  New-Item -ItemType Directory -Force -Path "ops/artifacts" | Out-Null
  Move-Item -Force "ascii-safe-20250817.zip" "ops/artifacts/"
}

$lines = Get-Content $MapPath
$lines = $lines | Select-Object -Skip 2  # skip header
foreach ($line in $lines) {
  $parts = $line -split '\|'
  if ($parts.Count -lt 3) { continue }
  $orig = $parts[1].Trim()
  $safe = $parts[2].Trim()
  if ([string]::IsNullOrWhiteSpace($orig) -or [string]::IsNullOrWhiteSpace($safe)) { continue }
  $target = $safe -replace '^ascii-safe/', ''

  $targetDir = Split-Path $target -Parent
  if ($targetDir) { New-Item -ItemType Directory -Force -Path $targetDir | Out-Null }

  if (Test-Path $safe) {
    try { git mv -f -- $safe $target | Out-Null } catch { Move-Item -Force -- $safe $target }
  }
  if ((Test-Path $orig) -and ($orig -ne $target)) {
    try { git rm -f -- $orig | Out-Null } catch { Remove-Item -Force -- $orig }
  }
  Write-Output "Moved: $safe -> $target; removed: $orig"
}

Write-Output "Done. Review with: git status"

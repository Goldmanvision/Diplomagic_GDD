# zip_repo_winrar.ps1
$ErrorActionPreference = 'Stop'

$RAR = 'C:\Program Files\WinRAR\Rar.exe'
$RepoDir = 'F:\Diplomagic_GDD_MASTER\Updated_GDD\Diplomagic_GDD_git'
$OutDir  = Join-Path $RepoDir '_zips'
if (-not (Test-Path $RAR)) { throw "Rar.exe not found at $RAR" }
if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }

$ts = Get-Date -Format 'yyyyMMdd_HHmmss'
$Archive = Join-Path $OutDir "Diplomagic_GDD_$ts.zip"

Push-Location (Split-Path $RepoDir -Parent)
& $RAR a -afzip -r -m5 -idq -ep1 `
  -x"Diplomagic_GDD_git\_zips\*" `
  -x"Diplomagic_GDD_git\.git\*" `
  -x"Diplomagic_GDD_git\node_modules\*" `
  -x"Diplomagic_GDD_git\artifacts\*" `
  -x"Diplomagic_GDD_git\ci-artifacts\*" `
  -x"Diplomagic_GDD_git\*.zip" `
  $Archive "Diplomagic_GDD_git\"
$rc = $LASTEXITCODE
Pop-Location

if ($rc -ne 0) {
  throw "WinRAR failed with code $rc"
} else {
  Write-Host "Archive created: $Archive"
}

param(
  [string]$Repo = "F:\Diplomagic_GDD_MASTER\Updated_GDD\Diplomagic_GDD_git"
)

# zip_repo_7z.ps1
# Usage: .\zip_repo_7z.ps1 [-Repo "F:\path\to\repo"]

if (-not (Test-Path -LiteralPath $Repo)) {
  Write-Error "Repo path not found: $Repo"
  exit 2
}

# Locate 7z.exe
$sevenZip = $null
$defaultPaths = @(
  "C:\Program Files\7-Zip\7z.exe",
  "C:\Program Files (x86)\7-Zip\7z.exe"
)
foreach ($p in $defaultPaths) {
  if (Test-Path -LiteralPath $p) { $sevenZip = $p; break }
}
if (-not $sevenZip) {
  $cmd = Get-Command 7z.exe -ErrorAction SilentlyContinue
  if ($cmd) { $sevenZip = $cmd.Source }
}
if (-not $sevenZip) {
  Write-Error "7z.exe not found. Install 7-Zip or add it to PATH."
  exit 3
}

$ts = Get-Date -Format yyyyMMdd_HHmmss
$zipDir = Join-Path $Repo "_zips"
if (-not (Test-Path -LiteralPath $zipDir)) { New-Item -ItemType Directory -Path $zipDir | Out-Null }
$archive = Join-Path $zipDir ("Diplomagic_GDD_{0}.zip" -f $ts)

Push-Location $Repo
try {
  Write-Host "Creating `"$archive`" ..."
  $args = @(
    'a','-tzip',$archive,'.\*','-mx=5',
    '-xr!_zips\*','-xr!.git\*','-xr!node_modules\*','-xr!artifacts\*','-xr!ci-artifacts\*','-x!*.zip'
  )
  $p = Start-Process -FilePath $sevenZip -ArgumentList $args -NoNewWindow -Wait -PassThru
  if ($p.ExitCode -ne 0) {
    Write-Error "7-Zip failed with code $($p.ExitCode)."
    exit $p.ExitCode
  }
  Write-Host "Archive created: $archive"
} finally {
  Pop-Location
}
exit 0

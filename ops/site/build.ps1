Param(
  [Parameter(Mandatory=$true)][ValidateSet('sync','serve','build','clean')]$Cmd
)

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = (Resolve-Path (Join-Path $Here '..\..')).Path
$Docs = Join-Path $Here 'docs'

function Sync-Files {
  New-Item -ItemType Directory -Force -Path $Docs | Out-Null
  Get-Content (Join-Path $Here 'mirror.lst') | ForEach-Object {
    $line = $_.Trim()
    if ($line -eq '' -or $line.StartsWith('#')) { return }
    $src = Join-Path $Root $line
    $dst = Join-Path $Docs $line
    New-Item -ItemType Directory -Force -Path (Split-Path $dst) | Out-Null
    Copy-Item -Force $src $dst
  }
  Write-Host 'Synced files to docs/'
}

switch ($Cmd) {
  'sync'  { Sync-Files }
  'serve' { Sync-Files; Set-Location $Here; mkdocs serve }
  'build' { Sync-Files; Set-Location $Here; mkdocs build }
  'clean' { Remove-Item -Recurse -Force (Join-Path $Here 'site') -ErrorAction Ignore; Write-Host 'Cleaned site/' }
}

Param(
  [string]$Dept = "Mail Department",
  [string]$Codename = "Postmaster",
  [string]$Suffix = "Ops Thread 2",
  [string]$Channel = "#ops",
  [string]$Link = "/DECISIONS.md",
  [string]$Note = ""
)
$Date = Get-Date -Format "yyyy-MM-dd"
$Slug = ($Dept.ToLower() -replace '[^a-z0-9]+','-').Trim('-')
$OutDir = "ops/reports"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$Cork = @"
ptcork v2
title: $Dept rollover
channel: $Channel
content: $Dept is moving to "$Codename — $Suffix" due to log size. Old thread enters naptime. All routing and logs continue in the new thread. Double-Confirm remains for multi-file batches. $Note
link: $Link
---
"@
$CorkPath = Join-Path $OutDir ("ptcork_{0}_rollover_{1}.md" -f $Slug,$Date)
$Cork | Out-File -Encoding utf8 $CorkPath

$Decision = "## $Date`n- $Dept chat rollover to `"$Codename — $Suffix`"; prior thread archived with naptime; routing unchanged.`n"
Add-Content -Encoding utf8 -Path "DECISIONS.md" -Value $Decision

git add "DECISIONS.md" $CorkPath
Write-Host "Created:" $CorkPath

param(
  [string]$Owner = "Postmaster",
  [string]$Scope = "global",
  [string]$Note = "Resume"
)
$ts = (Get-Date).ToString("yyyy-MM-dd")
Add-Content CHANGELOG.md "changelog-entry: $ts | mail/global | Quiet Period | end | Scope=$Scope"
Write-Host "UNCORKED: $Note ($Scope)"

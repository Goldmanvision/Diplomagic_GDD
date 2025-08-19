param(
  [string]$Owner = "Postmaster",
  [string]$Scope = "global",
  [string]$Reason = "Quiet Period"
)
$ts = (Get-Date).ToString("yyyy-MM-dd")
Add-Content DECISIONS.md "decision-entry: $ts | $Reason | ACK | Owner=$Owner | Scope=$Scope"
Add-Content CHANGELOG.md "changelog-entry: $ts | mail/global | $Reason | start | Scope=$Scope"
Write-Host "CORKED: $Reason ($Scope)"

param([string]$Tag="pre-change")
$ts = (Get-Date).ToString("yyyyMMdd-HHmm")
git tag "$Tag-$ts"
git push origin "$Tag-$ts"
Write-Host "Tagged $Tag-$ts"

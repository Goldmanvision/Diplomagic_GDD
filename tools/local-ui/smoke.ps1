$ErrorActionPreference = 'Stop'
$exe = Join-Path $PSScriptRoot '..\dist\windows\bundle\daps.exe'
$proc = Start-Process -FilePath $exe -PassThru
try {
  Start-Sleep -Seconds 3
  $resp = Invoke-WebRequest -Uri 'http://127.0.0.1:8000/health' -UseBasicParsing
  if ($resp.StatusCode -ne 200) { throw "health check failed" }
  $json = $resp.Content | ConvertFrom-Json
  if (-not $json.ok) { throw "ok flag false" }
}
finally {
  Stop-Process -Id $proc.Id -Force
}

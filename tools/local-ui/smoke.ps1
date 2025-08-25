param(
    [string]$ExePath = "dist/windows/daps.exe",
    [string]$Url = "http://127.0.0.1:5174/health"
)

Write-Host "Launching DAPS smoke test..."

if (-Not (Test-Path $ExePath)) {
    Write-Error "Executable not found: $ExePath"
    exit 1
}

# Start the exe
$proc = Start-Process -FilePath $ExePath -PassThru

Start-Sleep -Seconds 5

try {
    $resp = Invoke-RestMethod -Uri $Url -TimeoutSec 10
    if ($resp.ok -ne $true) {
        Write-Error "Health endpoint did not return ok=true"
        Stop-Process -Id $proc.Id -Force
        exit 1
    }
    Write-Host "Smoke test passed."
}
catch {
    Write-Error "Smoke test failed: $_"
    Stop-Process -Id $proc.Id -Force
    exit 1
}

Stop-Process -Id $proc.Id -Force
exit 0

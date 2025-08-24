Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

# Backend
Start-Process -NoNewWindow -FilePath "cmd.exe" -ArgumentList '/c', '.\run_backend.bat'

# Frontend
Push-Location .\frontend
if (!(Test-Path .\node_modules)) { npm ci }
Start-Process -NoNewWindow -FilePath "npx" -ArgumentList "vite", "--port", "5173"
Pop-Location

Write-Host "Backend: http://127.0.0.1:5174/health"
Write-Host "Frontend: http://127.0.0.1:5173"

@echo off
setlocal
REM zip_repo_7z.cmd - wrapper to run zip_repo_7z.ps1 with pwsh or Windows PowerShell
if exist "%ProgramFiles%\PowerShell\7\pwsh.exe" (
  "%ProgramFiles%\PowerShell\7\pwsh.exe" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0zip_repo_7z.ps1" %*
) else (
  powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0zip_repo_7z.ps1" %*
)
endlocal

@echo off
REM zip_repo_7z_fix.bat — zip the repo using 7-Zip if present, else PowerShell Compress-Archive.
setlocal ENABLEDELAYEDEXPANSION

REM === Repo root ===
set "REPO_DIR=F:\Diplomagic_GDD_MASTER\Updated_GDD\Diplomagic_GDD_git"

REM === Timestamp and output ===
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do set "YYYY=%%d" & set "MM=%%b" & set "DD=%%c"
set "HH=%time:~0,2%"
set "MI=%time:~3,2%"
set "SS=%time:~6,2%"
set "HH=0%HH%"
set "HH=%HH:~-2%"
set "STAMP=%YYYY%%MM%%DD%_%HH%%MI%%SS%"
set "OUT_DIR=%REPO_DIR%\_zips"
if not exist "%OUT_DIR%" mkdir "%OUT_DIR%"
set "ZIP_PATH=%OUT_DIR%\Diplomagic_GDD_%STAMP%.zip"

echo Repo: "%REPO_DIR%"
echo Out : "%ZIP_PATH%"
echo.

REM Locate 7-Zip
set "SEVENZ="
where 7z >nul 2>nul && set "SEVENZ=7z"
if not defined SEVENZ if exist "C:\Program Files\7-Zip\7z.exe" set "SEVENZ=C:\Program Files\7-Zip\7z.exe"
if not defined SEVENZ if exist "C:\Program Files (x86)\7-Zip\7z.exe" set "SEVENZ=C:\Program Files (x86)\7-Zip\7z.exe"

if defined SEVENZ (
  echo Using 7-Zip: %SEVENZ%
  pushd "%REPO_DIR%" >nul
  REM Single-line call to avoid caret parsing issues. Exclude recursive dirs and common large types.
  "%SEVENZ%" a -tzip "%ZIP_PATH%" * -xr!.git\* -xr!node_modules\* -xr!artifacts\* -xr!ci-artifacts\* -xr!_zips\* -x!*.psd -x!*.wav -x!*.mp4 -x!*.zip
  set RC=%ERRORLEVEL%
  popd >nul
  if %RC% EQU 0 (
    echo Created: "%ZIP_PATH%"
    exit /b 0
  ) else (
    echo 7-Zip failed with code %RC%. Falling back to PowerShell...
  )
) else (
  echo 7-Zip not found. Falling back to PowerShell...
)

REM PowerShell fallback with excludes
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$src='F:\Diplomagic_GDD_MASTER\Updated_GDD\Diplomagic_GDD_git';" ^
  "$outDir=Join-Path $src '_zips'; if(-not(Test-Path $outDir)){ New-Item -ItemType Directory -Path $outDir | Out-Null };" ^
  "$out=Join-Path $outDir ('Diplomagic_GDD_{0}.zip' -f (Get-Date -Format 'yyyyMMdd_HHmmss'));" ^
  "$excludeRe='\\\.git\\\|\\\node_modules\\\|\\\artifacts\\\|\\\ci-artifacts\\\|\\\_zips\\\|\.psd$|\.(wav|mp4|zip)$';" ^
  "$files=Get-ChildItem -LiteralPath $src -Recurse -File | Where-Object { $_.FullName -notmatch $excludeRe } | ForEach-Object { $_.FullName };" ^
  "Compress-Archive -Path $files -DestinationPath $out -Force;" ^
  "Write-Host ('Created: ' + $out)"
exit /b %ERRORLEVEL%

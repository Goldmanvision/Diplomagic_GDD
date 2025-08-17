@echo off
setlocal

rem --- paths ---
set "RAR=C:\Program Files\WinRAR\Rar.exe"
set "REPO_DIR=F:\Diplomagic_GDD_MASTER\Updated_GDD\Diplomagic_GDD_git"
set "OUT_DIR=%REPO_DIR%\_zips"

if not exist "%RAR%" (
  echo ERROR: Rar.exe not found at "%RAR%".
  exit /b 2
)

if not exist "%OUT_DIR%" mkdir "%OUT_DIR%"

for /f "delims=" %%I in ('powershell -NoProfile -Command "(Get-Date).ToString('yyyyMMdd_HHmmss')"') do set "TS=%%I"
set "ARCHIVE=%OUT_DIR%\Diplomagic_GDD_%TS%.zip"

rem --- zip the repo as a top-level folder, exclude heavy dirs/files ---
pushd "%REPO_DIR%\.."
"%RAR%" a -afzip -r -m5 -idq -ep1 ^
  -x"Diplomagic_GDD_git\_zips\*" ^
  -x"Diplomagic_GDD_git\.git\*" ^
  -x"Diplomagic_GDD_git\node_modules\*" ^
  -x"Diplomagic_GDD_git\artifacts\*" ^
  -x"Diplomagic_GDD_git\ci-artifacts\*" ^
  -x"Diplomagic_GDD_git\*.zip" ^
  "%ARCHIVE%" "Diplomagic_GDD_git\"
set "RC=%ERRORLEVEL%"
popd

if %RC% neq 0 (
  echo WinRAR failed with code %RC%.
  exit /b %RC%
)

echo Archive created: %ARCHIVE%
pause

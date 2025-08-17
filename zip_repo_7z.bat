@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

REM zip_repo_7z.bat
REM Usage: zip_repo_7z.bat [RepoPath]
REM If RepoPath is omitted, defaults to the user's repo path.

set "REPO=F:\Diplomagic_GDD_MASTER\Updated_GDD\Diplomagic_GDD_git"
if not "%~1"=="" set "REPO=%~1"

if not exist "%REPO%" (
  echo ERROR: Repo path not found: "%REPO%"
  exit /b 2
)

REM Resolve 7z.exe
set "SEVENZIP="
for %%P in ("C:\Program Files\7-Zip\7z.exe" "C:\Program Files (x86)\7-Zip\7z.exe") do (
  if exist "%%~P" set "SEVENZIP=%%~P"
)
if not defined SEVENZIP (
  for /f "delims=" %%Q in ('where 7z.exe 2^>nul') do (
    set "SEVENZIP=%%~Q"
    goto :sz_found
  )
)
:sz_found
if not defined SEVENZIP (
  echo ERROR: 7z.exe not found. Install 7-Zip or add it to PATH.
  exit /b 3
)

REM Timestamp via PowerShell
for /f %%T in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"') do set "TS=%%T"

set "ZIPDIR=%REPO%\_zips"
if not exist "%ZIPDIR%" mkdir "%ZIPDIR%"

set "ARCHIVE=%ZIPDIR%\Diplomagic_GDD_%TS%.zip"

pushd "%REPO%" >nul
echo Creating "%ARCHIVE%" ...
"%SEVENZIP%" a -tzip -r "%ARCHIVE%" ".\*" -mx=5 ^
 -xr!_zips\* -xr!.git\* -xr!node_modules\* -xr!artifacts\* -xr!ci-artifacts\* -x!*.zip
set "RC=%ERRORLEVEL%"
popd >nul

if not "%RC%"=="0" (
  echo ERROR: 7-Zip failed with code %RC%.
  exit /b %RC%
)

echo Archive created: "%ARCHIVE%"
exit /b 0

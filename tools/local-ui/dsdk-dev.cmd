@echo off
setlocal
rem DIPLOMAGIC SDK dev launcher
cd /d "%~dp0"

rem Ports
set "DMG_FE_PORT=5173"
set "DMG_BE_PORT=5174"

rem Start backend in its own window (uses venv and reload-exclude)
start "DIPLOMAGIC Backend" cmd /k call "%~dp0run_backend.bat"

rem Pick npm
set "NPM=npm"
if exist "%ProgramFiles%\nodejs\npm.cmd" set "NPM=%ProgramFiles%\nodejs\npm.cmd"

rem Start frontend in its own window
start "DIPLOMAGIC Frontend" cmd /k pushd "%~dp0frontend" ^& "%NPM%" i ^& "%NPM%" run dev -- --port %DMG_FE_PORT%

rem Open browser tabs
timeout /t 3 /nobreak >nul
start "" "http://localhost:%DMG_FE_PORT%/"
start "" "http://127.0.0.1:%DMG_BE_PORT%/health"

echo Launched backend and frontend. You can close this window.
exit /b 0

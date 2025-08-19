@echo off
set SH="%ProgramFiles%\Git\bin\sh.exe"
if exist %SH% ( %SH% ".githooks/commit-msg" %1 ) else ( echo Git Bash not found & exit /b 1 )

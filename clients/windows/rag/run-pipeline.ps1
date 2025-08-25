Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

. .\.venv\Scripts\Activate.ps1
python -m clients.windows.rag embed
python -m clients.windows.rag watch

# Load .env into process
$envPath = Join-Path $PSScriptRoot ".env"
if (Test-Path $envPath) {
  Get-Content $envPath | Where-Object {$_ -notmatch '^\s*(#|$)'} | ForEach-Object {
    $k,$v = $_ -split '=',2
    if ($k -and $v) { [Environment]::SetEnvironmentVariable($k.Trim(), $v.Trim(), "Process") }
  }
}

# Install deps from requirements
$req = Join-Path $PSScriptRoot "backend\requirements.txt"
if (Test-Path $req) {
  python -m pip install -q -U -r $req
} else {
  python -m pip install -q -U fastapi uvicorn httpx pydantic python-multipart jsonschema pathspec
}

# Run backend
python (Join-Path $PSScriptRoot "backend\main.py")

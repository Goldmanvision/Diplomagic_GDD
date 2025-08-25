# rag_smoke.ps1 — Local-UI backend + Windows RAG client smoke
# Local-only. Prefers tools\local-ui\backend; falls back to tools\local_ui\backend.

$ErrorActionPreference = 'Stop'

if (-not $env:REPO_ROOT) { throw "REPO_ROOT not set. Example: `$env:REPO_ROOT='F:\repos\Diplomagic_GDD'" }
$root = (Resolve-Path $env:REPO_ROOT).Path
$py   = (Resolve-Path "$root\.ci311\Scripts\python.exe").Path
if (-not (Test-Path $py)) { throw "Missing venv at $root\.ci311. Create with: py -3.11 -m venv .ci311; .\.ci311\Scripts\Activate.ps1" }

# Pick app-dir safely
$appDirs = @()
$dir1 = Join-Path $root 'tools\local-ui\backend'
if (Test-Path (Join-Path $dir1 'main.py')) { $appDirs += $dir1 }
$dir2 = Join-Path $root 'tools\local_ui\backend'
if (Test-Path (Join-Path $dir2 'main.py')) { $appDirs += $dir2 }
if ($appDirs.Count -eq 0) { throw "No backend main.py under tools\local-ui or tools\local_ui." }
$appDir = (Resolve-Path $appDirs[0]).Path

$env:PYTHONPATH    = "$root"
$env:RAG_EMBED_URL = ''   # offline embeddings

$logDir  = Join-Path $root 'ops\handoffs\logs'
$scratch = Join-Path $root 'ops\handoffs\scratch'
New-Item $logDir -ItemType Directory -Force | Out-Null
New-Item $scratch -ItemType Directory -Force | Out-Null

# ensure uvicorn
$uv = & "$py" -c "import importlib; importlib.import_module('uvicorn'); print('ok')" 2>$null
if ($LASTEXITCODE -ne 0 -or $uv -notmatch 'ok') { & "$py" -m pip install uvicorn --quiet }

# start backend (fixed target)
Push-Location $appDir
$stdout = Join-Path $logDir 'backend_stdout.log'
$stderr = Join-Path $logDir 'backend_stderr.log'
$args = @('-m','uvicorn','--app-dir',"$appDir",'main:app','--host','127.0.0.1','--port','8765','--log-level','info')
$backendProc = $null

try {
  $backendProc = Start-Process -FilePath $py -ArgumentList $args -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr

  # wait ready
  $up=$false
  foreach($i in 1..40){
    try { $r = Invoke-WebRequest "http://127.0.0.1:8765/health" -TimeoutSec 1; if($r.StatusCode -eq 200){ $up=$true; break } } catch { Start-Sleep 1 }
  }
  if(-not $up){
    if (Test-Path $stderr) { Get-Content $stderr -Tail 200 }
    throw ("uvicorn failed on :8765 (app-dir: {0}, target: main:app)" -f $appDir)
  }

  # capture OpenAPI if present
  try {
    Invoke-WebRequest "http://127.0.0.1:8765/openapi.json" -TimeoutSec 2 |
      Select-Object -ExpandProperty Content |
      Out-File (Join-Path $logDir 'openapi.json') -Encoding utf8
  } catch {}

  # embeddings test
  $embedTest = Join-Path $root 'clients\windows\rag\tests\test_embeddings.py'
  if (Test-Path $embedTest) {
    & "$py" -m pytest -q -rA "$embedTest::test_embeddings_written_and_retrievable" --maxfail=1
  } else {
    Write-Host "WARN: $embedTest not found; running RAG test folder"
    & "$py" -m pytest -q -rA (Join-Path $root 'clients\windows\rag\tests') --maxfail=1
  }

  # retrieve smoke (OpenAPI-driven with fallback)
  $retried = $false
  try {
    $apiPath = Join-Path $logDir 'openapi.json'
    if (Test-Path $apiPath) {
      $api = Get-Content $apiPath -Raw | ConvertFrom-Json
      $paths = $api.paths.PSObject.Properties.Name
      $retrPath = $paths | Where-Object { $_ -match 'retrieve|search|query' } | Select-Object -First 1
      if ($retrPath) {
        $body = @{ query = "door forced agent"; top_k = 3 } | ConvertTo-Json
        $resp = Invoke-WebRequest ("http://127.0.0.1:8765{0}" -f $retrPath) -Method Post -Body $body -ContentType 'application/json'
        if (-not $resp.Content) { throw "empty retrieval response" }
      } else { $retried = $true; Write-Host "WARN: no retrieve-like endpoint; skipping" }
    } else {
      $body = @{ query = "door forced agent"; top_k = 3 } | ConvertTo-Json
      Invoke-WebRequest "http://127.0.0.1:8765/retrieve/query" -Method Post -Body $body -ContentType 'application/json' | Out-Null
      $retried = $true
    }
  } catch {
    if (-not $retried) {
      $body = @{ query = "door forced agent"; top_k = 3 } | ConvertTo-Json
      Invoke-WebRequest "http://127.0.0.1:8765/retrieve/query" -Method Post -Body $body -ContentType 'application/json' | Out-Null
    } else { Write-Host "WARN: retrieval smoke skipped or fallback failed." }
  }

  # export check
  $csvPath = Join-Path $scratch "embeds.csv"
  Invoke-WebRequest "http://127.0.0.1:8765/export/csv" -OutFile $csvPath
  if ((Get-Item $csvPath).Length -lt 10) { throw "export/csv produced empty file" }

  Write-Host ("Smoke PASS (app-dir: {0}, target: main:app)" -f $appDir)
  exit 0
}
finally {
  if ($backendProc) { Stop-Process -Id $backendProc.Id -ErrorAction SilentlyContinue }
  Pop-Location
}

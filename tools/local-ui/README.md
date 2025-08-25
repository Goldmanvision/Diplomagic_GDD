# Prompt Hub MVP (stubbed)

**Extract this zip into `tools/local-ui\\`.** It will create:
```
tools/local-ui/
  backend/main.py
  frontend/index.html
  frontend/app.js
  frontend/styles.css
  run_backend.bat
  README.md
```

## Run
```powershell
# from repo root or tools\local-ui
tools\local-ui\run_backend.bat    # starts 127.0.0.1:5174
# frontend: open tools\local-ui\frontend\index.html
# optional dev server:
#   cd tools\local-ui\frontend; npx vite  (http://127.0.0.1:5173)
```

## Windows bundle
System requirements: Windows 10 or later, 64-bit.

The build script compiles the backend into a standalone `daps.exe` and assembles all
runtime assets into a single zip file. Build locally with:

```bash
python -m pip install -r tools/local-ui/backend/requirements.txt pyinstaller
python tools/local-ui/build_bundle.py
```

The archive will be created at `tools/local-ui/dist/daps_bundle.zip`. Extract it on
Windows and run `daps.exe` to start the API (127.0.0.1:5174); open
`frontend/index.html` to use the UI.


## Windows installer
After building the bundle you can package it into an installer
(`daps-installer.exe`) with a tool such as Inno Setup or NSIS. Sign the installer
to reduce Windows SmartScreen warnings.

1. Create `tools/local-ui/certs/` and place your code-signing certificate
   (`daps.pfx`) and any intermediate `.cer` files there. Keep this directory out
   of version control.
2. Use SignTool (from the Windows SDK) to sign and verify the installer:

```powershell
signtool sign /fd sha256 /tr http://timestamp.digicert.com /td sha256 \
  /f tools\\local-ui\\certs\\daps.pfx /p <PASSWORD> tools\\local-ui\\dist\\daps-installer.exe
signtool verify /pa tools\\local-ui\\dist\\daps-installer.exe
```

Replace `<PASSWORD>` with the certificate password.


## Behavior
- Single input, output feed, quick actions (Yes/No/Retry).
- Agent strip, unread counts, deep link `?agent=<name>`.
- Per-agent drafts in localStorage.
- Rate guard ≤6 req/min/agent and 1 inflight/agent.
- Outbox JSONL at `tools/local-ui/_outbox/outbox.jsonl` via `/outbox` and `/outbox/tail`.
- Feed keeps last 200 entries.

## Tests
```bash
# from repo root
python -m pip install -r tools/local-ui/backend/requirements.dev.txt
python -m pytest tools/local-ui/backend/tests
```
The API tests require `fastapi` and will be skipped automatically if it is not installed.

CI tick: 2025-08-24T15:54:35

## CI bypass
The `local-ui-pack` workflow runs backend tests and packages the UI. To skip packaging while keeping the backend tests:

- Commit: include `[skip local-ui-pack]` in a commit message.
- PR: add a `skip-local-ui-pack` label.
- Manual: run the local-ui-pack workflow with `skip_checks=true`.

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

## Behavior
- Single input, output feed, quick actions (Yes/No/Retry).
- Agent strip, unread counts, deep link `?agent=<name>`.
- Per-agent drafts in localStorage.
- Rate guard ≤6 req/min/agent and 1 inflight/agent.
- Outbox JSONL at `tools/local-ui/_outbox/outbox.jsonl` via `/outbox` and `/outbox/tail`.
- Feed keeps last 200 entries.

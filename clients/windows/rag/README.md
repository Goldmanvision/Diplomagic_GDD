# Windows RAG utilities

This folder contains helper scripts for generating embeddings from saved
Workthread logs.

## Installation

Create a virtual environment and install the requirements:

```bash
pip install -r requirements.txt
```

If you see `ModuleNotFoundError: watchdog` when running `watch_logs.py`, it
means the optional `watchdog` package is missing. Install the dependencies as
shown above.

## CLI

The tools can be invoked through the package itself:

```bash
python -m clients.windows.rag embed            # Embed existing logs
python -m clients.windows.rag watch            # Start log watcher
python -m clients.windows.rag query "text"     # Retrieve similar lines
```

Use `--log-dir` and `--db-dir` to override the default paths (`ops/handoffs/logs`
and `ops/handoffs`).

## PowerShell helpers

For Windows users the following scripts simplify setup and execution:

- `install-deps.ps1` – create a virtual environment and install dependencies.
- `run-pipeline.ps1` – embed any existing logs then start the watcher.

Run them from PowerShell using `./install-deps.ps1` and `./run-pipeline.ps1`.

## Troubleshooting

- Include `[skip local-ui]` in a commit message to bypass the local UI workflow.
- Ensure `watchdog` is installed if the watcher fails to start.
- Delete the database in `ops/handoffs` if embeddings become inconsistent.

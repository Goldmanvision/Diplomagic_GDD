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

## Scripts

- `embed_logs.py` – embed existing transcripts.
- `watch_logs.py` – monitor the log directory and stream new lines into the
  transcript and vector index.

"""Embed existing log files using a local embedding model.

This script demonstrates how logs could be embedded. It does not depend on
watchdog but lives alongside ``watch_logs.py``.
"""

import subprocess
from pathlib import Path

LOG_DIR = Path("ops/handoffs/logs")


def embed_file(path: Path) -> None:
    """Run ``ollama embed`` on ``path`` if available."""
    try:
        subprocess.run(["ollama", "embed", str(path)], check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"Embedding failed for {path}: {exc}")


def main() -> None:
    for log in LOG_DIR.glob("*.log"):
        embed_file(log)


if __name__ == "__main__":
    main()

"""Embed existing log files using a local embedding model.

This script demonstrates how logs could be embedded. It does not depend on
watchdog but lives alongside ``watch_logs.py``.
"""

import subprocess
import sqlite3
from pathlib import Path

LOG_DIR = Path("ops/handoffs/logs")
DB_PATH = LOG_DIR / "embeddings.db"


def write_embedding_to_db(path: Path) -> None:
    """Persist embedding metadata for *path* in a SQLite database."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS embeddings (file TEXT UNIQUE)"
        )
        conn.execute("INSERT OR REPLACE INTO embeddings(file) VALUES (?)", (str(path),))


def embed_file(path: Path) -> None:
    """Run ``ollama embed`` on ``path`` if available."""
    try:
        subprocess.run(["ollama", "embed", str(path)], check=True)
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"Embedding failed for {path}: {exc}")
        return

    try:
        write_embedding_to_db(path)
    except sqlite3.DatabaseError as exc:
        print(f"Failed to write embedding for {path}: {exc}")


def main() -> None:
    for log in LOG_DIR.glob("*.log"):
        embed_file(log)


if __name__ == "__main__":
    main()

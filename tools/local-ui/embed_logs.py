"""Embed log files and persist vectors for retrieval."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sqlite3
from pathlib import Path
from typing import Optional
import time
import uuid

import db

LOG_DIR = Path("ops/handoffs/logs")
DB_PATH = LOG_DIR / "embeddings.db"
VECTOR_DIM = 8

EMBED_URL = "http://localhost:8000/embed"
MAX_RETRIES = 5
MAX_BACKOFF = 30
COOLDOWN = 60


def write_embedding_to_db(path: Path) -> None:
    """Persist embedding metadata for *path* in a SQLite database."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS embeddings (file TEXT UNIQUE)"
        )
        conn.execute("INSERT OR REPLACE INTO embeddings(file) VALUES (?)", (str(path),))


DEFAULT_LOG_DIR = Path("ops/handoffs/logs")
DEFAULT_DB_DIR = Path("ops/handoffs")
DB_FILE = "embeddings.db"
INDEX_FILE = "embeddings.faiss"


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


def _post_with_retry(data: dict, *, path: Path | None = None) -> dict:
    """POST *data* to the embed endpoint with retries.

    Returns a structured result: ``{"kind": "ok", "json": {...}}`` on success or
    ``{"kind": "error", "code": <code>}`` on failure.
    """

    import httpx  # imported lazily for easier testing

    event_id = uuid.uuid4().hex
    delay = 1.0
    timeout = httpx.Timeout(10.0, connect=10.0)
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = httpx.post(EMBED_URL, json=data, timeout=timeout)
            r.raise_for_status()
            return {"kind": "ok", "json": r.json()}
        except httpx.ConnectError:
            code = "connect"
        except httpx.HTTPStatusError as exc:
            code = exc.response.status_code
        else:  # pragma: no cover - defensive
            code = "unknown"
        log = {
            "event": "embed_error",
            "id": event_id,
            "path": str(path) if path else None,
            "retry": attempt,
            "code": code,
        }
        print(json.dumps(log))
        if attempt == MAX_RETRIES:
            print(json.dumps({"event": "circuit_breaker", "id": event_id}))
            time.sleep(COOLDOWN)
            break
        time.sleep(min(delay, MAX_BACKOFF))
        delay *= 2
    return {"kind": "error", "code": code}


def compute_embedding(text: str, dim: int = VECTOR_DIM) -> list[float]:
    """Return a deterministic embedding vector for *text*."""
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return [int.from_bytes(digest[i : i + 4], "little") / 2 ** 32 for i in range(0, dim * 4, 4)]


def process_file(
    path: Path,
    conn,
    index,
    index_path: Path,
) -> Optional[object]:
    """Embed new lines from *path* and store them."""
    existing = conn.execute(
        "SELECT MAX(line) FROM embeddings WHERE source = ?", (str(path),)
    ).fetchone()[0]
    processed = existing or 0
    with path.open("r", encoding="utf-8") as handle:
        for lineno, line in enumerate(handle, start=1):
            if lineno <= processed:
                continue
            text = line.strip()
            if not text:
                continue
            vector = compute_embedding(text)
            _post_with_retry({"text": text}, path=path)
            if index is None:
                index = db.load_index(index_path, VECTOR_DIM)
            db.add_embedding(conn, index, str(path), lineno, text, vector)
    return index


def main(
    log_dir: Path = DEFAULT_LOG_DIR,
    db_dir: Path = DEFAULT_DB_DIR,
) -> None:
    db_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / DB_FILE
    index_path = db_dir / INDEX_FILE
    conn = db.connect(db_path)
    index = None
    for log in log_dir.glob("*.log"):
        index = process_file(log, conn, index, index_path)
    db.save_index(index, index_path)


if __name__ == "__main__":
    main()

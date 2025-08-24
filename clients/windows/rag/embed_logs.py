"""Embed existing log files and persist vectors."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Optional

from . import db

DEFAULT_LOG_DIR = Path("ops/handoffs/logs")
DEFAULT_DB_DIR = Path("ops/handoffs")
DB_FILE = "embeddings.db"
INDEX_FILE = "embeddings.faiss"


def compute_embedding(text: str, dim: int = 8) -> list[float]:
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
            if index is None:
                index = db.load_index(index_path, len(vector))
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

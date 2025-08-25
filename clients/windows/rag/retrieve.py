"""Simple retrieval helpers for embedded log lines."""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from . import db
from .embed_logs import (
    DEFAULT_DB_DIR,
    DB_FILE,
    INDEX_FILE,
    compute_embedding,
)


def query(
    text: str,
    top_k: int = 5,
    db_dir: Path = DEFAULT_DB_DIR,
) -> List[Tuple[int, str, int, str, float]]:
    """Return the *top_k* most similar log entries to *text*.

    Each result is ``(id, source, line, text, distance)``.
    """

    db_path = Path(db_dir) / DB_FILE
    index_path = Path(db_dir) / INDEX_FILE
    vector = compute_embedding(text)
    conn = db.connect(db_path)
    index = db.load_index(index_path, len(vector))
    try:
        return db.search(conn, index, vector, top_k)
    finally:
        conn.close()


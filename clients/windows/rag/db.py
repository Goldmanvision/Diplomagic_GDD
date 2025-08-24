"""Simple SQLite/FAISS helpers for log embeddings."""

from __future__ import annotations

import array
import sqlite3
from pathlib import Path
from typing import Iterable, Iterator

try:  # pragma: no cover - optional dependency
    import faiss  # type: ignore
    import numpy as np  # type: ignore
except Exception:  # pragma: no cover - import guard
    faiss = None
    np = None

SCHEMA = (
    """CREATE TABLE IF NOT EXISTS embeddings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    line INTEGER,
    text TEXT,
    vector BLOB
);"""
)


def connect(db_path: Path) -> sqlite3.Connection:
    """Return a connection and ensure schema exists."""
    conn = sqlite3.connect(db_path)
    conn.execute(SCHEMA)
    return conn


def load_index(index_path: Path, dim: int):
    """Return a FAISS index if the library is available."""
    if faiss is None:
        return None
    if index_path.exists():
        return faiss.read_index(str(index_path))
    return faiss.IndexFlatL2(dim)


def save_index(index, index_path: Path) -> None:
    """Persist *index* to *index_path* if possible."""  # pragma: no cover - simple wrapper
    if faiss is None or index is None:
        return
    faiss.write_index(index, str(index_path))


def add_embedding(
    conn: sqlite3.Connection,
    index,
    source: str,
    line: int,
    text: str,
    vector: Iterable[float],
) -> int:
    """Insert *vector* for *text* into the database and index."""
    arr = array.array("f", list(vector))
    cur = conn.execute(
        "INSERT INTO embeddings (source, line, text, vector) VALUES (?, ?, ?, ?)",
        (source, line, text, arr.tobytes()),
    )
    rowid = cur.lastrowid
    if index is not None and np is not None:  # pragma: no cover - optional branch
        vec_np = np.asarray(list(vector), dtype="float32")
        ids = np.asarray([rowid], dtype="int64")
        index.add_with_ids(vec_np.reshape(1, -1), ids)
    conn.commit()
    return rowid


def fetch_all(conn: sqlite3.Connection) -> Iterator[tuple[int, str, int, str, bytes]]:
    """Yield all rows from the embeddings table."""
    cursor = conn.execute(
        "SELECT id, source, line, text, vector FROM embeddings ORDER BY id"
    )
    yield from cursor

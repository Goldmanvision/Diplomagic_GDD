"""Simple SQLite/FAISS helpers for log embeddings."""

from __future__ import annotations

import array
import sqlite3
from pathlib import Path
from typing import Iterable, Iterator, Sequence

try:  # pragma: no cover - optional dependency
    import faiss  # type: ignore
    import numpy as np  # type: ignore
except Exception:  # pragma: no cover - import guard
    faiss = None
    np = None

try:  # pragma: no cover - optional dependency
    import pgvector  # type: ignore
except Exception:  # pragma: no cover - import guard
    pgvector = None

SCHEMA = """CREATE TABLE IF NOT EXISTS embeddings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    line INTEGER,
    text TEXT,
    vector BLOB,
    vec VECTOR(8)
);"""


def connect(db_path: Path) -> sqlite3.Connection:
    """Return a connection and ensure schema exists."""
    conn = sqlite3.connect(db_path)
    if pgvector is not None:  # pragma: no cover - optional branch
        try:
            conn.enable_load_extension(True)
            pgvector.load(conn)  # type: ignore[attr-defined]
        except Exception:
            pass
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
    vec_list = list(vector)
    arr = array.array("f", vec_list)
    vec_val = pgvector.to_db(vec_list) if pgvector is not None else None
    cur = conn.execute(
        "INSERT INTO embeddings (source, line, text, vector, vec) VALUES (?, ?, ?, ?, ?)",
        (source, line, text, arr.tobytes(), vec_val),
    )
    rowid = cur.lastrowid
    if index is not None and np is not None:  # pragma: no cover - optional branch
        vec_np = np.asarray(vec_list, dtype="float32")
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


def search(
    conn: sqlite3.Connection,
    index,
    vector: Sequence[float],
    top_k: int,
) -> list[tuple[int, str, int, str, float]]:
    """Return the closest *top_k* rows for *vector*.

    Results are ordered by increasing squared L2 distance. If a FAISS ``index``
    is provided and the library is available, it is queried directly. Otherwise
    all rows are loaded via :func:`fetch_all` and distances computed in pure
    Python.
    """

    q_list = list(vector)
    results: list[tuple[int, str, int, str, float]] = []

    if index is not None and faiss is not None and np is not None:  # pragma: no cover
        q_np = np.asarray(q_list, dtype="float32").reshape(1, -1)
        distances, ids = index.search(q_np, top_k)
        for dist, idx in zip(distances[0], ids[0]):
            if idx == -1:
                continue
            row = conn.execute(
                "SELECT id, source, line, text FROM embeddings WHERE id = ?",
                (int(idx),),
            ).fetchone()
            if row:
                results.append((*row, float(dist)))
        return results

    # Fallback: compute distance in Python
    for row_id, source, line, text, blob in fetch_all(conn):
        vec = array.array("f")
        vec.frombytes(blob)
        dist = sum((a - b) ** 2 for a, b in zip(q_list, vec))
        results.append((row_id, source, line, text, float(dist)))
    results.sort(key=lambda x: x[4])
    return results[:top_k]


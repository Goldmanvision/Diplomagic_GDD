"""Simple retrieval of embedded log lines."""
from __future__ import annotations

from pathlib import Path
import sqlite3
import array
from typing import List, Tuple

from . import embed_logs


def _l2(a: List[float], b: array.array) -> float:
    """Return the squared L2 distance between two vectors."""
    return sum((x - y) * (x - y) for x, y in zip(a, b))


    db_path = Path(db_dir) / DB_FILE
    index_path = Path(db_dir) / INDEX_FILE
    vector = compute_embedding(text)
    conn = db.connect(db_path)
    index = db.load_index(index_path, len(vector))
    try:
        return db.search(conn, index, vector, top_k)
    finally:
        conn.close()


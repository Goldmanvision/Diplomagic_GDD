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


def query(text: str, db_dir: Path = embed_logs.DEFAULT_DB_DIR, top_k: int = 5) -> List[Tuple[str, float]]:
    """Return the *top_k* closest log lines to *text*.

    If the embeddings database does not exist an empty list is returned.
    """
    db_path = Path(db_dir) / embed_logs.DB_FILE
    if not db_path.exists():
        return []

    vec = embed_logs.compute_embedding(text)
    with sqlite3.connect(db_path) as conn:
        rows = conn.execute("SELECT text, vector FROM embeddings").fetchall()

    scored: List[Tuple[str, float]] = []
    for row_text, blob in rows:
        arr = array.array("f")
        arr.frombytes(blob)
        scored.append((row_text, _l2(vec, arr)))
    scored.sort(key=lambda r: r[1])
    return scored[:top_k]

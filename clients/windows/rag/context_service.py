"""Simple context lookup service for embedded logs."""

from __future__ import annotations

import array
import sqlite3
from pathlib import Path
from typing import List

from .embed_logs import DB_FILE, compute_embedding, DEFAULT_DB_DIR


def _vector_from_blob(blob: bytes) -> list[float]:
    arr = array.array("f")
    arr.frombytes(blob)
    return list(arr)


def query(text: str, db_dir: Path = DEFAULT_DB_DIR, top_k: int = 1) -> List[str]:
    """Return up to *top_k* snippets most similar to *text*."""
    db_path = Path(db_dir) / DB_FILE
    if not db_path.exists():
        return []
    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT text, vector FROM embeddings").fetchall()
    conn.close()
    if not rows:
        return []
    target = compute_embedding(text)
    scored = []
    for row_text, blob in rows:
        vec = _vector_from_blob(blob)
        dist = sum((a - b) ** 2 for a, b in zip(target, vec))
        scored.append((dist, row_text))
    scored.sort(key=lambda x: x[0])
    return [text for _, text in scored[:top_k]]

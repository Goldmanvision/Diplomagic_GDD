import sys
import array
import sqlite3
from pathlib import Path

# Ensure repository root on path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from clients.windows.rag import embed_logs, retrieve


def test_embeddings_written_and_retrievable(tmp_path):
    log_dir = tmp_path / "ops/handoffs/logs"
    db_dir = tmp_path / "ops/handoffs"
    log_dir.mkdir(parents=True)

    log_file = log_dir / "example.log"
    log_file.write_text("First line\nSecond line\n", encoding="utf-8")

    embed_logs.main(log_dir=log_dir, db_dir=db_dir)

    db_path = db_dir / embed_logs.DB_FILE
    assert db_path.exists()
    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT text, vector FROM embeddings ORDER BY id").fetchall()
    conn.close()
    assert [row[0] for row in rows] == ["First line", "Second line"]
    vec = array.array("f")
    vec.frombytes(rows[0][1])
    assert len(vec) == 8

    # Add a new line and ensure it appends rather than duplicates
    log_file.write_text("First line\nSecond line\nThird line\n", encoding="utf-8")
    embed_logs.main(log_dir=log_dir, db_dir=db_dir)

    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT text FROM embeddings ORDER BY id").fetchall()
    conn.close()
    assert [row[0] for row in rows] == ["First line", "Second line", "Third line"]

    results = retrieve.query("Third line", top_k=1, db_dir=db_dir)
    assert results[0][3] == "Third line"

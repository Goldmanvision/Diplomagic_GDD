from pathlib import Path
import sys

# Ensure repository root on path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from clients.windows.rag import embed_logs, context_service


def test_context_service_returns_relevant_snippet(tmp_path, monkeypatch):
    log_dir = tmp_path / "ops/handoffs/logs"
    db_dir = tmp_path / "ops/handoffs"
    log_dir.mkdir(parents=True)

    log_file = log_dir / "sample.log"
    log_file.write_text("alpha\nbeta\ngamma\n", encoding="utf-8")

    # Ensure external embedding command is stubbed
    monkeypatch.setattr(embed_logs.subprocess, "run", lambda *a, **k: None)

    embed_logs.main(log_dir=log_dir, db_dir=db_dir)

    results = context_service.query("beta", db_dir=db_dir, top_k=1)
    assert results == ["beta"]

import importlib
import sqlite3
import subprocess
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.append(str(ROOT))

import clients.windows.rag.embed_logs as embed_logs


def load_watch_logs(monkeypatch):
    """Import ``watch_logs`` with stubbed watchdog modules."""
    sys.modules.pop("clients.windows.rag.watch_logs", None)
    monkeypatch.setitem(sys.modules, "watchdog", types.ModuleType("watchdog"))
    events = types.ModuleType("watchdog.events")
    events.FileSystemEventHandler = object
    observers = types.ModuleType("watchdog.observers")
    observers.Observer = object
    monkeypatch.setitem(sys.modules, "watchdog.events", events)
    monkeypatch.setitem(sys.modules, "watchdog.observers", observers)
    return importlib.import_module("clients.windows.rag.watch_logs")


def test_embed_file_handles_file_not_found(monkeypatch, tmp_path, capsys):
    def fake_run(*args, **kwargs):
        raise FileNotFoundError("ollama not found")

    monkeypatch.setattr(embed_logs.subprocess, "run", fake_run)
    embed_logs.embed_file(tmp_path / "x.log")
    assert "Embedding failed" in capsys.readouterr().out


def test_embed_file_handles_called_process_error(monkeypatch, tmp_path, capsys):
    def fake_run(*args, **kwargs):
        raise subprocess.CalledProcessError(1, "cmd")

    monkeypatch.setattr(embed_logs.subprocess, "run", fake_run)
    embed_logs.embed_file(tmp_path / "x.log")
    assert "Embedding failed" in capsys.readouterr().out


def test_embed_file_handles_db_error(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(embed_logs.subprocess, "run", lambda *a, **k: None)

    def fake_db(path):
        raise sqlite3.DatabaseError("db locked")

    monkeypatch.setattr(embed_logs, "write_embedding_to_db", fake_db)
    embed_logs.embed_file(tmp_path / "x.log")
    assert "Failed to write embedding" in capsys.readouterr().out


def test_watch_logs_handles_file_not_found(monkeypatch):
    watch_logs = load_watch_logs(monkeypatch)

    monkeypatch.setattr(watch_logs, "process_file", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError()))
    monkeypatch.setattr(watch_logs.db, "save_index", lambda *a, **k: None)
    handler = watch_logs.LogHandler(None, None, Path("x"))
    event = types.SimpleNamespace(is_directory=False, src_path="missing.log")
    handler.on_modified(event)


def test_watch_logs_retries_on_db_error(monkeypatch):
    watch_logs = load_watch_logs(monkeypatch)

    calls = []
    def maybe_fail(*args, **kwargs):
        calls.append(args[0])
        if len(calls) == 1:
            raise sqlite3.DatabaseError("db locked")
    monkeypatch.setattr(watch_logs, "process_file", maybe_fail)
    monkeypatch.setattr(watch_logs.db, "save_index", lambda *a, **k: None)
    handler = watch_logs.LogHandler(None, None, Path("x"))

    event = types.SimpleNamespace(is_directory=False, src_path="x.log")
    handler.on_modified(event)
    assert len(calls) == 2


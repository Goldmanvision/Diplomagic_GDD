"""Watch handoff log files and update vector index."""

from __future__ import annotations

import json
import sqlite3
import time
import uuid
from pathlib import Path

try:  # pragma: no cover - optional dependency
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer
except ModuleNotFoundError:  # pragma: no cover - import guard
    Observer = None  # type: ignore[assignment]

    class FileSystemEventHandler:  # type: ignore
        pass

import db
from embed_logs import (
    DEFAULT_DB_DIR,
    DEFAULT_LOG_DIR,
    INDEX_FILE,
    DB_FILE,
    process_file,
)

MAX_RETRIES = 5
MAX_BACKOFF = 30
COOLDOWN = 60


def _request_with_retry(method: str, url: str, *, path: Path | None = None) -> dict:
    """Send an HTTP request with retries and return a structured result."""

    import httpx  # imported lazily for easier testing

    event_id = uuid.uuid4().hex
    delay = 1.0
    timeout = httpx.Timeout(10.0, connect=10.0)
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = httpx.request(method, url, timeout=timeout)
            r.raise_for_status()
            return {"kind": "ok"}
        except httpx.ConnectError:
            code = "connect"
        except httpx.HTTPStatusError as exc:
            code = exc.response.status_code
        except httpx.TimeoutException:
            code = "timeout"
        log = {
            "event": "request_error",
            "id": event_id,
            "path": str(path) if path else None,
            "retry": attempt,
            "code": code,
        }
        print(json.dumps(log))
        if attempt == MAX_RETRIES:
            print(json.dumps({"event": "circuit_breaker", "id": event_id}))
            time.sleep(COOLDOWN)
            break
        time.sleep(min(delay, MAX_BACKOFF))
        delay *= 2
    return {"kind": "error", "code": code}


def _wait_for_stable(path: Path, intervals: int = 3, delay: float = 1.0) -> bool:
    prev = -1
    stable = 0
    start = time.time()
    while time.time() - start < 60:
        size = path.stat().st_size if path.exists() else -1
        if size == prev:
            stable += 1
            if stable >= intervals:
                return True
        else:
            stable = 0
            prev = size
        time.sleep(delay)
    return False

class LogHandler(FileSystemEventHandler):
    """Append new log lines to the transcript and vector index."""

    def __init__(self, conn=None, index=None, index_path: Path | None = None):
        self.conn = conn
        self.index = index
        self.index_path = index_path or Path(INDEX_FILE)

    def on_modified(self, event):  # pragma: no cover - callback
        if not event.is_directory:
            path = Path(event.src_path)
            event_id = uuid.uuid4().hex
            print(json.dumps({"event": "modified", "id": event_id, "path": str(path)}))
            if not _wait_for_stable(path):
                return
            result = _request_with_retry(
                "get", "http://localhost:8000/health", path=path
            )
            if result.get("kind") == "error":
                return
            try:
                self.index = process_file(
                    path, self.conn, self.index, self.index_path
                )
                db.save_index(self.index, self.index_path)
            except FileNotFoundError as exc:
                print(
                    json.dumps(
                        {
                            "event": "file_missing",
                            "id": event_id,
                            "path": str(path),
                            "code": str(exc),
                        }
                    )
                )
            except sqlite3.DatabaseError as exc:
                log = {
                    "event": "db_error",
                    "id": event_id,
                    "path": str(path),
                    "code": str(exc),
                }
                print(json.dumps(log))
                try:
                    self.index = process_file(
                        path, self.conn, self.index, self.index_path
                    )
                    db.save_index(self.index, self.index_path)
                except Exception as retry_exc:
                    print(
                        json.dumps(
                            {
                                "event": "retry_failed",
                                "id": event_id,
                                "path": str(path),
                                "code": str(retry_exc),
                            }
                        )
                    )


def main(log_dir: str = str(DEFAULT_LOG_DIR), db_dir: str = str(DEFAULT_DB_DIR)) -> None:
    """Monitor *log_dir* for changes."""
    directory = Path(log_dir)
    if not directory.exists():
        print(f"Log directory {directory} does not exist")
        return

    db_path = Path(db_dir) / DB_FILE
    index_path = Path(db_dir) / INDEX_FILE
    conn = db.connect(db_path)
    index = db.load_index(index_path, 8)

    handler = LogHandler(conn, index, index_path)
    observer = Observer()
    observer.schedule(handler, str(directory), recursive=False)
    observer.start()
    print(f"Watching {directory} for updates...")

    try:  # pragma: no cover - long running loop
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()

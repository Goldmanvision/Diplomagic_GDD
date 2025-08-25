"""Watch handoff log files and update vector index."""

from __future__ import annotations

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ModuleNotFoundError as exc:  # pragma: no cover - import guard
    raise SystemExit(
        "watch_logs.py requires the 'watchdog' package. "
        "Install dependencies with 'pip install -r requirements.txt'."
    ) from exc

from pathlib import Path

import time
import sqlite3
import httpx

from . import db
from .embed_logs import (
    DEFAULT_DB_DIR,
    DEFAULT_LOG_DIR,
    INDEX_FILE,
    DB_FILE,
    process_file,
)

MAX_RETRIES = 5
MAX_BACKOFF = 30


def _request_with_retry(method: str, url: str) -> None:
    delay = 1.0
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = httpx.request(method, url, timeout=10)
            r.raise_for_status()
            return
        except (httpx.ConnectError, httpx.HTTPStatusError) as exc:
            print(f"request failed (attempt {attempt}): {exc}")
            if attempt == MAX_RETRIES:
                print("circuit breaker: sleeping 60s")
                time.sleep(60)
                break
            time.sleep(min(delay, MAX_BACKOFF))
            delay *= 2


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
            print(f"Detected change in {path}")
            if not _wait_for_stable(path):
                return
            _request_with_retry("get", "http://localhost:8000/health")
            try:
                self.index = process_file(
                    path, self.conn, self.index, self.index_path
                )
                db.save_index(self.index, self.index_path)
            except FileNotFoundError as exc:
                print(f"Log file not found {path}: {exc}")
            except sqlite3.DatabaseError as exc:
                print(
                    f"Database write failed for {path}: {exc}. Retrying once..."
                )
                try:
                    self.index = process_file(
                        path, self.conn, self.index, self.index_path
                    )
                    db.save_index(self.index, self.index_path)

                except Exception as retry_exc:
                    print(f"Retry failed for {path}: {retry_exc}")


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

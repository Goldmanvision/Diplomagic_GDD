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

from . import db
from .embed_logs import (
    DEFAULT_DB_DIR,
    DEFAULT_LOG_DIR,
    INDEX_FILE,
    DB_FILE,
    process_file,
)


class LogHandler(FileSystemEventHandler):
    """Append new log lines to the transcript and vector index."""

    def __init__(self, conn, index, index_path: Path):
        self.conn = conn
        self.index = index
        self.index_path = index_path

    def on_modified(self, event):  # pragma: no cover - callback
        if not event.is_directory:
            path = Path(event.src_path)
            print(f"Detected change in {path}")
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

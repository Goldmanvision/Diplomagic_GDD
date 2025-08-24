"""Watch handoff log files and update vector index.

Requires the optional watchdog package. If watchdog is not installed,
this script will exit with a helpful message.
"""

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ModuleNotFoundError as exc:  # pragma: no cover - import guard
    raise SystemExit(
        "watch_logs.py requires the 'watchdog' package. "
        "Install dependencies with 'pip install -r requirements.txt'."
    ) from exc

import time
from pathlib import Path
import subprocess
import sqlite3

from .embed_logs import embed_file

class LogHandler(FileSystemEventHandler):
    """Append new log lines to the transcript and vector index."""

    def on_modified(self, event):  # pragma: no cover - callback
        if not event.is_directory:
            path = Path(event.src_path)
            print(f"Detected change in {path}")
            try:
                embed_file(path)
            except FileNotFoundError as exc:
                print(f"Log file not found {path}: {exc}")
            except subprocess.CalledProcessError as exc:
                print(f"Embedding failed for {path}: {exc}")
            except sqlite3.DatabaseError as exc:
                print(f"Database write failed for {path}: {exc}. Retrying once...")
                try:
                    embed_file(path)
                except Exception as retry_exc:
                    print(f"Retry failed for {path}: {retry_exc}")


def main(log_dir: str = "ops/handoffs/logs") -> None:
    """Monitor *log_dir* for changes."""
    directory = Path(log_dir)
    if not directory.exists():
        print(f"Log directory {directory} does not exist")
        return

    handler = LogHandler()
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

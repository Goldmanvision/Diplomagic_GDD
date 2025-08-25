"""Command line interface for Windows RAG utilities."""
from __future__ import annotations

import argparse
from pathlib import Path

from . import embed_logs, retrieve


def _path(string: str) -> Path:
    return Path(string)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="RAG utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    p_embed = sub.add_parser("embed", help="Embed existing logs")
    p_embed.add_argument("--log-dir", type=_path, default=embed_logs.DEFAULT_LOG_DIR)
    p_embed.add_argument("--db-dir", type=_path, default=embed_logs.DEFAULT_DB_DIR)
    p_embed.set_defaults(func=lambda a: embed_logs.main(a.log_dir, a.db_dir))

    p_watch = sub.add_parser("watch", help="Watch log directory for changes")
    p_watch.add_argument("--log-dir", type=str, default=str(embed_logs.DEFAULT_LOG_DIR))
    p_watch.add_argument("--db-dir", type=str, default=str(embed_logs.DEFAULT_DB_DIR))

    def _run_watch(a):
        from . import watch_logs
        watch_logs.main(a.log_dir, a.db_dir)

    p_watch.set_defaults(func=_run_watch)

    p_query = sub.add_parser("query", help="Retrieve similar log lines")
    p_query.add_argument("text", help="Query text")
    p_query.add_argument("--db-dir", type=_path, default=embed_logs.DEFAULT_DB_DIR)
    p_query.add_argument("-k", "--top-k", type=int, default=5)

    def _run_query(a):
        results = retrieve.query(a.text, a.db_dir, a.top_k)
        for text, score in results:
            print(f"{score:.3f}\t{text}")

    p_query.set_defaults(func=_run_query)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()

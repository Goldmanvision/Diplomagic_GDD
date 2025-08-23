#!/usr/bin/env python3
import pathlib, re, sys
p = pathlib.Path("ops/locks/supervisor.lock")
if not p.exists(): print("LOCK: ABSENT"); sys.exit(0)
t = p.read_text(encoding="utf-8")
ok = all(k in t for k in ("holder:", "scope:", "start:", "ttl:", "note:"))
print("LOCK:", "PRESENT" if ok else "PRESENT but schema incomplete")

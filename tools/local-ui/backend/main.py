from __future__ import annotations

import io
import csv
import json
import re
from pathlib import Path
from datetime import datetime, timezone
from collections import deque
from typing import List, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from jsonschema import validate, ValidationError

# ------------------------------------------------------------------------------
# App + CORS
# ------------------------------------------------------------------------------
APP = FastAPI(title="DAPS Sidecar", version="0.3.2")
APP.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------------------
# Paths and minimal state
# ------------------------------------------------------------------------------
OUTBOX = Path(__file__).resolve().parent.parent / "_outbox/outbox.jsonl"
CFG_DIR = Path(__file__).resolve().parent
DEFAULT_MODE = "http"

_state = {"repoRoot": "."}  # for repo-scoped scanners (dashboards/mail/schemas)

def ensure_outbox():
    OUTBOX.parent.mkdir(parents=True, exist_ok=True)
    if not OUTBOX.exists():
        OUTBOX.write_text("", encoding="utf-8")

def write_outbox_line(obj: dict):
    OUTBOX.parent.mkdir(parents=True, exist_ok=True)
    with OUTBOX.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

# ------------------------------------------------------------------------------
# Models (Pydantic v2: use `pattern` not `regex`)
# ------------------------------------------------------------------------------
class PacketIn(BaseModel):
    agent: str = Field(..., min_length=1, max_length=80)
    kind: str = Field(..., pattern="^(prompt|action)$")
    action: Optional[str] = Field(None, pattern="^(yes|no|retry)$")
    text: Optional[str] = Field(None, max_length=20000)
    ref: Optional[str] = Field(None, max_length=120)

class PacketOut(BaseModel):
    id: str
    ts: str
    agent: str
    kind: str
    action: Optional[str] = None
    text: Optional[str] = None
    ref: Optional[str] = None
    source: str = "ui:prompt-hub"
    client: str = "local-ui"

# ------------------------------------------------------------------------------
# Health
# ------------------------------------------------------------------------------
@APP.get("/health")
def health():
    return {
        "ok": True,
        "ts": datetime.now(timezone.utc).isoformat(),
        "mode": DEFAULT_MODE,
    }


# ------------------------------------------------------------------------------
# Agents
# ------------------------------------------------------------------------------
@APP.get("/agents")
def agents():
    p = Path(__file__).parent / "agents.http.json"
    if not p.exists():
        raise HTTPException(404, "agents.http.json missing")
    return json.loads(p.read_text(encoding="utf-8"))

# ------------------------------------------------------------------------------
# Outbox queue (JSONL)
# ------------------------------------------------------------------------------
@APP.post("/outbox", response_model=PacketOut)
def enqueue(pkt: PacketIn, bg: BackgroundTasks):
    ensure_outbox()
    if pkt.kind == "prompt" and not (pkt.text or "").strip():
        raise HTTPException(400, "prompt requires text")
    if pkt.kind == "action" and not pkt.action:
        raise HTTPException(400, "action requires action field")

    rec = PacketOut(
        id=str(uuid4()),
        ts=datetime.now(timezone.utc).isoformat(),
        agent=pkt.agent,
        kind=pkt.kind,
        action=pkt.action,
        text=(pkt.text or None),
        ref=pkt.ref,
    )
    write_outbox_line(rec.model_dump())

    # Background forwarding can be added here later:
    # bg.add_task(forward_and_record_reply, rec)

    return rec

@APP.get("/outbox/tail", response_model=List[PacketOut])
def tail(limit: int = 200):
    ensure_outbox()
    if limit < 1 or limit > 1000:
        raise HTTPException(400, "limit 1..1000")
    dq: deque[str] = deque(maxlen=limit)
    with OUTBOX.open("r", encoding="utf-8") as f:
        for line in f:
            dq.append(line)
    out: List[PacketOut] = []
    for line in dq:
        try:
            out.append(PacketOut(**json.loads(line)))
        except Exception:
            continue
    return out

# ------------------------------------------------------------------------------
# Repo-scoped utilities and endpoints (dashboards, mail, schemas, export)
# ------------------------------------------------------------------------------
class Cfg(BaseModel):
    repoRoot: str

@APP.post("/config")
def set_cfg(cfg: Cfg):
    _state["repoRoot"] = cfg.repoRoot
    return {"ok": True, "repoRoot": _state["repoRoot"]}

def repo_path(p: str) -> Path:
    return Path(_state["repoRoot"]).joinpath(p)

def _scan_md():
    root = Path(_state["repoRoot"])
    for p in root.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
            yield p, text
        except Exception:
            continue

MAIL_RE = re.compile(r"(?ms)^From:\s*(?P<from>.+?)\nTo:\s*(?P<to>.+?)\nSubj:\s*(?P<subj>.+?)\n(?P<body>.*)")
QUIET_RE = re.compile(r"(?ms)^quiet-mail:\s*(?P<from>[^|]+)\|\s*(?P<to>[^|]+)\|\s*(?P<subj>[^|]+)\|\s*(?P<body>.+)$")

@APP.get("/dashboards")
def dashboards():
    items = []
    for p, txt in _scan_md():
        if "Dashboard" in p.name:
            title_m = re.search(r"^#\s*(.+)", txt, re.M)
            links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", txt)
            dept = "unknown"
            parts = p.parts
            if "departments" in parts:
                try:
                    dept = parts[parts.index("departments") + 1]
                except Exception:
                    pass
            items.append({
                "dept": dept,
                "title": title_m.group(1) if title_m else p.stem,
                "path": str(p),
                "links": [u for _, u in links],
                "meta": {},
            })
    return items

@APP.get("/mail")
def mail(dept: str = "", since: str = ""):
    out = []
    since_dt = None
    if since:
        try:
            since_dt = datetime.fromisoformat(since)
        except Exception:
            since_dt = None
    for p, txt in _scan_md():
        if dept and dept.lower() not in str(p).lower():
            continue
        # crude block splitting over code fences or blank lines
        for block in re.split(r"`(?:\w+)?\s*|\n{2,}", txt):
            m = MAIL_RE.search(block) or QUIET_RE.search(block)
            if not m:
                continue
            body = m.groupdict().get("body", "").strip()
            ts = None
            mdate = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", body)
            if mdate:
                ts = mdate.group(1)
            if ts and since_dt:
                try:
                    if datetime.fromisoformat(ts) < since_dt:
                        continue
                except Exception:
                    pass
            out.append({
                "from": m.group("from").strip(),
                "to": m.group("to").strip(),
                "subj": m.group("subj").strip(),
                "ts": ts or "",
                "body": body,
                "path": str(p),
            })
    return out

@APP.get("/schemas")
def schemas():
    d = repo_path("data/schemas")
    res = []
    if d.exists():
        for f in d.glob("*.json"):
            try:
                j = json.loads(f.read_text(encoding="utf-8"))
                res.append({"name": f.stem, "schema": j})
            except Exception:
                continue
    return res

class ExportReq(BaseModel):
    schema_id: str = Field(alias="schema")
    rows: list
    model_config = {"populate_by_name": True}

@APP.post("/export/csv")
def export_csv(req: ExportReq):
    # optional schema validation
    schema_file = repo_path(f"data/schemas/{req.schema_id}.json")
    if schema_file.exists():
        try:
            schema = json.loads(schema_file.read_text(encoding="utf-8"))
            for r in req.rows:
                validate(instance=r, schema=schema)
        except ValidationError as e:
            raise HTTPException(400, f"Schema validation failed: {e.message}")
        except json.JSONDecodeError as e:
            raise HTTPException(400, f"Invalid schema JSON: {e}")

    buf = io.StringIO()
    fieldnames = sorted({k for r in req.rows for k in r.keys()})
    w = csv.DictWriter(buf, fieldnames=fieldnames)
    w.writeheader()
    for r in req.rows:
        w.writerow(r)
    return buf.getvalue()

# ------------------------------------------------------------------------------
# Entrypoint
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    ensure_outbox()
    uvicorn.run(APP, host="127.0.0.1", port=5174)

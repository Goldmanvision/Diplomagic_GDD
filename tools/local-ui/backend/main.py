from __future__ import annotations
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pathlib import Path
from datetime import datetime, timezone
from collections import deque
from typing import List, Optional
from uuid import uuid4
import json

app = FastAPI(title="Local Sidecar Stub", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173", "*"],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

OUTBOX = Path("tools/local-ui/_outbox/outbox.jsonl")

def ensure_outbox():
    OUTBOX.parent.mkdir(parents=True, exist_ok=True)
    if not OUTBOX.exists():
        OUTBOX.write_text("", encoding="utf-8")

class PacketIn(BaseModel):
    agent: str = Field(..., min_length=1, max_length=80)
    kind: str = Field(..., regex="^(prompt|action)$")
    action: Optional[str] = Field(None, regex="^(yes|no|retry)$")
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
    source: str = "ui:prompt-hub-mvp"
    client: str = "local-ui"

@app.get("/health")
def health():
    return {"ok": True, "ts": datetime.now(timezone.utc).isoformat()}

@app.post("/outbox", response_model=PacketOut)
def outbox_write(pkt: PacketIn):
    ensure_outbox()
    if pkt.kind == "prompt" and not (pkt.text or "").strip():
        raise HTTPException(400, "prompt requires text")
    if pkt.kind == "action" and not pkt.action:
        raise HTTPException(400, "action requires action field")
    rec = PacketOut(
        id=str(uuid4()),
        ts=datetime.now(timezone.utc).isoformat(),
        agent=pkt.agent, kind=pkt.kind, action=pkt.action,
        text=(pkt.text or None), ref=pkt.ref,
    )
    with OUTBOX.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec.dict(), ensure_ascii=False) + "\n")
    return rec

@app.get("/outbox/tail", response_model=List[PacketOut])
def outbox_tail(limit: int = 200):
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5174)

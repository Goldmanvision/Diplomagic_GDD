from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from jsonschema import validate, ValidationError
from pathlib import Path
import re, json, csv, io, datetime

app=FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
_state={"repoRoot":"."}

class Cfg(BaseModel): repoRoot:str

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/config")
def set_cfg(cfg:Cfg):
    _state["repoRoot"]=cfg.repoRoot
    return {"ok":True}

def repo_path(p:str)->Path: return Path(_state["repoRoot"]).joinpath(p)

MAIL_RE=re.compile(r"(?ms)^From:\s*(?P<from>.+?)\nTo:\s*(?P<to>.+?)\nSubj:\s*(?P<subj>.+?)\n(?P<body>.*)")
QUIET_RE=re.compile(r"(?ms)^quiet-mail:\s*(?P<from>[^|]+)\|\s*(?P<to>[^|]+)\|\s*(?P<subj>[^|]+)\|\s*(?P<body>.+)$")

def _scan_md():
    root=Path(_state["repoRoot"])
    for p in root.rglob("*.md"):
        try:
            text=p.read_text(encoding="utf-8", errors="ignore")
            yield p, text
        except: pass

@app.get("/dashboards")
def dashboards():
    items=[]
    for p,txt in _scan_md():
        if "Dashboard" in p.name:
            import os
            title=re.search(r"^#\s*(.+)", txt, re.M)
            links=re.findall(r"\[([^\]]+)\]\(([^)]+)\)", txt)
            dept="unknown"
            parts=p.parts
            if "departments" in parts:
                try: dept=parts[parts.index("departments")+1]
                except: pass
            items.append({
                "dept": dept,
                "title": title.group(1) if title else p.stem,
                "path": str(p),
                "links":[u for _,u in links],
                "meta":{}
            })
    return items

@app.get("/mail")
def mail(dept:str="", since:str=""):
    out=[]
    since_dt=None
    if since:
        try: since_dt=datetime.datetime.fromisoformat(since)
        except: pass
    for p,txt in _scan_md():
        if dept and dept.lower() not in str(p).lower(): continue
        for block in re.split(r"`(?:\w+)?\s*|\n{2,}", txt):
            m=MAIL_RE.search(block) or QUIET_RE.search(block)
            if not m: continue
            body=m.groupdict().get("body","").strip()
            ts=None
            mdate=re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", body)
            if mdate: ts=mdate.group(1)
            if ts and since_dt:
                try:
                    if datetime.datetime.fromisoformat(ts) < since_dt: continue
                except: pass
            out.append({
                "from":m.group("from").strip(),
                "to":m.group("to").strip(),
                "subj":m.group("subj").strip(),
                "ts":ts or "",
                "body":body,
                "path":str(p)
            })
    return out

@app.get("/schemas")
def schemas():
    d=repo_path("data/schemas")
    res=[]
    if d.exists():
        for f in d.glob("*.json"):
            try:
                j=json.loads(f.read_text())
                res.append({"name":f.stem,"schema":j})
            except: pass
    return res

class ExportReq(BaseModel):
    schema_id: str = Field(alias="schema")
    rows:list

@app.post("/export/csv")
def export_csv(req:ExportReq):
    schema_file=repo_path(f"data/schemas/{req.schema_id}.json")
    if schema_file.exists():
        try:
            for r in req.rows: validate(instance=r, schema=json.loads(schema_file.read_text()))
        except ValidationError as e:
            return {"ok":False, "error":str(e)}
    buf=io.StringIO()
    fieldnames=sorted({k for r in req.rows for k in r.keys()})
    w=csv.DictWriter(buf, fieldnames=fieldnames)
    w.writeheader()
    for r in req.rows: w.writerow(r)
    return buf.getvalue()


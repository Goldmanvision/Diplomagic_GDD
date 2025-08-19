Set-StrictMode -Version Latest
\Continue = 'Stop'
Set-Location -LiteralPath \
. ..\tools\guard.ps1
Enter-RepoRoot
# --- original script below ---# wizard_local_ui.ps1 — DIPLOMAGIC Local UI scaffold
param([string]$AppDir="tools/local-ui")
$ErrorActionPreference="Stop"

# Guard
if(Test-Path $AppDir){ Write-Host "Exists: $AppDir"; exit 1 }

# Layout
New-Item -ItemType Directory -Force -Path $AppDir, "$AppDir/backend", "$AppDir/frontend" | Out-Null

# Backend
@"
fastapi
uvicorn[standard]
pydantic
python-multipart
jsonschema
pathspec
"@ | Set-Content "$AppDir/backend/requirements.txt" -Encoding ascii

@"
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
        for block in re.split(r"```(?:\w+)?\s*|\n{2,}", txt):
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
    schema:str
    rows:list

@app.post("/export/csv")
def export_csv(req:ExportReq):
    schema_file=repo_path(f"data/schemas/{req.schema}.json")
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
"@ | Set-Content "$AppDir/backend/main.py" -Encoding utf8

@"
@echo off
python -m venv .venv && call .venv\\Scripts\\activate && pip install -r backend\\requirements.txt && uvicorn backend.main:app --reload --port 5174
"@ | Set-Content "$AppDir/run_backend.bat" -Encoding ascii

# Frontend
Set-Content "$AppDir/frontend/package.json" @"
{
  "name": "local-ui",
  "private": true,
  "scripts": {"dev":"vite","build":"vite build","preview":"vite preview"},
  "dependencies": {},
  "devDependencies": {"vite":"^5.4.0"}
}
"@ -Encoding ascii

New-Item -ItemType Directory "$AppDir/frontend/public","$AppDir/frontend/src" | Out-Null
Set-Content "$AppDir/frontend/index.html" @"
<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>DIPLOMAGIC Local UI</title></head>
<body><div id="app"></div><script type="module" src="/src/main.js"></script></body></html>
"@ -Encoding utf8

Set-Content "$AppDir/frontend/src/main.js" @"
const api = (p,opt)=>fetch(`http://localhost:5174${p}`,{headers:{'Content-Type':'application/json'},...opt});
document.getElementById('app').innerHTML=`
  <section>
    <h1>DIPLOMAGIC Local UI</h1>
    <label>Repo root <input id="root" size="60" placeholder="../Diplomagic_GDD"></label>
    <button id="set">Set</button>
    <button id="dboards">Dashboards</button>
    <button id="mail">Mail</button>
    <pre id="out" style="white-space:pre-wrap;border:1px solid #ccc;padding:.5rem;margin-top:.5rem;height:60vh;overflow:auto"></pre>
  </section>`;
const out = document.getElementById('out');
document.getElementById('set').onclick=async ()=>{
  const root=document.getElementById('root').value||'.';
  const r=await api('/config',{method:'POST',body:JSON.stringify({repoRoot:root})}); out.textContent=JSON.stringify(await r.json(),null,2);
};
document.getElementById('dboards').onclick=async ()=>{
  const r=await api('/dashboards'); out.textContent=JSON.stringify(await r.json(),null,2);
};
document.getElementById('mail').onclick=async ()=>{
  const r=await api('/mail'); out.textContent=JSON.stringify(await r.json(),null,2);
};
"@ -Encoding utf8

# README
@"
DIPLOMAGIC Local UI Wizard
==========================

Usage
1) `.\wizard_local_ui.ps1`
2) Start backend: `.\tools\local-ui\run_backend.bat`
3) Frontend: `cd tools\local-ui\frontend && npm i && npm run dev -- --port 5173`
4) Open http://localhost:5173

Notes
- Set repo root in the UI.
- CSV export returns text; client should download.
- Place JSON schemas in `data/schemas`.
"@ | Set-Content "$AppDir/README.md" -Encoding utf8

Write-Host "Scaffold created at $AppDir"


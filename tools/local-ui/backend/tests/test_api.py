from fastapi.testclient import TestClient
from pathlib import Path
import json

from backend.main import app  # uses in-proc app
client = TestClient(app)

def test_health():
    r = client.get("/health"); assert r.status_code == 200; assert r.json()["status"]=="ok"

def test_schemas_and_export(tmp_path: Path, monkeypatch):
    # temp repo with schemas
    repo = tmp_path / "repo"; (repo/"data/schemas").mkdir(parents=True)
    (repo/"data/schemas/spawn_row.json").write_text(json.dumps({
        "type":"object","properties":{"Name":{"type":"string"}}, "required":["Name"]
    }), encoding="utf-8")

    # set repo root via API
    r = client.post("/config", json={"repoRoot": str(repo)})
    assert r.status_code == 200

    # list schemas
    r = client.get("/schemas"); assert r.status_code == 200
    assert any(s.get('name')=='spawn_row' for s in r.json())

    # export minimal CSV
    r = client.post("/export/csv", json={"schema":"spawn_row","rows":[{"Name":"X"}]})

    assert r.status_code == 200
    assert "Name" in r.text and "X" in r.text

from fastapi.testclient import TestClient
from pathlib import Path
import json

from backend.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_schemas_and_export(tmp_path: Path):
    repo = tmp_path / "repo"
    (repo / "data/schemas").mkdir(parents=True)
    (repo / "data/schemas/spawn_row.json").write_text(json.dumps({
        "type": "object",
        "properties": {"Name": {"type": "string"}},
        "required": ["Name"]
    }), encoding="utf-8")

    r = client.post("/config", json={"repoRoot": str(repo)})
    assert r.status_code == 200

    r = client.get("/schemas")
    assert r.status_code == 200
    data = r.json()
    ids = [d.get("name") for d in data] if data and isinstance(data[0], dict) else data
    assert "spawn_row" in ids

    r = client.post("/export/csv", json={"schema": "spawn_row", "rows": [{"Name": "X"}]})
    assert r.status_code == 200
    assert "Name" in r.text and "X" in r.text

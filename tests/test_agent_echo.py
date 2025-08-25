import sys
from pathlib import Path
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1] / "tools" / "local-ui"))
import backend.main as main  # noqa: E402

client = TestClient(main.APP)

def test_agent_echo(monkeypatch):
    captured = {}

    def fake_write(obj):
        captured['obj'] = obj

    monkeypatch.setattr(main, 'write_outbox_line', fake_write)
    payload = {"agent": "tester", "kind": "prompt", "text": "hi"}
    r = client.post("/outbox", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["agent"] == "tester"
    assert data["kind"] == "prompt"
    assert "id" in data and "ts" in data
    assert captured['obj']["agent"] == "tester"

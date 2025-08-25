import sys
from pathlib import Path
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1] / "tools" / "local-ui"))
from backend.main import APP  # noqa: E402

client = TestClient(APP)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["ok"] is True

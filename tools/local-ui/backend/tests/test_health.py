import os
import importlib
from fastapi.testclient import TestClient

def _load_app():
    # Try common names: app or APP in backend.main
    mod = importlib.import_module("backend.main")
    app = getattr(mod, "app", None) or getattr(mod, "APP", None)
    if app is None:
        raise RuntimeError("FastAPI app not found in backend.main")
    return app

def test_health_reports_http_mode():
    os.environ["DAPS_AGENT_MODE"] = "http"
    app = _load_app()
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data.get("ok") is True
    assert data.get("mode") == "http"
    assert "paths" in data or isinstance(data, dict)

import os
import uuid
import pytest
import httpx

# Skip in CI or if service not running
pytestmark = pytest.mark.skipif(
    os.getenv("CI") == "true", reason="local-only test; requires echo agent on :6001"
)

def test_echo_agent_ping():
    payload = {
        "agent": "Macro Manager",
        "kind": "prompt",
        "text": "ping",
        "ref": str(uuid.uuid4())
    }
    try:
        r = httpx.post("http://127.0.0.1:6001/agent", json=payload, timeout=5.0)
    except Exception as e:
        pytest.skip(f"echo agent unavailable: {e}")
    assert r.status_code == 200
    data = r.json()
    assert data.get("kind") == "reply"
    assert isinstance(data.get("text"), str) and data["text"].startswith("[echo]")

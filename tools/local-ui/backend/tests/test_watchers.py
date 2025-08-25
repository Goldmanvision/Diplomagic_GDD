import json
import sys
import types
import uuid
from pathlib import Path

import time

# Ensure local-ui modules are importable
sys.path.append(str(Path(__file__).resolve().parents[2]))

from watch_logs import _request_with_retry, _wait_for_stable, MAX_RETRIES  # noqa: E402
from embed_logs import _post_with_retry  # noqa: E402


def install_httpx_stub(monkeypatch, *, mode: str):
    """Install a minimal httpx stub into sys.modules."""
    class HTTPStatusError(Exception):
        def __init__(self, message="", response=None):
            super().__init__(message)
            self.response = response

    class ConnectError(Exception):
        pass

    class TimeoutException(Exception):
        pass

    class DummyResponse:
        def __init__(self, status_code=500, json_data=None):
            self.status_code = status_code
            self._json = json_data or {}

        def raise_for_status(self):
            if self.status_code >= 400:
                raise HTTPStatusError(response=self)

        def json(self):
            return self._json

    calls = {"count": 0}
    
    def fake_request(method, url, timeout=None):
        calls["count"] += 1
        if mode == "connect":
            raise ConnectError("boom")
        resp = DummyResponse(500)
        resp.raise_for_status()
        return resp

    def fake_post(url, json=None, timeout=None):
        calls["count"] += 1
        if mode == "connect":
            raise ConnectError("boom")
        resp = DummyResponse(500)
        resp.raise_for_status()
        return resp

    stub = types.SimpleNamespace(
        ConnectError=ConnectError,
        HTTPStatusError=HTTPStatusError,
        TimeoutException=TimeoutException,
        Timeout=lambda *a, **k: None,
        request=fake_request,
        post=fake_post,
    )
    monkeypatch.setitem(sys.modules, "httpx", stub)
    return calls


def test_request_with_retry_http_error(monkeypatch, capsys):
    calls = install_httpx_stub(monkeypatch, mode="status")
    monkeypatch.setattr(time, "sleep", lambda *_: None)
    monkeypatch.setattr(uuid, "uuid4", lambda: uuid.UUID(int=0))
    result = _request_with_retry("get", "http://example", path=Path("f"))
    assert result == {"kind": "error", "code": 500}
    assert calls["count"] == MAX_RETRIES
    log = json.loads(capsys.readouterr().out.splitlines()[0])
    assert log["path"] == "f"
    assert log["retry"] == 1


def test_post_with_retry_connect_error(monkeypatch, capsys):
    calls = install_httpx_stub(monkeypatch, mode="connect")
    monkeypatch.setattr(time, "sleep", lambda *_: None)
    monkeypatch.setattr(uuid, "uuid4", lambda: uuid.UUID(int=0))
    result = _post_with_retry({"text": "hi"}, path=Path("f"))
    assert result == {"kind": "error", "code": "connect"}
    assert calls["count"] == MAX_RETRIES
    log = json.loads(capsys.readouterr().out.splitlines()[0])
    assert log["retry"] == 1 and log["path"] == "f"


def test_wait_for_stable(monkeypatch):
    sizes = [10, 20, 20, 20, 20]

    class Stat:
        def __init__(self, size):
            self.st_size = size

    def fake_stat(self):
        return Stat(sizes.pop(0))

    monkeypatch.setattr(Path, "stat", fake_stat)
    monkeypatch.setattr(Path, "exists", lambda self: True)
    monkeypatch.setattr(time, "sleep", lambda *_: None)
    assert _wait_for_stable(Path("dummy"), intervals=3, delay=0.0)

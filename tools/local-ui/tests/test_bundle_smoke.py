import subprocess
import sys
import time
from pathlib import Path
import http.client

import pytest


@pytest.mark.skipif(sys.platform != "win32", reason="Windows bundle test requires Windows")
def test_bundle_smoke():
    exe = Path(__file__).resolve().parents[1] / "dist" / "bundle" / "daps.exe"
    if not exe.exists():
        pytest.skip("daps.exe not found")

    proc = subprocess.Popen([str(exe)], cwd=str(exe.parent))
    try:
        deadline = time.time() + 30
        while time.time() < deadline:
            conn = http.client.HTTPConnection("127.0.0.1", 5174, timeout=1)
            try:
                conn.request("GET", "/health")
                resp = conn.getresponse()
                body = resp.read()
                if resp.status == 200 and b"ok" in body:
                    return
            except OSError:
                pass
            finally:
                conn.close()
            time.sleep(0.5)
        pytest.fail("Health endpoint did not respond in time")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()

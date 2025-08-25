from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_src = Path(__file__).resolve().parents[2] / "local-ui" / "backend" / "main.py"
_spec = spec_from_file_location("tools_local_ui_backend_main_src", _src)
_mod = module_from_spec(_spec)
_spec.loader.exec_module(_mod)

APP = _mod.APP
app = APP

# re-export public names from the original module
for name in dir(_mod):
    if name in {"APP", "app"} or name.startswith("_"):
        continue
    globals()[name] = getattr(_mod, name)

__all__ = [name for name in globals() if not name.startswith("_")]

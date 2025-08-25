import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
import zipfile

ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"
DIST = ROOT.parent.parent / "dist" / "windows"


def build_backend() -> Path:
    """Compile backend into a standalone Windows executable using PyInstaller."""
    exe_dir = DIST / "backend"
    exe_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "pyinstaller",
            "--onefile",
            "--name",
            "daps",
            "--distpath",
            str(exe_dir),
            str(BACKEND / "main.py"),
        ],
        check=True,
    )
    return exe_dir / "daps.exe"


def assemble_bundle(exe: Path) -> Path:
    """Collect frontend assets, executable, and launch scripts into a bundle."""
    bundle_dir = DIST / "bundle"
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir(parents=True)

    shutil.copytree(FRONTEND, bundle_dir / "frontend")
    shutil.copy2(exe, bundle_dir / "daps.exe")
    for script in ["run_backend.bat", "run_backend.ps1"]:
        src = ROOT / script
        if src.exists():
            shutil.copy2(src, bundle_dir / script)
    return bundle_dir


def write_version() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    ts = datetime.utcnow().isoformat()
    (DIST / "VERSION.txt").write_text(f"{sha}\n{ts}\n", encoding="utf-8")


def zip_bundle(bundle_dir: Path) -> Path:
    zip_path = DIST / "daps_windows_bundle.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in bundle_dir.rglob("*"):
            zf.write(file, file.relative_to(bundle_dir))
    return zip_path


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--no-zip", action="store_true")
    parser.add_argument("--zip-only", action="store_true")
    args = parser.parse_args()

    if args.zip_only:
        zip_path = zip_bundle(DIST / "bundle")
        print(f"Created bundle at {zip_path}")
        return

    exe = build_backend()
    bundle_dir = assemble_bundle(exe)
    write_version()
    if not args.no_zip:
        zip_path = zip_bundle(bundle_dir)
        print(f"Created bundle at {zip_path}")
    else:
        print(f"Bundle prepared at {bundle_dir}")


if __name__ == "__main__":
    main()

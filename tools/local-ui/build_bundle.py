import os
import shutil
import subprocess
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"
DIST = ROOT / "dist"


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

    # copy frontend
    shutil.copytree(FRONTEND, bundle_dir / "frontend")

    # copy executable and helper scripts
    shutil.copy2(exe, bundle_dir / "daps.exe")
    for script in ["run_backend.bat", "run_backend.ps1"]:
        src = ROOT / script
        if src.exists():
            shutil.copy2(src, bundle_dir / script)

    # create zip archive
    zip_path = DIST / "daps_bundle.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in bundle_dir.rglob("*"):
            zf.write(file, file.relative_to(bundle_dir))
    return zip_path


def main() -> None:
    exe = build_backend()
    zip_path = assemble_bundle(exe)
    print(f"Created bundle at {zip_path}")


if __name__ == "__main__":
    main()

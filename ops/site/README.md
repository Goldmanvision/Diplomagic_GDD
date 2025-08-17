# ops/site — Local docs site

Purpose: quick local UI for the Project Workspace using MkDocs Material.

## Install
- Python 3.8+ and pip.
- `pip install mkdocs mkdocs-material`

## Use
```bash
# from repo root
cd ops/site
./build.sh serve   # or: ./build.sh build
# Windows PowerShell:
#   cd ops/site; ./build.ps1 serve
```

## Mirror list
Edit `mirror.lst` to add repo Markdown paths. Run `sync` to update `docs/`.

## Notes
- ASCII-safe paths only.
- This site is for local use. Do not publish without Suit approval.

_Last updated: 2025-08-17_

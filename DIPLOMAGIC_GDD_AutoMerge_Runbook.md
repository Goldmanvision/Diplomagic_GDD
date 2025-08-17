# DIPLOMAGIC GDD Auto‑Merge Runbook

**Purpose:** Automate application of `/Patches` and `/Trackers` into the section files (`SEC-*`), rebuild the combined GDD, and open a PR on each change.

**Status:** Implemented on `main`. Last updated 2025-08-16 08:18 UTC.

---

## Repo prerequisites
- GitHub → Settings → Actions → General → **Workflow permissions: Read and write**.
- Files live on `main` at:
  - `.github/workflows/merge-patches.yml`
  - `.github/scripts/merge_gdd.py`

---

## Workflow YAML (final)
Place at `.github/workflows/merge-patches.yml`.

```yaml
name: Merge patches and trackers
on:
  workflow_dispatch:
  push:
    branches: [ main ]
    paths:
      - 'Patches/**'
      - 'Trackers/**'

concurrency:
  group: auto-merge
  cancel-in-progress: true

permissions:
  contents: write
  pull-requests: write

jobs:
  merge:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Run merge
        run: |
          python --version
          ls -la .github/scripts || true
          python .github/scripts/merge_gdd.py
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v6
        with:
          branch: auto/merge-patches
          commit-message: "chore: auto-merge patches and trackers"
          title: "Auto-merge: Patches + Trackers → Updated GDD"
          body: "Automated merge from /Patches and /Trackers, plus root *_REPLACE*.md."
          delete-branch: true
```

---

## Merge script (final)
Place at `.github/scripts/merge_gdd.py`.

```python
#!/usr/bin/env python3
import re, os, shutil, datetime
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parents[2]  # repo root
PATCHES_DIR = ROOT / "Patches"
TRACKERS_DIR = ROOT / "Trackers"
COMBINED = ROOT / "DIPLOMAGIC_GDD_Combined.md"
REPORT = ROOT / "AUTO_MERGE_REPORT.md"
CHANGELOG = ROOT / "CHANGELOG_AUTO.md"
BACKUP_DIR = ROOT / ("Backups/AUTO-" + datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S") + "Z")
DRY_RUN = os.getenv("DRY_RUN", "0") == "1"

# ---------- Utilities ----------
def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def write_text(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    if not DRY_RUN:
        p.write_text(s, encoding="utf-8")

def list_section_files():
    # Section files look like SEC-03-*, SEC-12-*, etc.
    files = []
    for p in ROOT.glob("SEC-*"):
        if p.is_file() and p.suffix.lower() == ".md":
            m = re.search(r"SEC-(\d+)", p.name)
            if m:
                files.append((int(m.group(1)), p))
    files.sort(key=lambda tup: tup[0])
    return [p for _, p in files]

def parse_frontmatter(text: str):
    \"\"\"
    Parse simple YAML front matter. Example:
    ---
    target_file: SEC-03-NARRATIVE - Narrative.md
    target_heading: "3.2 Chapter List"
    mode: replace  # or append
    ---
    \"\"\"
    m = re.match(r"^---\\n(.*?)\\n---\\n", text, flags=re.DOTALL)
    if not m:
        return {}, text
    raw = m.group(1)
    body = text[m.end():]
    meta = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('\\"').strip("'")
    return meta, body

def parse_html_meta(text: str) -> dict:
    # <!-- target: FILE | heading: H | mode: replace|append -->
    m = re.search(r"<!--\\s*([^>]+)\\s*-->", text)
    if not m:
        return {}
    meta = {}
    for part in m.group(1).split("|"):
        if ":" in part:
            k, v = part.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta

def derive_meta_from_filename(path: Path) -> dict:
    name = path.name
    meta = {}
    sec = re.search(r"(SEC-\\d{2})", name)
    if sec:
        meta["target_section_prefix"] = sec.group(1)
    h = re.search(r"_(\\d+(?:\\.\\d+)*)_", name)
    if h:
        meta["target_heading"] = h.group(1)
    if "REPLACE" in name.upper():
        meta["mode"] = "replace"
    return meta

def find_target_file(meta: dict, section_files):
    tf = meta.get("target_file")
    if tf:
        for p in section_files:
            if p.name == tf:
                return p
    prefix = meta.get("target_section_prefix")
    if prefix:
        for p in section_files:
            if p.name.startswith(prefix):
                return p
    return None

def find_heading_block(md: str, heading_hint: str):
    \"\"\"Return (start_idx, end_idx, header_line, header_level) for the block that begins
    at a heading whose text startswith heading_hint (case-insensitive, ignoring numeric prefixes).
    If not found, return None.
    \"\"\"
    lines = md.splitlines(keepends=True)
    hdrs = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#(1, 6))\\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            title_norm = re.sub(r"^\\d+(?:\\.\\d+)*\\s*", "", title).lower()
            hdrs.append((i, level, title, title_norm))
    if not hdrs:
        return None
    hint_low = heading_hint.strip().lower()

    candidates = []
    if re.match(r"^\\d", hint_low):
        for idx, level, title, title_norm in hdrs:
            num = re.match(r"^(\\d+(?:\\.\\d+)*)", title)
            if num and num.group(1).startswith(hint_low):
                candidates.append((idx, level, title))
        if not candidates:
            for idx, level, title, title_norm in hdrs:
                if title_norm.startswith(hint_low):
                    candidates.append((idx, level, title))
    else:
        for idx, level, title, title_norm in hdrs:
            if title_norm.startswith(hint_low):
                candidates.append((idx, level, title))
    if not candidates:
        return None

    start_idx, level, header_title = candidates[0]
    end_idx = len(lines)
    for i2, lvl2, _, _ in hdrs:
        if i2 > start_idx and lvl2 <= level:
            end_idx = i2
            break
    start_char = sum(len(l) for l in lines[:start_idx])
    end_char = sum(len(l) for l in lines[:end_idx])
    header_line = lines[start_idx].rstrip("\\n")
    return (start_char, end_char, header_line, level)

def apply_replace_block(orig_md: str, block_span, new_body: str, keep_header=True):
    s, e, header_line, level = block_span
    header = header_line + "\\n" if keep_header else ""
    return orig_md[:s] + header + new_body.rstrip() + "\\n" + orig_md[e:]

def append_into_block(orig_md: str, block_span, new_body: str):
    s, e, header_line, level = block_span
    insertion = ("\\n" if not orig_md[e-1:e] == "\\n" else "") + new_body.rstrip() + "\\n"
    return orig_md[:e] + insertion + orig_md[e:]

def backup_file(p: Path):
    rel = p.relative_to(ROOT)
    dst = BACKUP_DIR / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not DRY_RUN:
        shutil.copy2(p, dst)

def rebuild_combined(section_files):
    chunks = []
    for p in section_files:
        chunks.append(read_text(p).rstrip() + "\\n\\n")
    return "# DIPLOMAGIC – Combined GDD (Auto-Rebuilt)\\n\\n" + "".join(chunks).rstrip() + "\\n"

def banner(s: str) -> str:
    bar = "=" * len(s)
    return f"{s}\\n{bar}\\n"

def sanitize_body(text: str) -> str:
    meta, body = parse_frontmatter(text)
    text2 = body
    text2 = re.sub(r"^<!--.*?-->\\s*\\n", "", text2, flags=re.DOTALL)
    return text2.strip() + "\\n"

# ---------- Main ----------
def main():
    report = []
    changes = []

    section_files = list_section_files()
    section_names = [p.name for p in section_files]

    # Safety backups
    for p in section_files + [COMBINED]:
        if p.exists(): 
            backup_file(p)

    tracker_items = []

    # 1) Collect patches from /Patches and root *_REPLACE*.md
    patch_files = []
    if PATCHES_DIR.exists():
        patch_files += sorted(PATCHES_DIR.rglob("*.md"))
    patch_files += sorted(ROOT.glob("SEC-*_*REPLACE*.md"))

    for pf in patch_files:
        raw = read_text(pf)
        fm, body0 = parse_frontmatter(raw)
        htmlm = parse_html_meta(raw)
        fnm = derive_meta_from_filename(pf)

        meta = {}
        for src in (fnm, htmlm, fm):
            meta.update(src)

        mode = meta.get("mode", "replace").lower()
        tgt = find_target_file(meta, section_files)
        if not tgt:
            report.append(f"[SKIP] {pf.name} → target not resolved. Candidates: {section_names}")
            continue

        tgt_md = read_text(tgt)
        body = sanitize_body(raw)

        heading_hint = meta.get("target_heading")
        block = find_heading_block(tgt_md, heading_hint) if heading_hint else None

        if block:
            if mode == "append":
                new_md = append_into_block(tgt_md, block, body)
                action = "APPEND"
            else:
                new_md = apply_replace_block(tgt_md, block, body, keep_header=True)
                action = "REPLACE"
            write_text(tgt, new_md)
            changes.append(f"{action}: {pf.name} → {tgt.name} @ '{heading_hint}'")
        else:
            if mode == "append":
                new_md = tgt_md.rstrip() + "\\n\\n" + body
                write_text(tgt, new_md)
                changes.append(f"APPEND-END: {pf.name} → {tgt.name}")
            else:
                if meta.get("target_heading"):
                    new_md = tgt_md.rstrip() + "\\n\\n" + body
                    write_text(tgt, new_md)
                    changes.append(f"FALLBACK-APPEND: {pf.name} → {tgt.name} (heading not found)")
                else:
                    if "REPLACE" in pf.name.upper():
                        write_text(tgt, body)
                        changes.append(f"FILE-REPLACE: {pf.name} → {tgt.name}")
                    else:
                        new_md = tgt_md.rstrip() + "\\n\\n" + body
                        write_text(tgt, new_md)
                        changes.append(f"SAFE-APPEND: {pf.name} → {tgt.name}")

    # 2) Aggregate trackers into changelog
    if TRACKERS_DIR.exists():
        for tf in sorted(TRACKERS_DIR.rglob("*.md")):
            text = read_text(tf)
            title = text.splitlines()[0].strip() if text else tf.name
            tracker_items.append(f"- {tf.name}: {title}")
        if tracker_items:
            write_text(CHANGELOG, "# Auto Changelog (Trackers)\\n\\n" + "\\n".join(tracker_items) + "\\n")

    # 3) Rebuild combined
    sects = list_section_files()
    combined = rebuild_combined(sects)
    write_text(COMBINED, combined)

    # 4) Report
    rep = []
    rep.append(banner("AUTO MERGE REPORT"))
    rep.append(f"UTC: {datetime.datetime.utcnow().isoformat()}Z\\n")
    rep.append("Applied changes:\\n")
    if changes:
        rep.append("\\n".join(f"- {c}" for c in changes) + "\\n")
    else:
        rep.append("- No patches applied\\n")
    if tracker_items:
        rep.append("\\nTracker items summarized in CHANGELOG_AUTO.md\\n")
    rep.append("\\nArtifacts:\\n- DIPLOMAGIC_GDD_Combined.md (rebuilt)\\n- CHANGELOG_AUTO.md\\n- Backups/*\\n")
    write_text(REPORT, "".join(rep))

if __name__ == "__main__":
    main()
```

---

## Usage
- Manual: Actions → **Merge patches and trackers** → **Run workflow**.
- Auto: Any push that changes `Patches/**` or `Trackers/**` triggers a run.

PR output includes:
- Updated `SEC-*` files as targeted by patches
- `DIPLOMAGIC_GDD_Combined.md` rebuilt
- `CHANGELOG_AUTO.md` updated from trackers
- `AUTO_MERGE_REPORT.md` detailing applied changes
- `Backups/AUTO-*` snapshot of ascii-safes

---

## Patch targeting
Use any of these in a patch file to direct placement:
```md
---
target_file: SEC-03-NARRATIVE - Narrative.md
target_heading: "3.2 Chapter List"
mode: replace   # or append
---
```
or an HTML comment
```md
<!-- target: SEC-03-NARRATIVE - Narrative.md | heading: 3.2 Chapter List | mode: replace -->
```
or encode in filename
```
SEC-03_3.2_Chapter_List_REPLACE.md
```

Rules:
- If `target_heading` resolves, `replace` swaps that section, `append` adds within it.
- If no heading found: safe append to end.
- Whole‑file replace only when filename contains `REPLACE` or explicitly targeted without a heading.

---

## Troubleshooting
- `python: not found` → ensure `actions/setup-python@v5` step.
- `No such file or directory: .github/scripts/merge_gdd.py` → path mismatch.
- `Resource not accessible by integration` on PR creation → enable **Read and write** permissions.
- If runs overlap, they queue. Concurrency block prevents conflicts.

---

## Smoke test (optional)
1. Add `Trackers/SMOKE-YYYYMMDD.md` with one line of text.
2. Commit to `main` and push.
3. Merge the auto PR. Confirm updated `CHANGELOG_AUTO.md` and `AUTO_MERGE_REPORT.md` on `main`.

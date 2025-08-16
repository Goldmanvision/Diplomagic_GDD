#!usrbinenv python3
import re, os, sys, shutil, json, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # repo root
PATCHES_DIR = ROOT  Patches
TRACKERS_DIR = ROOT  Trackers
COMBINED = ROOT  DIPLOMAGIC_GDD_Combined.md
REPORT = ROOT  AUTO_MERGE_REPORT.md
CHANGELOG = ROOT  CHANGELOG_AUTO.md
BACKUP_DIR = ROOT  (BackupsAUTO- + datetime.datetime.utcnow().strftime(%Y%m%d-%H%M%S) + Z)
DRY_RUN = os.getenv(DRY_RUN, 0) == 1

# ---------- Utilities ----------
def read_text(p Path) - str
    return p.read_text(encoding=utf-8, errors=replace)

def write_text(p Path, s str)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not DRY_RUN
        p.write_text(s, encoding=utf-8)

def list_section_files()
    files = sorted(ROOT.glob(SEC--.md), key=lambda p int(re.search(rSEC-(d+), p.name).group(1)))
    return files

def parse_frontmatter(text str) - (dict, str)
    # Minimal YAML front matter parser. Keys target_file, target_heading, mode
    m = re.match(r^---n(.)n---n, text, flags=re.DOTALL)
    if not m
        return {}, text
    raw = m.group(1)
    body = text[m.end()]
    meta = {}
    for line in raw.splitlines()
        line=line.strip()
        if not line or line.startswith(#) continue
        if  in line
            k, v = line.split(, 1)
            meta[k.strip()] = v.strip().strip('').strip(')
    return meta, body

def parse_html_meta(text str) - dict
    # !-- target FILE  heading H  mode replaceappend --
    m = re.search(r!--s([^]+)s--, text)
    if not m return {}
    meta = {}
    for part in m.group(1).split()
        if  in part
            k, v = part.split(, 1)
            meta[k.strip()] = v.strip()
    return meta

def derive_meta_from_filename(path Path) - dict
    # Examples
    # SEC-03_3.2_Chapter_List_REPLACE.md  → target SEC-03-, heading 3.2, mode replace
    # SEC-07_UI_Notes.md                  → target SEC-07-
    name = path.name
    meta = {}
    sec = re.search(r(SEC-d{2}), name)
    if sec
        meta[target_section_prefix] = sec.group(1)  # e.g., SEC-03
    h = re.search(r_(d+(.d+))_, name)
    if h
        meta[target_heading] = h.group(1)
    if REPLACE in name.upper()
        meta[mode] = replace
    return meta

def find_target_file(meta dict, section_files)
    # 1) explicit target_file
    tf = meta.get(target_file)
    if tf
        for p in section_files
            if p.name == tf
                return p
    # 2) by section prefix e.g., SEC-03
    prefix = meta.get(target_section_prefix)
    if prefix
        for p in section_files
            if p.name.startswith(prefix)
                return p
    return None

def find_heading_block(md str, heading_hint str)
    
    Return (start_idx, end_idx, header_line, header_level) for the block that begins
    at a heading whose text startswith heading_hint (case-insensitive, ignoring numeric prefixes).
    If not found, return None.
    
    lines = md.splitlines(keepends=True)
    # Build list of heading indices
    hdrs = []
    for i, line in enumerate(lines)
        m = re.match(r^(#{1,6})s+(.)$, line)
        if m
            level = len(m.group(1))
            title = m.group(2).strip()
            # strip leading numbering like 3.2  or 3 
            title_norm = re.sub(r^d+(.d+)s, , title).lower()
            hdrs.append((i, level, title, title_norm))
    if not hdrs
        return None
    hint_low = heading_hint.strip().lower()

    # First pass match by numeric prefix 3.2
    candidates = []
    if re.match(r^d, hint_low)
        for idx, level, title, title_norm in hdrs
            num = re.match(r^(d+(.d+)), title)
            if num and num.group(1).startswith(hint_low)
                candidates.append((idx, level, title))
        if not candidates
            # fallback to prefix in title text
            for idx, level, title, title_norm in hdrs
                if title_norm.startswith(hint_low)
                    candidates.append((idx, level, title))
    else
        for idx, level, title, title_norm in hdrs
            if title_norm.startswith(hint_low)
                candidates.append((idx, level, title))

    if not candidates
        return None

    # Choose first candidate
    start_idx, level, header_title = candidates[0]
    # find end next heading with level = current
    end_idx = len(lines)
    for i2, lvl2, _, _ in hdrs
        if i2  start_idx and lvl2 = level
            end_idx = i2
            break
    start_char = sum(len(l) for l in lines[start_idx])
    end_char = sum(len(l) for l in lines[end_idx])
    header_line = lines[start_idx].rstrip(n)
    return (start_char, end_char, header_line, level)

def apply_replace_block(orig_md str, block_span, new_body str, keep_header=True)
    s, e, header_line, level = block_span
    header = header_line + n if keep_header else 
    return orig_md[s] + header + new_body.rstrip() + n + orig_md[e]

def append_into_block(orig_md str, block_span, new_body str)
    s, e, header_line, level = block_span
    # append before end of block, ensure spacing
    insertion = (n if not orig_md[e-1e] == n else ) + new_body.rstrip() + n
    return orig_md[e] + insertion + orig_md[e]

def backup_file(p Path)
    rel = p.relative_to(ROOT)
    dst = BACKUP_DIR  rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not DRY_RUN
        shutil.copy2(p, dst)

def rebuild_combined(section_files)
    chunks = []
    for p in section_files
        chunks.append(read_text(p).rstrip() + nn)
    return # DIPLOMAGIC – Combined GDD (Auto-Rebuilt)nn + .join(chunks).rstrip() + n

def banner(s str) - str
    bar = =  len(s)
    return f{s}n{bar}n

def sanitize_body(text str) - str
    # Remove front matter and any leading comment meta
    meta, body = parse_frontmatter(text)
    text2 = body
    # strip first HTML comment block if it seems like meta
    text2 = re.sub(r^!--.--sn, , text2, flags=re.DOTALL)
    return text2.strip() + n

# ---------- Main ----------
def main()
    report = []
    changes = []

    if not PATCHES_DIR.exists() and not TRACKERS_DIR.exists()
        print(No PatchesTrackers directories found. Exiting.)
        return

    section_files = list_section_files()
    section_names = [p.name for p in section_files]

    # Safety backups
    for p in section_files + [COMBINED]
        if p.exists() backup_file(p)

    # Load tracker items to emit into CHANGELOG_AUTO.md
    tracker_items = []

    # 1) Apply patches
    if PATCHES_DIR.exists()
        for pf in sorted(PATCHES_DIR.rglob(.md))
            raw = read_text(pf)
            fm, body0 = parse_frontmatter(raw)
            htmlm = parse_html_meta(raw)
            fnm = derive_meta_from_filename(pf)

            # Merge meta precedence frontmatter  html  filename
            meta = {}
            for src in (fnm, htmlm, fm)
                meta.update(src)

            mode = meta.get(mode, replace).lower()  # default replace
            tgt = find_target_file(meta, section_files)
            if not tgt
                report.append(f[SKIP] {pf.name} → target not resolved. Candidates {section_names})
                continue

            tgt_md = read_text(tgt)
            body = sanitize_body(raw)

            heading_hint = meta.get(target_heading)
            if heading_hint
                block = find_heading_block(tgt_md, heading_hint)
            else
                block = None

            if block
                if mode == append
                    new_md = append_into_block(tgt_md, block, body)
                    action = APPEND
                else
                    new_md = apply_replace_block(tgt_md, block, body, keep_header=True)
                    action = REPLACE
                write_text(tgt, new_md)
                changes.append(f{action} {pf.name} → {tgt.name} @ '{heading_hint}')
            else
                # No heading; choose whole-file behavior
                if mode == append
                    new_md = tgt_md.rstrip() + nn + body
                    write_text(tgt, new_md)
                    changes.append(fAPPEND-END {pf.name} → {tgt.name})
                else
                    # Whole-file replace only if explicitly flagged
                    if meta.get(target_heading)
                        # Heading intended but not found. Fallback to APPEND-END to avoid destructive ops.
                        new_md = tgt_md.rstrip() + nn + body
                        write_text(tgt, new_md)
                        changes.append(fFALLBACK-APPEND {pf.name} → {tgt.name} (heading not found))
                    else
                        # If file name includes '_REPLACE', allow full replace
                        if REPLACE in pf.name.upper()
                            write_text(tgt, body)
                            changes.append(fFILE-REPLACE {pf.name} → {tgt.name})
                        else
                            new_md = tgt_md.rstrip() + nn + body
                            write_text(tgt, new_md)
                            changes.append(fSAFE-APPEND {pf.name} → {tgt.name})

    # 2) Aggregate trackers into changelog
    if TRACKERS_DIR.exists()
        for tf in sorted(TRACKERS_DIR.rglob(.md))
            text = read_text(tf)
            title = text.splitlines()[0].strip() if text else tf.name
            tracker_items.append(f- {tf.name} {title})
        if tracker_items
            write_text(CHANGELOG, # Auto Changelog (Trackers)nn + n.join(tracker_items) + n)

    # 3) Rebuild combined
    sects = list_section_files()
    combined = rebuild_combined(sects)
    write_text(COMBINED, combined)

    # 4) Report
    rep = []
    rep.append(banner(AUTO MERGE REPORT))
    rep.append(fUTC {datetime.datetime.utcnow().isoformat()}Zn)
    rep.append(Applied changesn)
    if changes
        rep.append(n.join(f- {c} for c in changes) + n)
    else
        rep.append(- No patches appliedn)
    if tracker_items
        rep.append(nTracker items summarized in CHANGELOG_AUTO.mdn)
    rep.append(nArtifactsn- DIPLOMAGIC_GDD_Combined.md (rebuilt)n- CHANGELOG_AUTO.mdn- Backupsn)
    write_text(REPORT, .join(rep))

if __name__ == __main__
    main()

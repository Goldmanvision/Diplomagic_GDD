#!/usr/bin/env python3
\"\"\"validation_postfilter.py

Usage:
  python3 .github/scripts/validation_postfilter.py <input_report> <output_report> [--window N]

Reads input_report line by line. Writes only lines that contain a configured keyword
and are not negated within a window of N tokens before the keyword (default N=5).
\"\"\"
import sys
import re
from pathlib import Path

NEG_TOKENS = re.compile(r\"\\b(no|none|without|don't|do not|remove|removed|absent|not|never|exclude|excluded)\\b\", re.I)
KEYWORDS = re.compile(r\"\\b(Evidence|BlueOnBlue|CH6|Blue-on-Blue|CCTV|K-9|K9|K-9|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|raid)\\b\", re.I)

def neg_within_n_tokens(line, keyword_span_start, n=5):
    prefix = line[:keyword_span_start]
    tokens = re.findall(r\"\\w+|[-']\", prefix)
    window = ' '.join(tokens[-n:]) if tokens else ''
    return bool(NEG_TOKENS.search(window))

def process(inpath, outpath, window=5):
    inpath = Path(inpath)
    outpath = Path(outpath)
    if not inpath.exists():
        print(f\"Input report not found: {inpath}\", file=sys.stderr)
        return 2
    outpath.parent.mkdir(parents=True, exist_ok=True)
    kept = 0
    total = 0
    with inpath.open('r', encoding='utf-8', errors='ignore') as inf, outpath.open('w', encoding='utf-8') as outf:
        for line in inf:
            total += 1
            m = KEYWORDS.search(line)
            if not m:
                continue
            if neg_within_n_tokens(line, m.start(), n=window):
                continue
            outf.write(line)
            kept += 1
    print(f\"Processed {total} lines. Kept {kept} matching lines (window={window}).\")
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(\"Usage: validation_postfilter.py <input> <output> [--window N]\", file=sys.stderr)
        sys.exit(2)
    inrep = sys.argv[1]
    outre = sys.argv[2]
    window = 5
    if len(sys.argv) >= 4:
        try:
            window = int(sys.argv[3])
        except:
            pass
    rc = process(inrep, outre, window=window)
    sys.exit(rc)

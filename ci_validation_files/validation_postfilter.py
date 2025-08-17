#!/usr/bin/env python3
"""validation_postfilter.py

Usage:
  python3 validation_postfilter.py <input_report> <output_report> [window]

Reads input_report line by line. Writes only lines that contain configured keywords
and are not negated within a window of N tokens before or after the keyword (default N=5).
"""
import sys, re
from pathlib import Path

NEG_TOKENS = re.compile(r"\b(no|none|without|don't|do not|remove|removed|absent|not|never|exclude|excluded)\b", re.I)
KEYWORDS = re.compile(r"\b(Evidence|BlueOnBlue|CH6|Blue-on-Blue|CCTV|K-9|K9|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|raid)\b", re.I)


def neg_within_n_tokens(line, keyword_span_start, n=5):
    """Return True if a negation token appears within n tokens before OR after the keyword."""
    prefix = line[:keyword_span_start]
    suffix = line[keyword_span_start:]
    tokens_pre = re.findall(r"\w+|[-']", prefix)
    tokens_post = re.findall(r"\w+|[-']", suffix)
    window_pre = ' '.join(tokens_pre[-n:]) if tokens_pre else ''
    window_post = ' '.join(tokens_post[:n]) if tokens_post else ''
    return bool(NEG_TOKENS.search(window_pre) or NEG_TOKENS.search(window_post))


def process(inpath, outpath, window=5):
    inpath = Path(inpath)
    outpath = Path(outpath)
    if not inpath.exists():
        print(f"Input report not found: {inpath}", file=sys.stderr)
        return 2
    outpath.parent.mkdir(parents=True, exist_ok=True)
    kept = total = 0
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
    print(f"Processed {total} lines. Kept {kept} matching lines (window={window}).")
    return 0


def main(argv):
    if len(argv) < 3:
        print("Usage: validation_postfilter.py <input> <output> [window]", file=sys.stderr)
        return 2
    inrep, outre = argv[1], argv[2]
    window = int(argv[3]) if len(argv) >= 4 else 5
    return process(inrep, outre, window=window)


if __name__ == '__main__':
    sys.exit(main(sys.argv))

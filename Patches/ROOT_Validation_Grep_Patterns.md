# Root Validation — Grep/Ripgrep Patterns (CH5–CH6)
Repo dir: /Patches

Safe op. Text-only checks to verify constraints after merge.

## 1994 audit
- Find disallowed tech:
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SIM|digital camera" -S
```
- Ensure MicroTAC present when phones are referenced:
```
rg -n "MicroTAC"
```

## ROE and phrasing
- Remove legacy non-lethal language:
```
rg -n "non-\s*lethal preferred|IA penalties" -S
```
- Ambient phrase only:
```
rg -n "the stars are right tonight"
```

## Blue-on-Blue
- Confirm rule present:
```
rg -n "Blue[- ]on[- ]Blue|friendly[- ]fire.*fail" -S
```

## Evidence cap
```
rg -n "Evidence(Count| cap).*(3|three)"
```

## Prompt length scan (quick heuristic)
Prompts must be ≤14 chars. List suspect tokens >14:
```
rg -No "\b[A-Za-z][A-Za-z ]{14,}\b" SEC-07-* | sort -u
```
Then manually verify in `/Patches/SEC-07-CH6_Prompts_Verification.md`.

## Merge residue
```
rg -n "CH5|CH6" "SEC-03-NARRATIVE - Narrative.md" -n
rg -n "TODO|TBD|<<<|>>>" -S
```

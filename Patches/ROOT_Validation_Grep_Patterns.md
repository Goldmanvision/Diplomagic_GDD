# ROOT — Validation Grep/RG Patterns (CH5–CH6)
Repo dir: /Patches

Use **one** tool family (rg or grep). Run at repo root.

## 1) Disallowed tech (should return NO matches)
### ripgrep
```
rg -n -S "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera"
```
### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

## 2) Required ROE line
```
rg -n "CH6 is a .*raid.*Blue-?on-?Blue.*hard fail" -S SEC-03-*
```

## 3) Evidence cap mention
```
rg -n -S "evidence.*cap.*3|cap\s*3" SEC-05-* SEC-07-*
```

## 4) Prompts >14 chars (heuristic)
```
rg -n "^[^`]*\b[A-Za-z][A-Za-z ]{15,}\b" SEC-07-*
```

## 5) Ambient phrase usage (should be present, not in prompts)
```
rg -n -S "the stars are right tonight"
```

## 6) Node names consistency (should match set)
```
rg -n -S "Bulkhead Gate|Man-?Door|Service Passage|Valve Row|Dead Piping|Service Stair|Core Gallery|Splinter Vault" SEC-03-* SEC-06-*
```

## 7) Exceptions present (Shield/pellet)
```
rg -n -S "Shield.*absor[bp]|>\s*10\s*m.*pellet" SEC-05-*
```

If any command returns unexpected results, log in `/Trackers/PR_Crosscheck_Results_Log.md`.

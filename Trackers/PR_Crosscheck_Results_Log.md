# Tracker — PR Crosscheck Results Log (CH5–CH6)
Repo dir: /Trackers
Date: 2025-08-15

| Check | Command | Result (OK/Issue) | Notes / File refs |
|---|---|---|---|
| Disallowed tech | rg -n -S "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" |  |  |
| ROE line present | rg -n "CH6 is a .*raid.*Blue-?on-?Blue.*hard fail" -S SEC-03-* |  |  |
| Evidence cap | rg -n -S "evidence.*cap.*3|cap\s*3" SEC-05-* SEC-07-* |  |  |
| Prompts >14 | rg -n "^[^`]*\b[A-Za-z][A-Za-z ]{15,}\b" SEC-07-* |  |  |
| Ambient phrase | rg -n -S "the stars are right tonight" |  |  |
| Node names | rg -n -S "Bulkhead Gate|Man-?Door|Service Passage|Valve Row|Dead Piping|Service Stair|Core Gallery|Splinter Vault" SEC-03-* SEC-06-* |  |  |
| Exceptions | rg -n -S "Shield.*absor[bp]|>\s*10\s*m.*pellet" SEC-05-* |  |  |

Outcome:
- [ ] PASS
- [ ] FAIL → file issues and block merge

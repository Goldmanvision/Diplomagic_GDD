# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

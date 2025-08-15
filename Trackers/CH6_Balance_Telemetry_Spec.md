# Tracker — CH6 Balance Telemetry Spec
Repo dir: /Trackers

## Objective
Capture minimal, privacy‑safe playtest metrics to tune difficulty and pacing. Dev‑only; no in‑universe UI.

## Session KPIs
- Time to Vault (min)  
- Ending chosen (Contain / Sever / Black File)  
- EvidenceCount (0–3)  
- BlueOnBlue occurred (Y/N)  
- Deaths (count) and cause (Zombie / Cultist / Gaunt / Beast)  
- Ammo spent by type (Pistol / Shotgun / Rifle)  
- Tonics used (count)  
- Mana spent (total)  
- Fear peak (max state reached)  
- Waves cleared in Vault (count)  
- Damage taken (total)

## Segment timings (mm:ss)
- Bulkhead→Service Passage  
- Valve Row dwell  
- Dead Piping dwell  
- Service Stair ascent  
- Core Gallery dwell  
- Vault objective time

## Notes
- Store locally during tests; export CSV out‑of‑band.  
- Do not exceed CH6 evidence cap via telemetry.

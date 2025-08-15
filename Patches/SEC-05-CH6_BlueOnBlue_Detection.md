# SEC-05 — CH6 Blue‑on‑Blue Detection
Repo dir: /Patches

## Scope
Raid ROE: lethal vs hostiles is score‑neutral. Any friendly hit = fail.

## Friendly roster
Avery, Clara, Reddy, Deputy {DeputyName}. All others = hostile.

## Detection
- **Event:** DamageApplied(actor=Avery|Clara|Reddy, target in FriendlyRoster).  
- **Confirm:** Ignore if absorbed by **Shield** (damage==0). Else set `BlueOnBlue=1` and hard‑fail chapter.  
- **Pellet spread exception:** If shotgun pellet hits friendly at **>10 m**, ignore one pellet hit per trigger (mitigate false positives).

## Telemetry
Log attacker, target, weapon, timecode. No images.

## UI
Flash **BlueOnBlue** indicator, then fail screen.

## Tests
- Sidearm graze on Clara → fail.  
- Frag splash on Deputy → fail.  
- Shielded hit → no fail.  
- >10 m pellet single pellet → no fail; multiple pellets → fail.

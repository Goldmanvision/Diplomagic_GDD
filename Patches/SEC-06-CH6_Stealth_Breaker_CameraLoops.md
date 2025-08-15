# SEC-06 — CH6 Stealth: Breakers & Camera Loops
Repo dir: /Patches

## Analog cameras (1994)
- Fixed arcs in **Service Passage** only. Tape‑deck recording; no network.  
- **Blind spots:** at arc seams and breaker outages.

## Breaker boxes
- **Fuse pull** creates a **90 s** camera outage in connected zone.  
- **Cooldown:** 60 s before fuse reinsert allowed.  
- **K‑9 reroute:** patrol shifts to lantern sweep during outage.  
- **Risk:** pulling during Alert High spawns +1 Cultist on response.

## Loop design
- Player can chain two boxes to walk Valve Row unseen.  
- Breakers do **not** affect Vault cameras (none installed).

## UI prompts (≤14 chars)
Fuse, Pull Fuse, Insert Fuse, Breach, Hide, Crouch, Map, Note

## QA
- Verify 90 s outage timing.  
- Verify K‑9 route swap.  
- Verify no Vault cameras.

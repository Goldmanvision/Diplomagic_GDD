# SEC-05 — CH5→CH6 Systems: Rover, Fuel, O2
Repo dir: /Patches

## D‑LAMP Utility Rover
- **Controls (≤14 chars):** Drive, Brake, Lights, Horn, Enter, Exit.  
- **Handling:** Low‑speed torque; skids on gravel; handbrake turns limited.  
- **Damage:** Cave‑ins and collisions reduce `RoverHP`. At 0 → forced on‑foot detour.  
- **Fuel:** `FuelMax`, `Fuel`. Consumption scales with throttle; refuel only at Rover Bay. HUD meter on while driving.

## Headlights & Reveal
- Headlights reveal shimmered entities (Star Vampire Phase 1).  
- Lights off improves stealth vs cultists but worsens night‑gaunt ambush chance.

## Oxygen Hazard (Deep Site only)
- **Cue:** “O2 LOW” tone; no numeric display.  
- **Rule:** Sprinting drains O2 faster; idle near fans restores slowly.  
- **Fail:** Severe O2 drop blurs vision and slows actions; death only on extreme neglect.

## Fail/Retry
- Fuel empty or RoverHP=0 triggers on‑foot bypass; later reacquire rover if backtracked to bay.

## Flags/Vars
RoverHP, FuelMax, Fuel, O2LowCue, F_DLampRover, F_RouteKey

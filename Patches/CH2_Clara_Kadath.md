# Patch: CH2 — Clara “Kadath Survival”
Version: v0.2 • 2025-08-15
Owner: Nick Goldman

## Summary
Refocus CH2 on Kadath survival with supply-run infiltrations into Brightstar. Add portal topology, Safe Nests for Reddy, parent-call objective with Call Intercept meter, and a mandatory multipurpose-room fight. 1994 tech locked.

## World
- Two-way portal “Pine Break” behind Brightstar. Forest = Kadath. Building = warped Brightstar.
- All exterior exits loop. Re-entering portal returns to forest only.
- Anchor rooms persist: Service Corridor, Office, Multipurpose Room. Others scramble until Master Keys.

## Systems
- Survival meters: Hunger, Thirst, Warmth, Fatigue (decay only in forest).
- Safe Nests: Bivouac, Bus Cubby, Nurse Locker. Reddy carry = +noise, −stealth.
- Parent calls: office landline; Answered/Message/Busy; longer calls raise alert.
- Call Intercept meter (0–100): Low 45–60s, Med 30–45s, High 15–30s; spikes from cry/footsteps/redial; hang up to avoid intercept.
- Phrase: record “the stars are right tonight.” Playback opens one warded cabinet; Clara never speaks it.

## Set Piece
- “Brightstar Brawl” in multipurpose room. Non-lethal focus. Loot: Master Keys, Admin map, Medkit.

## Scoring (additive)
+5 parent Confirmed, +2 Message, +1 evidence page  
+3 WaterSafe, +3 FoodSecured, +2 FirstAid  
+5 per non-lethal disable (max +15), +5 Lights-Out clear  
+1 SafeCall (meter ≤70)  
−5 lethal finish, −5 firearm discharged (Deacon), −3 alert escalated

## UI prompts (≤14 chars)
Hush, Hide, Crouch, Throw, Listen, Use, Inspect, Pick Up, Forage, Gather, Boil, Purify, Eat, Drink, Rest, Soothe, Record, Play, Dial, Call Parent, Note, Map, Open, Unlock, Carry, Stash, Retrieve, Block, Dodge, Shove, Grapple, Swing, Spray, Trip, Sand, Lights, Wedge

## Flags/Vars
F_PortalKnown, ReddyAt, F_SafeNest_Bus, F_SafeNest_Locker,  
F_MasterKeys, ParentsConfirmed, Alerts, F_BrawlWon,  
CallInterceptMeter, CallInterceptBaseWindow, SafeCallBonus

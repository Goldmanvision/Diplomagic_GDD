# SEC-05 — CH6 AI Behavior (FSM)
Repo dir: /Patches

Raid ROE: all hostiles lethal; no arrest loop.

## Zombie FSM
States: Idle → Shamble → Lunge → Recover → Search  
- **Idle:** wander; noise check.  
- **Shamble:** toward last noise/LOS.  
- **Lunge:** if <2.5 m; wind-up 0.7 s.  
- **Recover:** 1.0 s; then Search.  
- **Staggers:** headshot, Shove.

## Night Gaunt FSM
States: Perch → Track → Dive → Grounded → FleePerch  
- **Track:** ceiling move; light hit → Grounded (1.5 s).  
- **Dive:** target sprinters first.  
- **FleePerch:** if HP <35% or light sustained.

## Cultist FSM
States: Patrol → Rite → Fire → Flinch → Retreat  
- **Rite:** channel; buffs others; interrupt on Suppress/TK Push.  
- **Fire:** .38 shots with cover seek.  
- **Retreat:** if alone and Alert High.

## Beast FSM
States: Stalk → Charge → Stun → Reacquire  
- **Charge:** 0.8 s tell; wall hit → Stun 1.0 s.

## Warden Shade FSM
States: Drift → Swipe → Phase → Disperse  
- **Phase:** 50% ballistic DR; **Ward Jam** forces Swipe.  
- **Disperse:** on low HP; brief invuln then Drift.

## Threat priority
- Gaunt on sprinters, Cultist on casters, Beast on nearest, Shade on clustered.

## Tuning hooks
- Alert High adds +1 Cultist on spawn.  
- Ammo <25% reduces spawn chance by 20% for next segment.

## UI prompts (≤14 chars)
Suppress, Frag, Shield, Ward Jam

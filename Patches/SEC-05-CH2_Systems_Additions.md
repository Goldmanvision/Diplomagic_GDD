### Liminal Loop System (CH2)
- Graph: Forest sectors A–D; Brightstar anchors {Service, Office, MPR}. Non-anchors scramble on each entry while `F_MasterKeys=0`.
- Persistence: Chalk marks persist only within 30 m of Brightstar exterior.  
- Soft reset: Failure returns to Beat 1; inventory and evidence persist; +Alert on retries from Brawl.

### Survival Meters (CH2-scoped)
- Hunger, Thirst, Warmth, Fatigue; decay only in forest. Thresholds drive “Soothe/Rest/Eat/Drink” prompts.

### Reddy Safe Nest + Cry Timer
- Nests: Bivouac, Bus Cubby, Nurse Locker.  
- Vars: `ReddyAt`, `CryCooldown`.  
- Effects: Carry = +NoiseMod, −StealthMod, +Fatigue. Cry event during calls adds meter spike.

### Parent Call FSM + Call Intercept Meter
- States: Idle → Dialing → Connected{Answered|Machine} → HangUp | Intercept.  
- `CallInterceptMeter` 0–100; at 100 → Intercept (parallel pick-up, drop line, `Alert += 1`, no parent credit).  
- Base windows by `Alert`: Low 45–60s, Med 30–45s, High 15–30s. `rate = 100 / T_base`.  
- Spikes: Reddy cry +20; door/footstep near office +10; redial within 60s +5.  
- Mitigations: lights off −10 on connect; using Nurse extension −10 start value.  
- Scoring: `SafeCallBonus` if max meter ≤70 on a successful call.

### Set Piece: Brightstar Brawl
- Enemies: Warden×2 (baton), Handyman (boxcutter), Deacon (.38, fires only with lights on).  
- Player verbs: Block, Dodge, Shove, Grapple→Disable; env: Extinguisher, Sand, Tripline, Shelf shove, Lights.  
- Stamina: drains on attack/block; regen in darkness.  
- Morale: after 2 disables, remaining enemies check flee.  
- Outcomes: `F_BrawlWon=1`, `F_MasterKeys=1`, loot Medkit+Keys+Admin map.

### Non-Lethal and Alert Scoring
- Non-lethal disables score; lethal and firearm use penalize.  
- Alert escalations reduce end-chapter rank and shorten future call windows.

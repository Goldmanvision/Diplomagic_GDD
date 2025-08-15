# SEC-05 — CH3 Fear Meter Spec

**Scope:** Unlocks in CH3 for Clara and Avery. Chapter-scoped debuff system.

## Variables
- `FearLevel` 0–100
- `FearState` {Calm, Uneasy, Afraid, Panicked}
- `FearDecayRate` per safe conditions
- `FearSpikeSources`: spectral proximity, darkness, loud stingers, low Warmth (Clara), injury (Avery)

## State thresholds
- Calm: 0–24
- Uneasy: 25–49
- Afraid: 50–74
- Panicked: 75–100

## Effects
- Uneasy: slight hand shake; minor stamina regen penalty.  
- Afraid: reduced accuracy and slower interact speed.  
- Panicked: sprint bursts only; fumbles reload/lockpick; AI more sensitive to noise.

## Modifiers
- Light source active: −5 per 10s.  
- Distance from threat: −10 per 10s after LOS break.  
- Safe Nest or Deputy presence: −15 instantly on enter.  
- Reddy nearby: −10 on enter and −1/s while present (Clara only).

## UI
- Meter visible during encounters and for 10s after.  
- No color choice specified; pulse when ≥75.  
- Placement TBD by UI doc.

## Scoring hooks
- +1 per encounter resolved while ≤49 max Fear.  
- −1 per Panicked state reached (cap −3 per chapter).

## 1994 constraints
- All effects portrayed via simple HUD meter and camera shakes; no modern VFX terminology.

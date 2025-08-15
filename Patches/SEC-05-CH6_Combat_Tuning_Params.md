# SEC-05 — CH6 Combat Tuning Params
Repo dir: /Patches

Raid ROE: lethal authorized; blue-on-blue fail. All values are starting targets.

## Player
- Sidearm DMG: 30 body / 100 head (zombie)
- Rifle DMG (if issued): 35 body / 90 head
- Shotgun DMG (slug): 80 body / 120 head
- Stamina: 100; Sprint drain 12/s; Recover 8/s (calm)
- Mana: 100; Regen only in calm windows 5/s
- Tonics: +40 Mana (cap at 100)

## Enemies
### Zombie
- HP: 100; Headshot x3; Body armor: none
- Detect: 8 m hearing; 6 m vision
- Attack: 18 dmg bite; Wind-up 0.7 s
- Spawn pack: 3–5

### Night Gaunt
- HP: 160; Stagger on light 1.5 s
- Detect: 15 m vision from above
- Attack: 28 dmg dive; Recovery 1.2 s

### Cultist
- HP: 140; Chant DR 30% until interrupted
- Detect: 12 m vision; 10 m hearing
- Attack: .38 revolver 22 dmg; Fire rate 0.5 s
- Ritual spawn: 2–3 on surge

### Beast
- HP: 220; Charge tell 0.8 s; Stun on wall hit 1.0 s
- Attack: 35 dmg gore; Cooldown 1.4 s

### Warden Shade
- HP: 90; Ballistic glaze 50% DR
- Vulnerable: Ward Jam 5 s → DR 0%
- Attack: 20 dmg swipe

## Ammo economy (1994)
- Pistol: start 60; cache +30
- Shotgun: start 12; cache +6
- Rifle: start 90; cache +45
- Tonic: 1–2 per chapter total

## Encounter pacing
- Base interval: 35–45 s between waves in Vault
- Alert High: −10 s to interval; add +1 cultist

## Friendly-fire
- Threshold: any team damage >0 → BlueOnBlue=1 → fail

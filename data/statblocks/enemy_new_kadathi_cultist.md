---
Department: Adversary & NPC Systems
Codename: Taxonomist
Type: Statblock
Status: Draft
Date: 2025-08-17
Schema: schema_statblock.md
---

id: ADV-0003-kadathi-cultist
name: New Kadathi Cultist
faction: New Kadathi Sect
tier: standard
role: support

hp: 14
morale: 7
armor: 1 (leather vest)
speed: 3.0 m/s
senses: normal; chants heighten focus
resist: fear_minor
vulnerable: bright sound shocks (handheld air horn)

attacks:
  - name: Weighted cord lash
    type: melee
    damage: 1d6
    reach/range: 1.5 m
    notes: on 6, target drops small item
  - name: Slingshot lead shot
    type: ranged
    damage: 1d6
    reach/range: 8 m
    notes: quiet; −1 to hit in wind

passives:
  - sect fervor: +1 morale if a spectral entity is present

actives:
  - name: Droning chant
    cost: 3‑turn cooldown
    effect: allies within 3 m gain +1 to next morale check

skills:
  stealth: 3
  athletics: 3
  perception: 4
  intimidation: 2
  occult: 5
  firearms: 1
  melee: 3

equipment:
  - leather vest with stitched sigil
  - slingshot with lead shot pouch
  - weighted cord
  - candle tin and matches
  - photocopied pamphlet of rites

behavior:
  ai: protect ritualist; prolong encounters
  tactics:
    - hang back and chant
    - use sling to harass investigators
    - retreat if outnumbered
  environment: basements, storage rooms, abandoned mills

rewards:
  loot: pamphlet pages with marginalia
  intel: meeting time/place cryptic hints

canon:
  appears_in: [Prologue, Ch1]
  notes: visual tie to graffiti and symbols

qa_checks:
  terminology_1994: pass
  anachronisms: none

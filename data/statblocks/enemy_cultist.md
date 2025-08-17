---
Department: Adversary & NPC Systems
Codename: Taxonomist
Type: Statblock
Status: Draft
Date: 2025-08-17
Schema: schema_statblock.md
---

id: ADV-0001-cultist
name: Occult Cell Cultist
faction: Local Occult Cell
tier: mook
role: melee

hp: 12
morale: 5
armor: 0
speed: 3.0 m/s
senses: normal vision; poor night vision
resist: fear_minor
vulnerable: intimidation

attacks:
  - name: Switchblade stab
    type: melee
    damage: 1d6
    reach/range: 1 m
    notes: +2 to hit if flanking
  - name: Tire iron swing
    type: melee
    damage: 1d6+1
    reach/range: 1 m
    notes: brief stagger on hit

passives:
  - group courage: gains +1 morale if 2+ allies adjacent

actives:
  - name: Desperate lunge
    cost: 1/encounter
    effect: move up to 2 m and attack; if miss, self‑stagger

skills:
  stealth: 3
  athletics: 4
  perception: 3
  intimidation: 2
  occult: 2
  firearms: 2
  melee: 4

equipment:
  - folding knife or switchblade
  - cheap lighter
  - payphone calling card
  - denim jacket with insignia marker

behavior:
  ai: swarm targets of opportunity
  tactics:
    - attack in pairs
    - focus isolated investigators
    - flee if leader drops
  environment: back alleys, basements, abandoned storefronts

rewards:
  loot: calling card with partial PIN; matchbook with address
  intel: cell meeting place hint

canon:
  appears_in: [Prologue, Ch1]
  notes: tie to early sightings and graffiti

qa_checks:
  terminology_1994: pass
  anachronisms: none

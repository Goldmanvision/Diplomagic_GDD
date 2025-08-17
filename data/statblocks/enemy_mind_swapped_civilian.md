---
Department: Adversary & NPC Systems
Codename: Taxonomist
Type: Statblock
Status: Draft
Date: 2025-08-17
Schema: schema_statblock.md
---

id: ADV-0002-mindswap
name: Mind‑Swapped Civilian
faction: independent (compelled)
tier: standard
role: control

hp: 18
morale: 8
armor: 0
speed: 3.0 m/s
senses: heightened awareness; dull pain response
resist: charm, fear_minor
vulnerable: bright light exposure

attacks:
  - name: Improvised swing
    type: melee
    damage: 1d6
    reach/range: 1 m
    notes: uses nearby object (lamp, pipe, wrench)
  - name: Uncanny stare
    type: special
    damage: —
    reach/range: 5 m
    notes: target morale check or lose next reaction

passives:
  - dampened pain: ignore first stagger each scene

actives:
  - name: Fugue step
    cost: 2‑turn cooldown
    effect: immediate move 2 m ignoring engagement

skills:
  stealth: 2
  athletics: 3
  perception: 6
  intimidation: 1
  occult: 0
  firearms: 0
  melee: 3

equipment:
  - civilian clothing
  - house keys
  - wallet with IDs

behavior:
  ai: delay and obstruct investigators; escape if cornered
  tactics:
    - use crowds as cover
    - break line of sight, then flee
    - avoid lethal force
  environment: apartments, offices, public spaces

rewards:
  loot: personal effects usable for leads
  intel: fragmentary recall of spectral presence

canon:
  appears_in: [Ch1, Ch2]
  notes: links to spectral entity sightings

qa_checks:
  terminology_1994: pass
  anachronisms: none

---
Department: Adversary & NPC Systems
Codename: Taxonomist
Type: Statblock
Status: Draft
Date: 2025-08-17
Schema: schema_statblock.md
---

id: ADV-0004-spectral
name: Spectral Entity
faction: independent
tier: elite
role: control

hp: 24
morale: —
armor: 2 (ethereal damping)
speed: 0 / glide 2.5 m/s
senses: sees heat shimmer; ignores darkness
resist: fear, poison, mundane restraints
vulnerable: bright continuous light; iron filings cloud

attacks:
  - name: Chill touch
    type: special
    damage: 1d6 cold + morale check
    reach/range: 1 m
    notes: on fail, target loses next reaction
  - name: Pressure wave
    type: special
    damage: 1d4
    reach/range: 4 m cone
    notes: knocks small objects; open flames may gutter

passives:
  - incorporeal drift: pass through thin barriers slowly
  - radio hush: nearby radios pick up static

actives:
  - name: Linger
    cost: 3‑turn cooldown
    effect: anchor to a spot; becomes partially visible; attacks gain +1 for 1 round

skills:
  stealth: 7
  athletics: 0
  perception: 6
  intimidation: 5
  occult: 6
  firearms: 0
  melee: 0

equipment:
  - none

behavior:
  ai: unsettle, isolate, then test defenses
  tactics:
    - separate targets with pressure wave
    - avoid direct damage; probe for weaknesses
    - withdraw if bright light sustained
  environment: cold spots, basements, near water leaks

rewards:
  loot: none
  intel: environmental traces; salt residue patterns; EMF spikes (period meters limited)

canon:
  appears_in: [Prologue, Ch1, Ch2]
  notes: ties clues found on civilians and cultists

qa_checks:
  terminology_1994: pass
  anachronisms: none

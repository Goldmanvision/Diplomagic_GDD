---
Department: Adversary & NPC Systems
Codename: Taxonomist
Type: Schema
Status: Active
Date: 2025-08-17
---

# Statblock Schema — v0.1
Use this template for all adversaries. Keep numbers modest. Balance later.

## Identity
- id: ADV-####-slug
- name: <string>
- faction: <string or 'independent'>
- tier: mook | standard | elite | boss
- role: melee | ranged | support | control | special

## Core Stats
- hp: <int>            # 5–80 typical
- morale: <int>        # 0–12
- armor: <int>         # 0–6
- speed: <m/s or tiles>
- senses: <notes>
- resist: <keywords>
- vulnerable: <keywords>

## Attacks
- attacks: 
  - name: <string>
    type: melee | ranged | psychic | special
    damage: <dice or flat>
    reach/range: <m or tiles>
    notes: <on-hit effects>

## Abilities
- passives: [<strings>]
- actives:
  - name: <string>
    cost: <action or cooldown>
    effect: <string>

## Skills
- stealth: 0–10
- athletics: 0–10
- perception: 0–10
- intimidation: 0–10
- occult: 0–10
- firearms: 0–10
- melee: 0–10

## Equipment (1994)
List period-correct items only. Examples: pocket knife, tire iron, .38 revolver, disposable lighter, payphone card.

## Behavior
- ai: <one-line goal>
- tactics: <2–4 bullets>
- environment: <where encountered>

## Rewards
- loot: <mundane loot; keep modest>
- intel: <clues unlocked>

## Canon
- appears_in: [Prologue, Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Epilogue]
- notes: <tie-ins>

## QA Checks
- terminology_1994: pass|needs-fix
- anachronisms: none|list

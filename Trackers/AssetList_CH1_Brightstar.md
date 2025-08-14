# CH1 — “Simple Curiosity” Asset List
Version: v0.1
Date: 2025-08-14 11:57:29 UTC
Owner: Nick Goldman
Scope: Interleaved Clara+Reddy at Brightstar and Avery roadside stop. 1994 period accuracy.

## Environments
### Brightstar Daycare (day→dusk)
- Intake foyer: sign‑in desk, ledger, wall clock, corkboard, “Visitors Sign In” sign.
- Classroom: low tables, chairs, cubbies, toys (period‑safe), bulletin board.
- Infirmary: cot, cabinet, sink, sharps container (period), med posters.
- Storage hallway: supply drawer (MEDSTAT note‑card), janitor closet door.
- Exterior exit: door with crash bar, small lot, chain‑link glimpse.
- Lighting: warm fluorescents inside; dusk exterior rig.

### Avery roadside stop (same day)
- Two‑lane rural road segment, shoulder, patrol car prop, cones.
- Mobile locker case on a folding table.

## Characters
- Clara Winston; Reddy (child companion); 1–2 staffers (patrol path); 1 child NPC for care task.
- Avery Jordan; local deputy (briefing); adult suspect.

## Props — Clara leg
- **MEDSTAT handheld** + **RF wrist‑band**; **MEDSTAT note‑card** (pickup/insert).
- Paper visitor ledger + pen; landline phone at desk.
- Care task set: water cup, bandage box, sticker sheet.
- Period dressing: posters, toys, cleaning supplies.
- Door buzzer/intercom box at foyer.

## Props — Avery leg
- 35mm SLR camera + flash; evidence bags; pre‑printed tags; clipboard, pens.
- Mobile locker case (portable cubbies, log book, stamper).
- Patrol car light bar (non‑interactive), roadside cones.
- VHF/UHF handheld radio + shoulder mic.

## Anim/FX/SFX
- Anim: sign‑in, open drawer, insert card, stealth crouch/peek, simple care action.
- Anim: challenge, cuff, search pockets, photo, locker handoff.
- VFX: subtle dust motes interior; daylight glare at exit; paper tear at custody.
- SFX: foyer ambience, classroom murmur, phone click; roadside wind, radio chirps.

## UI/HUD
- Prompts per CH1 Beat→Objective: SIGN IN, FIND CARD, INSERT, FOLLOW, AVOID, CARE, CALL; CHALLENGE, CUFF, SEARCH, CAMERA, BAG/TAG/LOG, LOCKER, REPORT.
- Toast: “Note logged from earlier chart.” on card insert.
- Subtitles default ON; speaker tags.

## Budgets
- Interior Brightstar ≤ 0.9M tris, ≤ 1,300 draws; GPU ≤ 14 ms @1080p mid tier.
- Roadside stop ≤ 0.8M tris, ≤ 1,100 draws; GPU ≤ 14 ms.
- Active voices ≤ 32; particle counts minimal.

## UE5 Paths
- `/Content/Diplomagic/Art/Environments/Brightstar/…`
- `/Content/Diplomagic/Art/Props/Devices/MEDSTAT/…` (note‑card mesh/material)
- `/Content/Diplomagic/Art/Props/Police/MobileLocker/…`
- `/Content/Diplomagic/Design/Blueprints/CH1/…`

## Test hooks
- Card insert triggers: `medstat_upgrade_card_found`, `medstat_upgrade_card_inserted`, `pin_auto_log_created`.
- Custody checklist sets `custody_complete=true`.

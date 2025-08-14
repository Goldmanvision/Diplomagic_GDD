# 0B — Clara Prologue Asset List (Betsy’s Apt, 1994)
Version: v0.1
Date: 2025-08-14 10:36:14 UTC
Owner: Nick Goldman
Scope: Interior apartment kit, caregiving props, MEDSTAT device. Period-accurate; **no FieldPad/TAPLINE**.

## Environment
- Apartment interior: entry hallway, living room, small kitchen nook, bathroom door stub. One-window light rig.
- Exterior buzzer panel at hallway (single prop with intercom grooves).

## Characters
- Clara Winston — civilian outfit, soft satchel.
- Betsy Lumbar — cardigan, slippers, frail posture.

## Props — Care & MEDSTAT
- **MEDSTAT handheld** with monochrome LCD, soft keys; **RF wrist‑band module**; finger pulse‑ox clip; BP cuff; thermometer probe.
- Paper patient chart + clipboard + pen.
- Pill organizer (7‑day), medication bottles (fictional labels).
- Kettle, mugs, tea box, sugar bowl, spoon, dish towel.
- Trash basket, tissue box, cleaning cloth.
- Landline phone (corded), notepad, pencil.
- **Brightstar lapel pin** (pickup/inspect) — same **cult symbol** mask as Hauser pistol.
- Kitchen table set: coasters, mail stack, TV remote, VHS case (flavor).

## Props — Misc & Signage
- Wall calendar, framed photo, lamp, throw blanket.
- Buzzer/intercom faceplate at entry; apartment number placard.
- Knife prop for Reddy‑POV beat (behind Reddy; not interactable).

## Anim/FX/SFX
- Anim: greet, place satchel, clip pulse‑ox, wrap BP cuff, measure temp, pour tea, arrange pills, tidy table, note on chart.
- VFX: gentle kettle steam, subtle dust motes.
- SFX: door buzzer, landline dial tone and click, kettle boil, cup/clink, pill rattle, paper/pen scribble, apartment hum.

## UI/HUD (diegetic cues)
- Prompts per tutorial pack: BUZZER, CALL, GREET, P‑OX, BP, TEMP, PILLS, TEA, TIDY, SWAP POV, PIN FOUND.
- Subtitle tags “[Clara] … / [Betsy] …” default ON.

## Period/Accuracy notes
- **No FieldPad/TAPLINE** in 0B. All notes on **paper chart**.
- Caller ID not guaranteed; phone visuals are generic.
- CRT TV/VHS as background only; no modern devices.
- MEDSTAT note‑card upgrade appears **in CH1** at Brightstar Daycare (not here).

## Budgets (targets)
- Interior set ≤ 0.8M tris, ≤ 1,200 draws; GPU ≤ 14 ms @1080p mid-tier.
- Active audio voices ≤ 24.
- Texture memory ≤ 384 MB; pin + symbol uses shared 512 px mask.

## Naming & Paths (UE5)
- `/Content/Diplomagic/Art/Environments/Apartments/Betsy/…`
- `/Content/Diplomagic/Art/Props/Care/…`
- MEDSTAT: `/Content/Diplomagic/Art/Props/Devices/MEDSTAT/…`
- Pin: `/Content/Diplomagic/Art/Props/Collectibles/BrightstarPin/…` (mesh, mat, symbol decal).

## Test hooks
- Pin inspect sets `brightstar_pin_found = true` (telemetry).
- Reddy‑POV trigger `reddy_pov_played = true`.
- Vitals logged increments `vitals_logged` counter.

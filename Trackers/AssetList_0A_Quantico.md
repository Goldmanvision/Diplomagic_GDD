# 0A — Avery Prologue Asset List (Quantico, 1989)
Version: v0.1
Date: 2025-08-14 10:36:14 UTC
Owner: Nick Goldman
Scope: Environment, characters, props, SFX/VFX, UI for Hogan’s Alley (night). Period-accurate; analog only.

## Environment
- Hogan’s Alley street set: 6–8 façade modules (storefront, tenement, alley cut, parking lot).
- Range lane: 3 paper target lanes + safety line + backstop + brass catch mesh.
- Locker window: counter, sliding glass, evidence cubbies.
- Precinct corner (implied): doorway and wall dressing for handoff framing.

## Characters
- Eddie Paldino (instructor) — LOD0/1/2, simple holster rig, radio mic.
- 2–4 role-players (trainees) — mixed bodytypes; one “contact” suspect; one escort target.
- Avery Jordan trainee variant — training belt, empty holster.

## Props — Training & ROE
- Handcuffs (chain), cuff pouch, training belt.
- Paper property sheet clipboard + pens.
- Evidence bags (paper), pre-printed tags (no printer in 1989).
- Mock contraband items (baggie, knife sheath, wallet).
- 35mm SLR camera + film canister + simple flash (period look).
- Locker window set dressing: trays, logbook, date/time stamper.
- VHF/UHF handheld radio (Motorola-style) + shoulder mic.
- Range set: target stands (IPS/steel), pulley or manual frame, shot timer box, eye/ear pro.
- **Hauser’s pistol (Mauser C96)** hero prop with **cult symbol** engraving (separate decal/mask). Shippable + inert variants.
- Non‑lethal marker rounds (range demo) — texture swap only; range‑only use.

## Props — Misc & Signage
- ROE poster, “Safety First” placards, range rules board.
- Payphone booth (optional flavor for Alley edge).

## Anim/FX/SFX
- Anim: challenge posture, cuffing, escort loop, search pockets, camera shoot, locker handoff, range stances, dual-wield stance.
- VFX: small muzzle flash (range only), paper tear, light dust puffs on targets.
- SFX: radio chirp, cuff ratchet, camera shutter, paper/tag rustle, range gunshots (indoor/outdoor), brass tinkle, footstep gravel.

## UI/HUD (diegetic cues)
- Floating prompts (≤14 chars) per tutorial pack: CHALLENGE, CUFF, SEARCH, CAMERA, BAG, TAG, LOG, LOCKER, FIRE, DUAL WIELD, AIM MODE, REPORT.
- Subtitle tags “[Eddie] …” default ON.

## Period/Accuracy notes
- No FieldPad/TAPLINE. No digital tags. All custody on paper.
- Telephonic warrant mentioned by Eddie only; no device or call UI shown.

## Budgets (targets)
- Exterior set ≤ 1.5M tris, ≤ 1,800 draws; GPU ≤ 14 ms @1080p mid-tier (SEC‑11).
- Active audio voices ≤ 32; cull reverb tails on range shots.
- Texture memory ≤ 512 MB for set; hero pistol uses unique 1k mask for symbol.

## Naming & Paths (UE5)
- `/Content/Diplomagic/Art/Environments/TrainingTown/…`
- `/Content/Diplomagic/Art/Props/Police/…`
- `/Content/Diplomagic/Art/Props/Range/…`
- Hero pistol: `/Content/Diplomagic/Art/Props/Weapons/Hauser_C96/` (mesh, mat, decal).

## Test hooks
- Target hitboxes report CSV (range spots).
- Locker window triggers `custody_complete` on valid handoff.
- Award gate tracks score ≥90 and ROE violations == 0 (for pistol award path).

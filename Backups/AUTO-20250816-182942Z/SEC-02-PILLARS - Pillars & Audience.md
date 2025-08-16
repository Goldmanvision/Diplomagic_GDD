# [SEC-02-PILLARS] Pillars & Audience
Version: v0.1 (no change to Master header)  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-01-FRONT — Front Matter & Executive Summary`
- `SEC-03-NARRATIVE — Narrative`
- `SEC-04-LOOPS — Core Gameplay Loops`

\# Patch Instructions for Existing MASTER — SEC-02



\#\# 1\) Replace this single manifest row


\`| SEC-02-PILLARS | Pillars \+ audience | v0.1 | 2025-08-11 | approved | archived to Master |\`

\#\# 2\) Append this section to the end of MASTER (add a \`\[\[PAGEBREAK\]\]\` before it)

\\\[\\\[PAGEBREAK\]\]

\# \*\*\\\[SEC-02-PILLARS\] Design Pillars & Target Audience\*\*


Owner: Nick Goldman

\#\# \*\*2.1 Product Pillars\*\*

Each pillar includes guardrails and checks used in reviews and greenlight gates.

\#\#\# \*\*P1. Dual‑Protagonist Parallax Narrative\*\*

\*\*Definition.\*\* The story alternates between Avery (procedural, institutional) and Clara (survival, improvisational). They converge mid‑campaign and affect shared world state.

\*\*Why.\*\* Contrast keeps pacing fresh and reinforces theme: human systems vs the unknowable.

\*\*Design Rules.\*\*

\* Do: Give each character exclusive mechanics, verbs, and UI affordances.

\* Do: Mirror key events from different viewpoints.

\* Don’t: Duplicate missions one‑to‑one or let skill trees collapse into sameness.

  \*\*Checks.\*\* ≥30% missions feature explicit cross‑impact; shared state is reflected in dialog, evidence, and encounters.

\#\#\# \*\*P2. Procedural Realism (1994)\*\*

\*\*Definition.\*\* FBI‑accurate process for Avery; era‑correct civilian problem‑solving for Clara. Evidence handling, communications, and tactics reflect 1994 constraints.

\*\*Why.\*\* Grounded realism amplifies dread and differentiates the game.

\*\*Design Rules.\*\*

\* Do: Enforce chain‑of‑custody, warrants, ROE for Avery.

\* Do: Prefer analog friction for Clara: paper trails, payphones, physical locks.

\* Don’t: Add modern conveniences (GPS, smartphones, cloud saves in‑fiction).

  \*\*Checks.\*\* Every Avery mission features at least one procedural gate; Clara scenarios require at least one analog workaround.

\#\#\# \*\*P3. Investigative Agency → Consequence\*\*

\*\*Definition.\*\* Player‑led inquiry drives outcomes. Evidence unlocks dialog, access, and tactical options; poor prep increases risk.

\*\*Why.\*\* Investigation is core loop glue between exploration and combat.

\*\*Design Rules.\*\*

\* Do: Score evidence quality; branch encounters by prep level.

\* Do: Surface inference tools and uncertainty.

\* Don’t: Solve with canned cutscene reveals after linear set pieces.

  \*\*Checks.\*\* Each mission supports ≥2 materially different resolutions tied to evidence tiers.

\#\#\# \*\*P4. Devices as Mechanics (FieldPad, TAPLINE, MEDSTAT)\*\*

\*\*Definition.\*\* Diegetic UIs modeled on IBM Simon/Palm/Apple Newton. They gate features and tutorialize through use.

\*\*Why.\*\* Cohesive UX and fiction alignment.

\*\*Design Rules.\*\*

\* Do: Keep screens two‑tone, large hit targets, latency modeled.

\* Do: Unlock apps through story beats; respect battery/connection constraints.

\* Don’t: Add non‑diegetic overlays that duplicate device functions.

  \*\*Checks.\*\* ≥70% mission interactions route through device apps; device upgrades change play, not stats alone.

\#\#\# \*\*P5. Dread‑First Aesthetics, PS1‑era Readability\*\*

\*\*Definition.\*\* Low‑poly silhouettes with modern lighting and post‑FX. Horror tone favors implication over gore.

\*\*Why.\*\* Distinct look with high performance and clear gameplay readability.

\*\*Design Rules.\*\*

\* Do: Prioritize silhouette, texture economy, fog volumes, limited palette.

\* Don’t: Photoreal blood‑porn; avoid comedic gore.

  \*\*Checks.\*\* Heuristic readability pass per level; \<5% of playtest deaths attributed to visual ambiguity.

\#\# \*\*2.2 Player Experience Goals (PXG)\*\*

\* Feel competent assembling truth from scraps under time pressure.

\* Feel the weight of procedure versus urgency.

\* Fear the unknown without losing mechanical clarity.

\* See choices echoed later by changed spaces, NPCs, and evidence trails.

\#\# \*\*2.3 Target Audience\*\*

\*\*Primary.\*\* PC players 18–45 who enjoy investigative horror, immersive sims, and tactical shooters.

\*\*Secondary.\*\* Narrative RPG and survival horror fans; mod‑curious PC communities.

\*\*Accessibility baseline.\*\* Subtitles, color‑blind safe palettes, remappable inputs, aim assist options, difficulty modifiers for information density.

\#\# \*\*2.4 Competitive Comps & Positioning\*\*

| Title/Ref               | Why it’s relevant              | Our differentiation                           |

| \----------------------- | \------------------------------ | \--------------------------------------------- |

| The X‑Files (TV)        | Tone, 1990s federal milieu     | Playable procedure, dual‑POV convergence      |

| Resident Evil (classic) | Survival horror pacing         | Investigation and procedure drive fights      |

| Signalis                | Low‑poly austerity, dread      | Dual devices \+ institutional realism          |

| Disco Elysium           | Evidence‑led narrative systems | First‑person, tactical risk, 1994 constraints |

\*\*Positioning Statement.\*\* An investigative horror where dual protagonists use period‑authentic tools to expose a cosmic intrusion, delivering grounded tension and meaningful agency.

\#\# \*\*2.5 Platform & Input Assumptions\*\*

\* PC first. Keyboard/mouse and gamepad parity targets.

\* Haptics optional on supported controllers.

\* No mandatory online features for core loop.

\#\# \*\*2.6 Content Rating Strategy\*\*

Target: ESRB \*\*M\*\* / PEGI \*\*18\*\*. Violence, language, horror themes. Avoid sexual content and torture porn. Use content warnings for specific scenes.

\#\# \*\*2.7 Success Criteria\*\*

\*\*Qualitative.\*\* Playtesters describe “investigation mattered,” “devices felt real,” “deaths felt fair.”

\*\*Quantitative.\*\*

\* Evidence systems used in ≥80% of missions.

\* Two or more valid mission resolutions logged in ≥60% of missions.

\* \<5% UI errors from discoverability in device apps by final beta.

\* Day‑1 crash‑free rate P90 ≥ 99.5% on min‑spec PC.

\#\# \*\*2.8 Risks & Mitigations\*\*

\* \*\*Procedural friction\*\* may frustrate: provide optional briefs, tooltips, and case files.

\* \*\*Dual‑protagonist scope\*\*: share assets via locations re‑used with altered objectives.

\* \*\*Device UI overload\*\*: progressive disclosure; tutorialize via cases, not modal popups.

\#\# \*\*2.9 Terminology\*\*

\* \*\*FieldPad\*\*: evidence capture and casework.

\* \*\*TAPLINE\*\*: communications interception and analysis.

\* \*\*MEDSTAT\*\*: biometrics, triage, and team status.

\#\# \*\*2.10 Approvals\*\*

On approval: archive to MASTER as \`\[SEC-02-PILLARS\] v0.1\` and add manifest row. Next section: \*\*SEC‑03 Narrative\*\*.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

# SEC-02 — Master Flags Matrix (CH5→CH6)
Repo dir: /Patches

## Legend
Y = set, ? = optional/branch, — = not used

| Flag | CH5 | CH6 | Purpose |
|---|:---:|:---:|---|
| F_Rogue | Y | Y | Avery off-book; FBI access limited |
| F_KrillHandler | Y | Y | Krill as sole handler |
| F_HandlerLost | ? | — | Miss 3 pager windows |
| F_ArrivedNYC | Y | — | Hotel check-in |
| F_FranklinMurdered | Y | — | Timing after debrief |
| F_EscapeHotel | Y | — | Morning raid escape |
| F_WarrantSRS | Y | — | SRS warrant prepared (legacy; UC path now rogue) |
| F_DLampLocated | Y | — | Found D-LAMP campus lead |
| F_DLampEntered | Y | — | Entered D-LAMP (deep site) |
| F_WV_IslandFound | Y | — | Found WV island elevator |
| F_ElevatorDown | Y | — | 1-mile descent complete |
| F_DLampUnderground | Y | — | Deep D-LAMP entered |
| F_StarVampireDefeated | Y | — | Pump cavern mini-boss |
| F_RouteKey | Y | — | Vehicle route key acquired |
| F_DLampRover | Y | — | Rover secured |
| F_IronHighwayEntered | Y | — | Driving tunnel route |
| F_SRS_SecretAnnexSeen | Y | — | Bulkhead reached |
| F_ClaraToBetsy | Y | — | Clara goes to Betsy |
| F_BetsyBossDefeated | ? | — | Boss cleared if no raid bypass |
| F_BetsyRaidBypass | ? | — | Raid bypass active |
| F_BetsyHouseCleared | ? | — | House swept |
| F_ClaraFollowsAvery | Y | — | Clara + Reddy reconverge |
| F_UCBriefed | — | Y | Final UC pre-brief (rogue posture) |
| F_SafehouseSting | — | Y | Safehouse raid done |
| F_SRSBreach | — | Y | Annex ingress |
| F_CoreFound | — | Y | Core Gallery located |
| F_RitualIgnited | — | Y | Ritual started |
| F_End_Contain | — | ? | Ending A selected |
| F_End_Escape | — | ? | Ending B selected |
| F_End_BlackFile | — | ? | Ending C selected |
| BlueOnBlue | — | ? | 1 on friendly-fire → fail |
| EvidenceCount | — | Y | CH6 cap 3 |
| F_Spellbook | Y | — | From CH4 boss |
| F_Spell_FastTravel | Y | — | Phrase learned |
| SpellsKnown[] | Y | Y | Persisted phrases |
| SpellsEquippedL/R | Y | Y | Equip slots |
| Scrolls[] | Y | Y | Single-use items |

Notes: Phrase remains ambient only — “the stars are right tonight.” Prompts ≤14 chars.

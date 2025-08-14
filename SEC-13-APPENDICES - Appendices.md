# [SEC-13-APPENDICES] Appendices
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-14-QA — Quality Assurance Test Plan`
- `TDD-EVIDENCE+FIELDPAD — Technical Design Document`

## **13.1 Glossary**

* **Caseboard**: Graph of evidence, persons, locations, threads.
* **Chain‑of‑custody**: Steps that keep A‑tier evidence valid.
* **Heat**: Systemic alert level from player actions.
* **Kadath (New/Unknown)**: Liminal layers affecting space, rules.
* **MEDSTAT / FieldPad / TAPLINE**: Devices for vitals, casework, signals.

## **13.2 Acronyms**

| Term | Meaning |
|---|---|
| AA | Anti‑Aliasing |
| DDC | Derived Data Cache |
| EA | Early Access |
| GI | Global Illumination |
| KPI | Key Performance Indicator |
| LOD | Level of Detail |
| LUFS | Loudness Units Full Scale |
| POI | Point of Interest |
| PSO | Pipeline State Object |
| ROE | Rules of Engagement |
| RTPC | Real‑Time Parameter Control |

## **13.3 Data Schemas (authoritative keys)**

**Evidence Item (save/telemetry)**

```json
{
  "id": "A-014",
  "tier": "A|B|C",
  "quality": 78,
  "chain": {
    "photo": true,
    "collect": true,
    "bag": true,
    "tag": true,
    "log": true,
    "sealIntact": true
  },
  "links": ["case:82", "victim:2", "loc:locker3"],
  "contam": 0,
  "time": "1994-10-31T14:41:00Z"
}
```

**Caseboard Node/Edge**

```json
{
  "nodes": [
    {"id": "victim:2", "type": "person"},
    {"id": "evidence:A-014", "type": "evidence"}
  ],
  "edges": [
    {"from": "victim:2", "to": "evidence:A-014", "rel": "linked"}
  ]
}
```

**Telemetry Event (subset)**

```json
[
  {"evt": "evidence_logged", "id": "A-014", "mission": "CH1_KidsKamp"},
  {"evt": "arrest", "npc": "guard_03", "nonlethal": true},
  {"evt": "stealth_resolve", "mode": "bypass"}
]
```

## **13.4 Checklists**

**Level Readability**

* Silhouettes readable at min spec.
* Patrol lines and cover affordances obvious.
* Fog volumes tuned; no glare hotspots.

**Device UX**

* Nav path discoverable within 6 s.
* Tap targets ≥ 32×32 px @1080p.
* Error states readable; destructive ops confirmed.

**Performance Pass**

* Tris/DC within SEC‑08/09 caps.
* GPU ≤ 14 ms @1080p min spec.
* Audio voices ≤ 48; particle caps met.

**Accessibility**

* Subtitles on; UI scale works.
* High‑contrast skin verified.
* Camera shake/flash reduction toggles.

## **13.5 Tuning Tables (defaults)**

| Parameter | Default | Notes |
|---|---|---|
| Detection base | 0.35 | Stealth visibility curve start |
| Noise budget walk/crouch/sprint | 5 / 2 / 12 | dB‑like units |
| Arrest surrender base | 0.25 | Avery compliance check |
| Evidence BaseTier A/B/C | 50 / 30 / 15 | See SEC‑05 |

## **13.6 Input Reference**

* **Keyboard/Mouse**: WASD move, Q/E lean, C crouch, Z prone, F interact, R reload, 1–4 quick slots, Tab device pane, M map, Esc pause.
* **Gamepad**: LS move, RS look, LB/RB cycle, LT aim, RT fire/apply, Y device swap, X interact, A confirm, B back.
* **Avery**: Hold T challenge, G cuff.
* **Clara**: Hold G place trap, V whistle.

## **13.7 Versioning & Build IDs**

* Scheme: `vMAJOR.MINOR.PATCH_YYYY‑MM‑DD` (e.g., `v1.0.0_2025‑10‑31`).
* Branch map: `Dev → Release/* → hotfix` tags.
* Changelogs per section using IDs `[SEC‑NN‑TAG]`.

## **13.8 Repository & Paths (UE5)**

```
/Content/Diplomagic/
  Art/{Characters,Props,Environments,Materials}
  UI/
  VFX/
  Audio/{SFX,Music,VO}
  Design/Blueprints/
/Docs/{GDD, Licenses, Style, Build}
```

## **13.9 Store Page Content Warnings (template)**

Contains intense violence, blood, strong language, and horror themes. No on‑screen harm to minors. Options include reduced‑gore and content warnings.

## **13.10 Contractor Handoff Pack**

* Current GDD sections.
* References (SEC‑08).
* Naming + folder rules.
* Budgets and KPIs.
* Sample assets and target captures.

## **13.11 Third‑Party & OSS Attributions**

* Fonts: VT323 (SIL OFL), Inter (SIL OFL), IBM Plex Sans (SIL OFL), JetBrains Mono (Apache 2.0).
* Engine and Marketplace items per their EULAs.
* Maintain `/Docs/Licenses/NOTICE.md`.

## **13.12 UI String Keys**

* Pattern: `ui.<area>.<screen>.<element>`
* Example: `ui.fieldpad.evidence.link_button`

## **13.13 Milestone Manifest & Changelog**

| Section | Version | Date | Summary |
|---|---|---|---|
| SEC‑01‑FRONT | v0.2 | 2025‑08‑11 | Exec summary finalized |
| SEC‑02‑PILLARS | v0.1 | 2025‑08‑11 | Pillars/audience |
| … | … | … | … |

## **13.14 Contacts**

* **Owner**: Nick Goldman — design, tech, approvals.
* **External**: to be filled per contract.

## **13.15 Figures & Diagrams**

* UML: `Diplomagic_UML.drawio`, `Statlines_and_Environmental_Systems.drawio` → export PNG/PDF for inclusion.
* Loop diagrams (SEC‑04), device flows (SEC‑07).

## **13.16 Templates (files to create)**

* `Docs/Templates/bug_report.md`
* `Docs/Templates/art_hand-off.md`
* `Docs/Templates/audio_cue_sheet.csv`
* `Docs/Templates/changelog.md`

## **13.17 Approvals**

On approval: archive to MASTER as `[SEC-13-APPENDICES] v0.1` and update manifest.

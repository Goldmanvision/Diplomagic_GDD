# [TDD-EVIDENCE+FIELDPAD] Technical Design Document
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-05-SYSTEMS — Systems & Mechanics`
- `SEC-06-WORLD — World, Levels, & Content`
- `SEC-07-UI — UI/UX (Devices, HUD, Menus)`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-13-APPENDICES — Appendices`

## **Scope**
Evidence system and the FieldPad device apps (Camera, Evidence, Caseboard, Warrant, Map, Contacts). Integrates with SEC‑05 (Systems), SEC‑07 (UI), SEC‑06 (World). Targets slice→gold.

## **1) Goals, Non‑Goals, Dependencies**

### Goals
- Make evidence meaningful, not collectible spam.
- Enforce simplified chain‑of‑custody (bag→tag→log) with clear feedback.
- Gate warrants and scene actions by evidence quality (Q) and legality.
- Keep 1994 friction while preserving play flow.

### Non‑Goals
- No lab minigames. No DNA/AFIS sims. No networked case sharing.

### Dependencies
- SEC‑05 §5.7 (Evidence & Casework), §5.9 (FieldPad), §5.6 (ROE).
- SEC‑07 §7.4.1 (FieldPad UI) and global HUD.
- SEC‑13 §13.D (Telemetry), §13.E (Save), §13.I (Localization).

## **2) Core Concepts**
- **Evidence Item**: world pickup or documentable object bound to a Case.
- **Chain of Custody (CoC)**: ordered steps; breaks invalidate A‑tier for warrants until supervisor sign‑off.
- **Quality Score (Q 0–100)**: formula determines gate strength.
- **Warrant Score (WS 0–100)**: function of linked evidence and affidavit quality.

## **3) State Machines**

### 3.1 Evidence Item Lifecycle
Discovered → Photographed → Collected → Bagged → Tagged → Logged → Stored/Transferred → Analyzed (narrative) → Released

**Guards**
- Photographed required before Collected for A/B tiers.
- Bagged requires available bag item; Tagged requires label printer or pre‑printed tags.
- Logged requires FieldPad online state (device storage OK, sync later).
- Stored/Transferred occurs at evidence locker/NPC handoff.

### 3.2 Seal State
Intact → Broken → Resealed

- If **Broken** before **Logged**, apply `ContamPenalty` and downgrade tier usage for warrants.

### 3.3 CoC Validity
Valid ↔ Invalid (break) ↔ Remediated (supervisor sign‑off)

- Remediation halves `ContamPenalty` and restores warrant eligibility for **B‑tier** only.

## **4) Data Model (Save‑Ready)**

### 4.1 EvidenceItem JSON
```json
{
  "id": "A-014",
  "case_id": 82,
  "tier": "A",
  "category": "fiber",
  "subtype": "carpet_fiber",
  "world_ref": "L-01_S-04_floor_vent",
  "photos": ["IMG_0142"],
  "chain": {
    "photographed": true,
    "collected": true,
    "bagged": true,
    "tagged": true,
    "logged": true,
    "stored": true,
    "seal_state": "Intact",
    "break_log": []
  },
  "handlers": ["Clara","Avery"],
  "locker_id": "LKR-3",
  "q_components": {
    "base_tier": 50,
    "chain_bonus": 18,
    "contam_penalty": 0,
    "time_decay": 4,
    "crosslink_bonus": 14
  },
  "Q": 78,
  "links": ["TPL-07","W-03"],
  "notes": "Found under vent panel"
}
```

### 4.2 Casefile
```json
{
  "case_id": 82,
  "title": "Brightstar Site",
  "items": ["A-014","B-021","C-005"],
  "suspects": ["Langston_Gromley"],
  "warrants": ["WRT-82-01"],
  "graph": { "nodes":[], "links":[] }
}
```

### 4.3 Warrant
```json
{
  "warrant_id": "WRT-82-01",
  "case_id": 82,
  "judge": "S_Hartford",
  "affidavit_text": "...",
  "linked_items": ["A-014","TPL-07"],
  "WS": 62,
  "status": "Submitted|Approved|Denied"
}
```

**Constraints**
- `id` is unique within `case_id`.
- `tier ∈ {A,B,C}`.
- Photos stored as compressed PNG/JPEG with EXIF‑like header.

## **5) Formulas & Scoring**

**Evidence Quality (SEC‑05 baseline)**

`Q = BaseTier + ChainBonus − ContamPenalty − TimeDecay + CrosslinkBonus`

- BaseTier: A=50, B=30, C=15.
- ChainBonus: +0…20 if bag→tag→log completed.
- ContamPenalty: −0…25 for breaks or missing steps.
- TimeDecay: −0…10 for perishable/late log.
- CrosslinkBonus: +0…15 for ≥2 corroborations.

**Warrant Score (WS)**

`WS = clamp( Σ(Q_linked) × K_evidence + K_affidavit − Penalties , 0, 100 )`

- `K_evidence = 0.35` (sum of Q capped at 200 pre‑scale).
- `K_affidavit = 0…30` from template completeness and length.
- Penalties: CoC invalid items ignored; exigent use applies −15 risk note.
- Gate: WS ≥ 60 → Approved; 45–59 → Judge Questions; <45 → Denied.

## **6) FieldPad Apps — UX Flows (SEC‑07 parity)**
Latency target per action ≤ 250 ms. All destructive ops require confirm.

### 6.1 Camera
- Open → focus reticle → **CAPTURE** → store `IMG_####` with timestamp and location.
- Auto‑suggest **Tag** if object outline detected (simple bounding box, no hard ML).

### 6.2 Evidence (List + Detail)
- **List**: filter by tier, CoC state, linked/unlinked, locker.
- **Detail actions**: PHOTO VIEW, CHAIN STEP, LINK, LOCKER, NOTES.

**CHAIN STEP modal**
- Shows checklist: Photo ✓ → Collect ✓ → Bag □ → Tag □ → Log □.
- Selecting a step records timestamp + handler.
- If Seal broken, banner: “Seal broken: A‑tier invalid until sign‑off.”

### 6.3 Caseboard
- Node graph for items, suspects, locations.
- Actions: ADD LINK, REMOVE LINK, PIN NOTE, FILTER by time/tier/POV.

### 6.4 Warrant Builder
- Template fields: Location, PC summary, Linked Items, Requested Actions.
- Live WS readout; reasons for failure listed.
- **SUBMIT** → status Submitted; mock judge delay 10–30 s; result Approved/Denied with rationale.

### 6.5 Map
- Shows lockers, TAPLINE nodes, last photo locations.
- Breadcrumbs for Clara path if enabled by difficulty.

### 6.6 Contacts
- Judges, supervisors, dispatch.
- Actions: request sign‑off for CoC remediation; log responses.

## **7) Items, Props, and World Hooks**
- Evidence Bag pickup increases bag capacity.
- Label Printer prop enables tagging without pre‑prints.
- Evidence Locker actor with slots; enforces `stored=true` and transfers handler to system.

## **8) Error Handling & Edge Cases**
- Duplicate ID: auto‑increment suffix `_B`; toast + edit option.
- Photo lost/corrupt: item remains usable but `ChainBonus −5` and banner shown.
- Seal broken after log: apply `ContamPenalty −10` and set `resealed=true` if resealed.
- Offline logging: cache ops; show **SYNC PENDING**; retries on next session.
- Bag shortage: allow **Collected** but not **Bagged/Tagged**; Q max capped at 55.

## **9) Performance & Storage**
- Max photos per mission: 60; image size target ≤ 200 KB each (JPEG Q80).
- Evidence items per mission target: 20–30 total; A‑tier ≤ 6.
- FieldPad memory bar shows storage; archive oldest photos first after confirm.

## **10) Accessibility & Localization**
- Device skins: Green/Amber/Gray; contrast pairs per SEC‑08.
- Minimum device font size equivalent ≥ 12 px @1080p; scalable.
- Avoid jargon; all UI strings in table with ≤14 char labels; provide short/long forms.

## **11) Telemetry (SEC‑13 parity)**

### Events
- `evidence_logged(case_id,item_id,tier,Q,time)`
- `warrant_submit(case_id,WS,pass_bool)`
- `chain_break(case_id,item_id,when)`
- `link_add/remove(case_id,src,dst)`
- `affidavit_edit(case_id,len,sections_filled)`

### KPIs
- Pre‑action evidence logged ≥70% (Avery arcs).
- Avg WS on first submit ≥55 by EA, ≥65 by Beta.
- Prompt misuse <5%.

## **12) Save/Load Contracts**
- **Slots**: 3 manual + autos.
- **Persist**: EvidenceItem structs, Casefile, Warrant, map breadcrumbs, locker state, pending sync queue.
- **Integrity**: checksum; schema version `evidence_schema_ver`.

## **13) Testing — Acceptance**
- **Functional**: complete CoC, link items, build warrant with WS≥60, approve/deny branches.
- **Negative**: break seal before log; attempt warrant with Q<60; offline log then quit; duplicate IDs.
- **Perf**: capture list open with 30 items < 150 ms; photo capture to view < 300 ms.
- **Localization**: truncation audit for 7–14 char labels.

## **14) Risks & Mitigations**
- **UI overload** → progressive disclosure; tutorial tips; limit on‑screen text.
- **Grind/Spam** → cap A‑tier, boost crosslink value, make optional C‑tier low friction.
- **Legal confusion** → simple WS meter and clear reasons; tie outcomes to narrative, not fail states.

## **15) Deliverables**
JSON schemas, BP/C++ API stubs, widget wireframes (SEC‑07), test plan, tuning table for Q/WS weights, data contract docs.

## **16) Approvals**
On approval: archive as `[TDD‑EVIDENCE+FIELDPAD] v0.1`, export DOCX (full + subsections), link from SEC‑05 §5.7/5.9 and SEC‑07 §7.4.1.

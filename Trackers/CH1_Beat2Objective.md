# CH1 — “Simple Curiosity” Beat→Objective
Version: v0.1
Date: 2025-08-14 11:49Z
Owner: Nick Goldman

Canon: 1994, Brightstar Daycare (Jackson, SC). Strict POV. **Clara:** MEDSTAT (+ note‑card unlocks Notes mid‑chapter). **Avery:** analog tools only.

## Leg A — Clara + Reddy (day → dusk)
### Flow
1) Intake desk sign‑in → supply drawer → **MEDSTAT note‑card** found → insert → **Notes unlocked** (auto‑logs prior pin note).  
2) Guided tour (classroom → infirmary → storage).  
3) Light **stealth** to avoid staffer; optional **care task** for a child.  
4) Exit prompt; schedule return.

### Beats → Objectives
| Beat | Objective | Success | Failure | Notes |
|---|---|---|---|---|
| Sign‑in | **SIGN IN** | Entry logged | Skip desk | Paper ledger |
| Find card | **FIND CARD** | Card in hand | Missed | Drawer hotspot |
| Insert card | **INSERT** | Notes enabled | Wrong slot | Toast: Note logged |
| Tour | **FOLLOW** | Rooms visited | Wander | Waypoints minimal |
| Stealth | **AVOID** | No confront | Spotted | Soft admonish |
| Care task | **CARE** | Task done | Skipped | Optional |
| Schedule | **CALL** | Date set | None | Landline note |

### Checkpoints
- CP1 Sign‑in done; CP2 Card inserted; CP3 Tour done; CP4 Stealth pass; CP5 Exit.

### Telemetry
- `medstat_upgrade_card_found`, `medstat_upgrade_card_inserted`, `pin_auto_log_created`  
- `stealth_pass_bool`, `care_task_done_bool`, `ch1_clara_complete`

### AX/UX
- Prompts ≤14 chars (SIGN IN, FIND CARD, INSERT, FOLLOW, AVOID, CARE, CALL).  
- Subtitles ON; high‑contrast skin toggle persists.

---

## Leg B — Avery (same day)
### Flow
1) Brief with deputy.  
2) **ROE field stop:** **challenge → cuff → search** a belligerent adult.  
3) Analog custody: **photo → bag → tag → log**; mobile locker case handoff.  
4) Debrief scorecard.

### Beats → Objectives
| Beat | Objective | Success | Failure | Notes |
|---|---|---|---|---|
| Brief | **BRIEF** | Goal clear | Skipped | VO line gated |
| Challenge | **CHALLENGE** | Hands up | Premature shot | Admonish |
| Cuff | **CUFF** | Secured | Flee | Re‑engage |
| Search | **SEARCH** | Contraband | Miss 2x | Hint |
| Photo | **CAMERA** | Saved frame | Wrong | 35mm counter |
| Bag/Tag/Log | **BAG/TAG/LOG** | Checklist ✔ | Missing step | Paper forms |
| Handoff | **LOCKER** | Accepted | Queue | Mobile case |
| Debrief | **REPORT** | Score shown | Skip | Score stored |

### Checkpoints
- CP1 Brief done; CP2 Arrest; CP3 Custody; CP4 Debrief.

### Telemetry
- `ch1_avery_complete`, `arrest_performed`, `custody_complete`, `roe_violations`, `range_score` (if referenced), `debrief_viewed`

### AX/UX
- Prompts ≤14 chars. Hold↔press works. Subtitles ON. High‑contrast prompts.

---

## Gates & Outcomes
- Clara wrap requires: `medstat_upgrade_card_inserted==true`; stealth pass not hard‑gated.  
- Avery wrap requires: `custody_complete==true`.  
- Save flags: `medstat_upgrade_card_found=true`, CaseNote created for SYM‑001 on insert.

## Perf spots (initial)
- Intake desk, classroom door, storage hallway; exterior exit.  
- Roadside stop, custody handoff.

## Evidence & Capture
- Screenshots: Notes unlock toast, custody checklist.  
- CSV: perf med/95p at perf spots.

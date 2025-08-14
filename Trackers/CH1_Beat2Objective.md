# CH1 — “Simple Curiosity” Beat→Objective
Version: v0.2
Date: 2025-08-14 23:10:43 UTC
Owner: Nick Goldman

Canon: 1994, Brightstar Daycare (Jackson, SC). Strict POV. **Clara:** MEDSTAT (+ note‑card unlocks Notes mid‑chapter). **Avery:** analog tools only.

## Leg A — Clara + Reddy (day → dusk)
### Flow
1) Intake desk sign‑in → supply drawer → **MEDSTAT note‑card** found → **insert PCMCIA card** → **Notes unlocked** (auto‑logs prior pin note).  
2) Guided tour (classroom → infirmary → storage).  
3) Light **stealth** to avoid staffer; overhear “the stars are right tonight”; optional **care task** for a child.  
4) Exit prompt; schedule return.

### Beats → Objectives
| Beat | Objective | Success | Failure | Notes |
|---|---|---|---|---|
| Sign‑in | **SIGN IN** | Entry logged | Skip desk | Paper ledger |
| Find card | **FIND CARD** | Card in hand | Missed | Drawer hotspot |
| Insert card | **INSERT** | Notes enabled (PCMCIA Type II) | Wrong slot | Toast: Note logged |
| Tour | **FOLLOW** | Rooms visited | Wander | Waypoints minimal |
| Stealth | **AVOID** | No confront | Spotted | Soft admonish |
| Care task | **CARE** | Task done | Skipped | Optional |
| Schedule | **CALL** | Date set | None | Landline note |

### Telemetry
- `medstat_upgrade_card_found`, `medstat_upgrade_card_inserted`, `pin_auto_log_created`  
- `coded_phrase_heard` ("the stars are right tonight")  
- `stealth_pass_bool`, `care_task_done_bool`, `ch1_clara_complete`

## Leg B — Avery (same day)
### Flow
1) Brief with deputy (**name randomized per save**).  
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

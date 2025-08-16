# CH2 Patch — DIPLOMAGIC

## Title
**Chapter 2: Passing Interest**

## Canon Summary
- Clara: survive with Reddy using stealth and martial arts; optional Rolodex call to parents; manage Reddy’s needs.
- Avery: promoted after Gromley; clearance LEVEL_X; meets Lewis Krill; tension between lawful process and extrajudicial force.

## Beat Sheet
### Clara — Survival Loop
1. **Safe Harbor** → `SAFE_HARBOR=TRUE`
2. **Resource Hunt** → `CLARA_RESOURCE_COUNT++`
3. **Rolodex Rescue** (optional) → `ROLODEX_CALL=TRUE` (score bonus)
4. **Manage Reddy** → maintain `REDDY_STATS_OK`

### Avery — Case Before Kicks
1. **Debrief** → `SECURITY_CLEARANCE=LEVEL_X`
2. **Krill Encounter** → `KRILL_CONTACT=TRUE`
3. **Chain of Custody** → `EVIDENCE_CHAIN=TRUE`
4. **Next Node** → `LEAD_NODE ∈ {SAFEHOUSE, ACCOUNTING, RAIL_DEPOT}`

## Gates & Outcomes
- Entry: `CH1_COMPLETE==TRUE`
- Completion: `CH2_COMPLETE==TRUE` when `SAFE_HARBOR==TRUE` and `LEAD_NODE` set with `SECURITY_CLEARANCE==LEVEL_X`

## Compliance Hooks
- **CH6 raid rules**: follow `Rules/CH6-raid-rules.md` ROE and non‑lethal preference for any retroactive references to CH6.
- **CH7 city rules**: friendly/civilian hits are strictly non‑lethal; reference `Trackers/CH7-city-rules.md`.
- **Evidence caps**: enforce caps in `Trackers/EVIDENCE-caps.md` when logging or spending evidence.

## Scoring (TBD thresholds)
- Arrest bonus, lethal penalty, custody bonus, Rolodex bonus, Reddy care bonus.

## Validation Invariants
- `CH2_ACTIVE ⇒ CH1_COMPLETE`
- Enums single‑valued; score deltas posted once on completion.

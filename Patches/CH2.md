# CH2 Patch — DIPLOMAGIC

## Title
**Chapter 2: Passing Interest**

## Canon Summary (from Outline)
- Clara: Survive with Reddy in liminal backwoods between Kids Kamp and reality. Must use stealth and martial arts. Optional Rolodex call to parents adds score bonus. Must manage Reddy’s stat lines for points.
- Avery: Promoted after taking down Langston Gromley. Security clearance upgraded to LEVEL X. Meets Lewis Krill. Tempted toward extrajudicial methods, foreshadowing darker choices later.

## Beat Sheet
### Clara — Survival Loop
1. **Safe Harbor** — Establish temporary haven. Set `SAFE_HARBOR=TRUE`.
2. **Resource Hunt** — Stealth martial arts recovery of food/items. Updates `CLARA_RESOURCE_COUNT`.
3. **Rolodex Rescue** — Optional call to parents. Sets `ROLODEX_CALL=TRUE` and awards bonus points.
4. **Manage Reddy** — Keep REDDY’s hunger/rest satisfied. Affects `FINAL_SCORE`.

### Avery — Clearance Upgrade
1. **Debrief** — Interrogation after CH1. Upgrade: `SECURITY_CLEARANCE=LEVEL_X`.
2. **Krill Encounter** — New mentor pushes for “do whatever necessary” methods. Logs `KRILL_CONTACT=TRUE`.
3. **Archive Review** — Gain access to Walter Phillips classified file. Sets `ARCHIVE_ACCESS=TRUE`.
4. **Path Divergence** — Player influenced toward arrest-first vs lethal-first approaches.

## Gates & Outcomes
- Entry: `CH1_COMPLETE==TRUE`.
- Completion: `CH2_COMPLETE==TRUE` requires `SAFE_HARBOR==TRUE` and `SECURITY_CLEARANCE==LEVEL_X`.
- Clara: Rolodex call optional but boosts final score.
- Avery: Player choice on methods influences alignment.

## Implementation Notes
- Tools: payphones, Rolodex, fax, pagers. 1994 tech only.
- Emphasis: survival for Clara, legal/ethical temptation for Avery.

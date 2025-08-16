# CH1 Patch — DIPLOMAGIC

## Title
**Chapter 1: Simple Curiosity**

## Canon Summary
- **Antagonist:** Langston Gromley, ex-FBI, regional cult head (Massapequa Park, NY).
- **Clara thread:** Escape with Reddy from Massapequa Kids Kamp into the liminal forest of New Kadath. Stealth and melee emphasized. Excess noise wakes Reddy and draws cultists.
- **Avery thread:** Infiltrate Massapequa Park to investigate Gromley. Player may go undercover or use force. Arrests raise Avery’s Final Score; kills penalize him. Limited 9mm ammo. Cultist weapons are unreliable.
- **Outcome:** Resolve both threads; Gromley is either **arrested**, **killed**, or **escapes**.

## Beat Sheet
### A) Clara — “Clara Escapes”
1. **Breakout** — Tutorial refresh on stealth, melee, carry/put-down Reddy.
2. **Noise Management** — Track `CLARA_NOISE_LEVEL`; if high, set `REDDY_CRYING=TRUE` and spawn pursuit squads.
3. **Forest Traverse** — Route choice: quiet trails vs faster risky paths.
4. **Extraction** — Reach forest edge safe node; set `CLARA_EXITED=TRUE`.

### B) Avery — “Avery Infiltrates”
1. **Approach Vector** — Choose **Undercover** or **Warranted Force** entry.
2. **Evidence Pass** — Optional intel pickups for later chapters; increment `EVIDENCE_COUNT`.
3. **Arrest vs Kill Economy** — Arrests increment `AVERY_ARRESTS`; lethal force increments `AVERY_KILLS` and applies score penalty.
4. **Confront Gromley** — Set one terminal status: `GROMLEY_STATUS ∈ {ARRESTED, KILLED, ESCAPED}`.

## Gates & Outcomes
- Enter CH1 only if `PROLOGUE_COMPLETE==TRUE`.
- `CH1_COMPLETE==TRUE` when `CLARA_EXITED==TRUE` **and** `GROMLEY_STATUS` is terminal.
- Hooks forward:
  - High `AVERY_ARRESTS` and low `AVERY_KILLS` boost Avery’s path score.
  - High noise or repeated `REDDY_CRYING` reduces Clara’s path score.
  - `EVIDENCE_COUNT` provides small global score bonus.

## Implementation Notes
- Period accuracy: 1994 tech behavior, unreliable cultist firearms, limited magazines.
- Do not add new mechanics beyond tutorialized stealth/melee/arrest flows.
- All outcomes must write a single `EPILOGUE`-compatible score delta only after CH1 completes.

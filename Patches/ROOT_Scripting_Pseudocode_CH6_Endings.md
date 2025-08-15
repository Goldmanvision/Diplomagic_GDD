# ROOT — Scripting Pseudocode: CH6 Endings
Repo dir: /Patches

Constraints: 1994 lock; prompts ≤14; ambient phrase only.

```pseudo
vars:
  EvidenceCount = 0..3
  BlueOnBlue = 0/1
  Ending = None  # Contain / Sever / BlackFile
  Score = 0
  Rep = 0

# friendly fire
on DamageApplied(attacker in Party, target in Party):
  if target.ShieldAbsorb == true: return
  if weapon == Shotgun and distance > 10m and pellet_count_to_target == 1:
    return  # exception
  BlueOnBlue = 1
  fail_chapter(-10)

# evidence intake (cap)
on EvidenceCollected(item):
  if EvidenceCount >= 3: show("Cap Reached"); return
  EvidenceCount += 1
  Score += 2

# CONTAIN
if WardsJammed == true and Valves == [A,B,C] and Gimbal == STABLE:
  Ending = "Contain"; Score += 5; exfil()

# SEVER
if ChargesPlanted == 2 and ChantInterrupted == true and Detonated == true:
  Ending = "Sever"; Score += 3; exfil()

# BLACK FILE
if Photos >=2 and Samples >=1 and exfil == true:
  Ending = "BlackFile"; Score += 5; Rep -= 5

# end guard
if BlueOnBlue == 1:
  Ending = None  # forced fail handled above

save_flags(Ending, EvidenceCount, BlueOnBlue, Score, Rep)
```

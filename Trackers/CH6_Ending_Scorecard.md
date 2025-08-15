# Tracker — CH6 Ending Scorecard
Repo dir: /Trackers

| Field | Value |
|---|---|
| Ending | Contain / Sever / Black File |
| EvidenceCount | 0–3 |
| EndingBonus | +5 / +3 / (+5 evidence, −5 rep) |
| BlueOnBlue | 0/1 (fail if 1) |
| FinalScoreDelta | compute from EvidenceCount + EndingBonus |

## Compute
```
if BlueOnBlue==1: FinalScoreDelta = "FAIL"
else:
  if Ending=="Contain": base=5
  elif Ending=="Sever": base=3
  elif Ending=="Black File": base=0  # evidence handled separately, rep penalty external
  FinalScoreDelta = base + (EvidenceCount*2)
```

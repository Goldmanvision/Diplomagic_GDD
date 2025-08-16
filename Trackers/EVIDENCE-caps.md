# Evidence Caps — CH6 and CH7

Purpose: bound evidence accumulation and ensure predictable scoring and progression.

## Global
- `EVIDENCE_CAP_GLOBAL = 12` across CH6–CH7

## CH6
- `EVIDENCE_CAP_CH6_RAID = 6`
- Required distribution:
  - 2× physical artifacts (bagged, labeled)
  - 2× photos (dated, signed)
  - 2× affidavits/notes (signed)

Validation:
- CI warns if > `EVIDENCE_CAP_CH6_RAID` logged.

## CH7
- `EVIDENCE_CAP_CH7_CITY = 4`
- Required distribution:
  - 2× civilian reports
  - 1× officer report
  - 1× photo

Validation:
- CI warns if > `EVIDENCE_CAP_CH7_CITY` or any civilian/friendly injury is logged as lethal (forbidden by city rules).

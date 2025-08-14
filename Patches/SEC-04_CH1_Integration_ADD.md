# SEC-04 — CH1 Integration ADD
Version: v0.1
Date: 2025-08-14 12:15Z
Owner: Nick Goldman

Paste under Core Loops as new subheading.

## 4.Y Chapter 1 Integration (Clara/Avery)

**IDs**
- Clara: OBJ-CH1-CLA-SIGNIN, -FINDCARD, -INSERT, -FOLLOW, -AVOID, -CARE, -CALL
- Avery: OBJ-CH1-AV-BRIEF, -CHALLENGE, -CUFF, -SEARCH, -CAMERA, -CUSTODY, -LOCKER, -REPORT

**Loop mapping**
| Loop | Step | IDs | Gate | Output |
|---|---|---|---|---|
| Investigate→Act→Record | Clara Notes unlock | OBJ-CH1-CLA-INSERT | Card inserted | `pin_auto_log_created` |
| Stealth | Clara avoid staff | OBJ-CH1-CLA-AVOID | none | `stealth_pass_bool` |
| Caregiving | Clara care task | OBJ-CH1-CLA-CARE | none | `care_task_done_bool` |
| Investigate→Act→Record | Avery custody | OBJ-CH1-AV-CUSTODY | Locker confirm | `custody_complete=true` |
| Arrest loop | Avery stop | OBJ-CH1-AV-CHALLENGE/CUFF/SEARCH | `shots_on_compliant==0` | `arrest_performed` |

**Wrap gates**
- Clara: `medstat_upgrade_card_inserted==true`.
- Avery: `custody_complete==true`.

**Telemetry**
Per `Trackers/QATelemetry_CH1.md`.

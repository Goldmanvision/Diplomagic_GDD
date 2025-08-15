# Tracker — QA Test Cases (CH5–CH6)
Repo dir: /Trackers

| ID | Area | Pre | Steps | Expected |
|---|---|---|---|---|
| TC-01 | ROE | CH6 start | Shoot friendly once | Fail; BlueOnBlue set |
| TC-02 | ROE | CH6 start | Hit friendly Shield | No fail; log only |
| TC-03 | ROE | Shotgun | One pellet >10 m hits friendly | No fail; single pellet ignore |
| TC-04 | Evidence | Vault | Collect 4th item | “Cap Reached”; score unchanged |
| TC-05 | Contain | Core | Jam wards; A→B→C | Ending=Contain; +5 |
| TC-06 | Sever | Core | Plant×2; interrupt; detonate | Ending=Sever; +3 |
| TC-07 | BlackFile | Vault | Photo×2; Sample×1; exfil | Ending=Black File; +5; rep −5 |
| TC-08 | UI | Any | Check all prompts | All ≤14 chars |
| TC-09 | Period | Any | Search tech strings | No smartphone/Wi‑Fi/Bluetooth/GPS/SMS/StarTAC |
| TC-10 | Spawn | Vault | Ammo <25% | Next spawn −20% chance |
| TC-11 | Cameras | Passage | Pull fuse | 90 s outage; K‑9 swap |
| TC-12 | Gaunt | Bright area | Light it | Grounded 1.5 s + icon |
| TC-13 | Map | Annex | Compare names to ASCII | Names match |
| TC-14 | Comms | Rogue | Pager→Payphone 90 s | Works; timed |

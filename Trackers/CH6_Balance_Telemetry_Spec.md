# Tracker — CH6 Balance Telemetry Spec
Repo dir: /Trackers

## Event schema (CSV or JSON lines)
- `timestamp` (ms)
- `save_seed` (int)
- `deputy_name` (string)
- `area` (enum: Passage/ValveRow/DeadPiping/Core/Vault/Egress)
- `event` (enum: BreakerPull/ValveTurn/Plant/Detonate/ChantInterrupt/Photo/Sample/BlueOnBlue/Death/End_Contain/End_Sever/End_BlackFile)
- `ammo_pistol` `ammo_shotgun` `ammo_rifle` (ints)
- `tonic_used` (int cumulative)
- `mana` (0–100)
- `evidence_count` (0–3)
- `friendly_hit` (bool)
- `light_stagger` (bool for gaunt interactions)
- `score_delta` (int running)
- `rep_delta` (int running)

## Sampling
- Log on every loop action and on timers: 10 s while in Vault.

## Output
- Store to local file for playtest; no network I/O (1994 constraint is narrative; tooling is modern).

## Reports
- Use `/Trackers/ROOT_Metrics_Snapshot_Template.md` for standups.

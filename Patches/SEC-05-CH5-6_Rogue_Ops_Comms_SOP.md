# SEC-05 — Rogue Ops Comms SOP (CH5→CH6)
Repo dir: /Patches

## Posture
- `F_Rogue=1`: limited FBI access. Krill is sole handler.
- Devices: **pager** + **payphone** only. No SENTINEL outside NYFO.

## Cadence
- **Check window:** :00, :20, :40 each hour (±5 min). Miss → next window.
- **Burst page codes (1994):**
  - 911 = contact now
  - 77 = abort route
  - 23 = reroute to Safe Node
  - 19 = evidence upload at next NYFO
- **Phrase lock:** ambient only — “the stars are right tonight.”

## Payphone Nodes
- NYC hotel lobby, Midtown corner booth, D‑LAMP island kiosk call box, SRS outer road diner.
- Calls ≤90 s to reduce trace risk.

## Fail states
- Miss 3 windows → `F_HandlerLost=1` (no tips).
- Stuck trace detected → cut call, relocate, wait one window.

## UI prompts (≤14)
Pager, Payphone, Call Back, Abort, Reroute, Upload

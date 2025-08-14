# Devices — Storage & Networking (1994 Audit)
Version: v0.1
Date: 2025-08-14 21:08:41 UTC
Owner: Nick Goldman

## Standards
- **PCMCIA Type II (68‑pin, 5V linear flash)** — primary “note‑card” medium; **Newton‑compatible** software card format.
- **CompactFlash Type I (50‑pin)** — optional via PCMCIA‑CF adapter for FieldPad/TAPLINE variants.

## Device matrix
| Device | Slot | Media | Purpose | Net stack |
|---|---|---|---|---|
| MEDSTAT | PCMCIA Type II | Linear flash card | Unlock **Notes**; read‑only pin CaseNote on CH1 insert | **SENTINEL** sat link to other MEDSTATs; no internet |
| FieldPad | PCMCIA Type II + CF via adapter | Linear flash / CF | Later chapters: apps, storage | Local only until later sync |
| TAPLINE | PCMCIA Type II | Linear flash | RF tools (scan/record), no internet | N/A |

## Constraints
- No general internet. No camera on MEDSTAT. Notes only.
- **SENTINEL**: store‑and‑forward to **linked MEDSTATs**; limited GPS‑style breadcrumb for patient bands.

## Legal
- Ship without real trademarks; use generic “Note‑Card” labeling.

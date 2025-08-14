# Inline Patch — SEC-05 Systems: Prologue Flags & Data
Version: v0.1 — 2025-08-14 10:57:09 UTC
Owner: Nick Goldman
Paste into SEC-05 under Save/Data Schemas and Systems Flags.

---
## BEGIN PATCH: SEC-05 — Prologue Flags & Data

### Save keys (player profile)
```json
{
  "prologue_flags": {
    "hauser_pistol_awarded": false,
    "brightstar_pin_found": false,
    "cult_symbol_link_active": false,
    "nonlethal_ammo_trained": false,
    "nonlethal_takedown_done": false,
    "escort_done": false
  },
  "range_score": 0,
  "roe_violations": 0,
  "medstat_upgrade_card_found": false
}
```

### Derived linkage
```pseudo
cult_symbol_link_active = hauser_pistol_awarded && brightstar_pin_found
```

### Notes vs Evidence
- 0B pin is **observed only** in Prologue; no EvidenceItem yet.
- After `medstat_upgrade_card_found == true` (CH1), create a **CaseNote** (non‑warrant) with `symbol_id:"SYM-001"` and text “Symbol seen on Betsy’s pin (matches SYM-001)”.

### Award rule (Hauser pistol)
- Unlock when `range_score ≥ 90 && roe_violations == 0` at 0A debrief; set `hauser_pistol_awarded=true`. Grant item later via inventory rules.

### Telemetry
Mirror QATelemetry events; persist above booleans. Bump minor save schema version.

## END PATCH

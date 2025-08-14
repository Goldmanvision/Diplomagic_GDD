# Propagation — SEC-05 Systems: Prologues Flags & Data
Version: v0.1
Date: 2025-08-14 10:49:18 UTC
Owner: Nick Goldman
Scope: Add data keys and flows for Prologue outcomes.

## Save keys (player profile)
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

## Derived linkage
On load or state change:
```pseudo
cult_symbol_link_active = hauser_pistol_awarded && brightstar_pin_found
```

## Symbol registry (lore; non-warrant)
```json
{
  "symbols": [{"id":"SYM-001","name":"Brightstar Sigil","tex":"Art/Symbols/sym001.png"}]
}
```

## Notes vs Evidence
- 0B pin is **observed only** in Prologue. No EvidenceItem yet.
- After `medstat_upgrade_card_found==true` (CH1), create a **CaseNote**, not EvidenceItem.

### CaseNote schema
```json
{
  "id": "N-0001",
  "case_id": "BRIGHTSTAR",
  "source": "paper_chart",
  "text": "Symbol seen on Betsy’s pin (matches SYM-001)",
  "symbol_id": "SYM-001",
  "created_from": "prologue_0b"
}
```

- CaseNotes do not contribute to Warrant Score. They unlock UI lore and filtering.

## Award rule (Hauser pistol)
- Unlock if `range_score≥90 && roe_violations==0` at 0A debrief.
- Set `hauser_pistol_awarded=true`. Grant item in later chapters per inventory rules.

## Telemetry keys
Mirror QATelemetry events. Persist booleans above. Version bump minor for save schema.

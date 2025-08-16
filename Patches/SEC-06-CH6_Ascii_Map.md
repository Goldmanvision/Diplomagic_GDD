# SEC-06-CH6_Ascii_Map.md
> SRS operation layout for Chapter 6. Cameras only in Service Passage. Vault has **no CCTV**.\n
```
                       NORTH
        ┌──────────────────────────────────────────┐
        │   DELIVERY YARD                         │
        │   [Parking][Trunk][Radio]               │
        └───────┬───────────────────────┬─────────┘
                │                       │
        ┌───────▼───────────┐   ┌───────▼───────────┐
        │  SERVICE PASSAGE  │   │     ADMIN WING    │
        │  [CCTV ZONE]      │   │  Offices, Breakr │
        │  [Photo/Sample]   │   │  Breaker Panel ◻ │
        │  K‑9 Route ⇄      │   │                   │
        └───┬─────────┬─────┘   └─────────┬────────┘
            │         │                   │
            │   ┌─────▼─────┐       ┌────▼─────┐
            │   │ REACTOR A │       │ REACTOR B│
            │   │ Valve A ● │       │ Valve B ●│
            │   │ Ward ◇    │       │ Ward ◇   │
            │   └─────┬─────┘       └────┬─────┘
            │         │                   │
        ┌───▼─────────▼──────┐      ┌────▼───────────┐
        │  CONNECTOR TUNNEL  │      │  REACTOR C     │
        │  Breach ✚  Jammer  │      │  Valve C ●     │
        └───┬────────────────┘      │  Ward ◇        │
            │                       └────┬───────────┘
            │                            │
        ┌───▼────────────────────────────▼───┐
        │               VAULT                 │
        │   [NO CCTV]   Core ◯   Device ▣    │
        │   Photo: ✖    Sample: ✔            │
        │   Escape Route ⇒ Collapsing Corr.  │
        └────────────────────────────────────┘

Legend:
● Valve A/B/C      ◻ Breaker (≈90 s)    ◇ Ward Node
✚ Breach Point     ▣ Device             ◯ Core
✔ Allowed          ✖ Not allowed        ⇄ K‑9 reroute path
```

## Notes
- Cameras exist only in **Service Passage**. Photography restricted there.
- Breaker recycle ≈ **90 s**. Staged restore at 30/60/90 s.
- K‑9 reroute via handler diversion or scent decoy along marked path.
- Vault enforces **no photography**; rely on samples/logs.

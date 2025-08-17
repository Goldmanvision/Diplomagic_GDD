---
Title: Depot & Branch Map
Department: Steam Operations
Codename: Stationmaster
Owner: Stationmaster
Reviewer: Postmaster
Date: 2025-08-17
Type: Ops Map
Status: Draft
---


## Revision — 2025-08-17
**OS Targets (Plan A):** Windows 10/11 x64. Steam Deck via Proton.  
Linux/macOS deferred until post-freeze.

### Depots (launch)
| DepotID | OS/Type   | Content                      | Notes           |
|--------:|-----------|------------------------------|-----------------|
| TBA001  | windows   | base game + content          | launch          |
| TBA100  | lang-pack | localized text/vo assets     | optional        |
| TBA900  | tools     | dedicated server/tools       | optional        |

### Branches
- public, default, beta, preview, dev (unchanged)
- Add **proton-qa** tag on beta builds for Deck validation.

### Actions
- Confirm Proton QA matrix and controller glyphs.
- Remove non-Windows depots from initial CI upload.

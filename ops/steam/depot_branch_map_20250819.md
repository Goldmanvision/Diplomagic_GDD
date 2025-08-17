---
Department: Steam Operations
Codename: Stationmaster
Date: 2025-08-17
Status: Active
---

## Plan A Confirmation — 2025-08-17
- OS targets: Windows 10/11 x64. Steam Deck via Proton.
- Tags: add `proton-qa` to beta branch.

### Branches
| Branch | Purpose | Notes |
|---|---|---|
| main | release‑ready | CI build; content lock near freeze |
| beta | public test | tagged `proton-qa` when Deck testable |
| dev | internal | daily integration |
| review | marketing/review | content‑locked snapshots |

### Depots
| Depot ID | Platform | Content | Notes |
|---|---|---|---|
| TBD-AppID | Windows x64 | binaries + content | compile with `/MD` runtime, x64 |
| TBD-Data  | cross‑platform | content only | shared assets |

### Packaging
- Use LFS or split archives for assets if size requires.
- Confirm runtime redistributables bundled or Steamworks redist set.

### Sign‑off
Owner (Stationmaster): ___  Postmaster: ___  Date: ___


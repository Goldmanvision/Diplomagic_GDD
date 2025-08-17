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

# Scope
Define initial depots, packages, and branch strategy for build intake and publishing.

# App
- AppID: TBA
- Name: DIPLOMAGIC

# Depots (initial)
| DepotID | OS/Type   | Content                          | Notes |
|--------:|-----------|----------------------------------|-------|
| TBA001  | windows   | base game binaries + content     | default |
| TBA002  | linux     | base game binaries + content     | if supported |
| TBA003  | macos     | base game binaries + content     | if supported |
| TBA100  | lang-pack | localized text/vo assets         | optional |
| TBA900  | tools     | dedicated server/tools           | optional |

# Packages
- Default package: includes TBA001 (+ TBA002/TBA003 if supported)
- Internal test package: includes all depots; not visible
- Promo keys package: default package

# Branches
| Branch    | Purpose                 | Visibility |
|-----------|-------------------------|------------|
| public    | live to customers       | public     |
| default   | same as public          | hidden     |
| beta      | opt‑in testing          | public     |
| preview   | partner QA              | limited    |
| dev       | internal only           | hidden     |

# Build intake
- Artifact: zipped per depot (no spaces; ASCII-safe).
- Versioning: YYYY.MM.DD.build
- Upload: SteamPipe via CI or SteamCMD
- Release notes: /ops/steam/release-notes-YYYYMMDD.md

# Compliance
- Executable names ASCII-safe.
- No sensitive data in depots.
- Include EULA if required.

# Risks
- OS support matrix undecided.
- Language pack structure TBA.

# Actions
1) Confirm OS targets.  
2) Finalize depot IDs.  
3) Wire CI upload script.  

# Gate check
- G1 Metadata: PASS
- G2 ASCII-safe path/name: PASS
- G3 Scope/Deps: PASS
- G4 Blockers: PENDING
- G5 Dept content: PASS
- G6 Sign-offs: PENDING

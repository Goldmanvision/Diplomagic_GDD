---
Title: Steam Store Asset Checklist — Plan A
Department: Steam Operations
Codename: Stationmaster
Owner: Stationmaster
Reviewer: Postmaster
Date: 2025-08-17
Status: Draft
---

# Targets
- OS: Windows 10/11 x64
- Steam Deck: Proton (QA on beta branch with `proton-qa` tag)
- Linux/macOS: deferred until post-freeze

# Asset spec matrix (confirm sizes in Steamworks before export)
| Asset                          | Required | Target Size (CONFIRM) | Crop/Notes                                  | Owner | Status |
|--------------------------------|:-------:|-----------------------|---------------------------------------------|:-----:|:------:|
| Store capsule — main           |   Y     | TBC                   | No text near edges; safe title area         | Art   |   ☐    |
| Store capsule — small          |   Y     | TBC                   | Legible at small scale                      | Art   |   ☐    |
| Store capsule — micro          |   Y     | TBC                   | High contrast                               | Art   |   ☐    |
| Library hero (store header)    |   Y     | TBC                   | Pan-safe top/bottom; no UI-critical text    | Art   |   ☐    |
| Library logo                   |   Y     | TBC                   | Transparent PNG; centered silhouette        | Art   |   ☐    |
| Library capsule                |   Y     | TBC                   | Matches main capsule design                 | Art   |   ☐    |
| Screenshots (min 5)            |   Y     | 1920×1080+            | No debug UI; 1994/1989 accuracy             | Dev   |   ☐    |
| Trailer (optional early)       |   N     | 1080p/4K              | No spoilers; music cleared                  | Mktg  |   ☐    |
| Legal boilerplate              |   Y     | n/a                   | Copyright, trademarks, ratings notes        | Mail  |   ☐    |
| Tags & features list           |   Y     | n/a                   | Justify per Playbook tone                   | Mail  |   ☐    |

# Copy blocks
- Short description: TBC
- Long description: TBC
- Key features: TBC
- Supported input: Keyboard/Mouse; controller; DualSense features on PC (note: verify legal wording).

# Deck verification checks
- Controller glyph set present and consistent.
- Default graphics preset stable on Deck.
- Text legibility at 800p.
- Cloud saves and suspend/resume smoke test.

# Actions
1) Pull official dimensions from Steamworks (confirm all “TBC”).
2) Lock template PSD/PNGs with 3–5% safe margins to avoid auto-crop.
3) Route first pass to Mail for gate checks before upload.

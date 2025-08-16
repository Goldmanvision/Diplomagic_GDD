# [SEC-09-TECH] Technology & Performance Targets
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-07-UI` — UI/UX (Devices, HUD, Menus)
- `SEC-08-ARTAUDIO` — Art Direction & Audio
- `SEC-10-PRODUCTION` — Production Plan & Milestones
- `SEC-11-QA` — QA, Localization, Accessibility

## **9.1 Tech Stack**

* Engine: **Unreal Engine 5.6**.

* RHI: **DX12** on Windows; **Vulkan** optional.

* Middleware: **Wwise** (audio), Niagara (VFX).

* UI: UMG + Slate; bitmap device fonts per SEC‑07.

* Source control: **Perforce** recommended for binary assets; Git acceptable for code/tools if isolated.

* Build automation: Unreal Automation Tool (UAT) + CI runner (local or hosted).

* Scripting: Blueprints for gameplay glue; C++ for systems.

## **9.2 Platforms & Performance Targets**

| Platform | Resolution | FPS Target | Notes |
| ----- | ----- | ----- | ----- |
| PC min‑spec | 1080p | **60** | Low/Medium preset, baked GI, limited volumetrics |
| PC rec‑spec | 1440p | **60** | Medium/High, selective volumetrics |
| PC high‑end | 2160p | **60** | High, optional CRT filter |
| Consoles (post‑launch) | 1080p/1440p | **60** | Parity with PC Medium/High; dynamic res allowed |

## **9.3 Hardware Targets (PC)**

* **Minimum**: 4‑core CPU @3.2 GHz, 16 GB RAM, GPU \~ GTX 1060 / RX 580 (6–8 GB), SSD.

* **Recommended**: 6‑core CPU @3.6+ GHz, 32 GB RAM, GPU \~ RTX 3060 / RX 6700 XT (8–12 GB), SSD.

## **9.4 Rendering Pipeline**

* GI/Lighting: baked where stable; limited dynamic keys for patrols and flicker.

* Shadows: stationary for key lights; virtual shadow maps off on min‑spec.

* Lumen: **off**; Nanite: **off by default** (enable only for hero props if perf allows).

* Post: minimal bloom, low grain, vignette low; chromatic aberration **off**.

* AA: **TSR** default; TAAU fallback for upscaling.

* Fog/Volumetrics: budgeted per SEC‑08.

## **9.5 Performance Budgets (frame)**

* GPU time: **≤ 14 ms** @ 1080p min‑spec.

* CPU game + render: **≤ 16 ms** total @ 1080p.

* Draw calls: **≤ 1,200** interior, **≤ 1,800** exterior.

* Visible triangles: **≤ 0.8 M** interior, **≤ 1.5 M** exterior.

* Shadowed lights: **≤ 2** dynamic key, **≤ 6** stationary total.

* Skeletal meshes active: **≤ 20** interior, **≤ 35** exterior.

* Particles: see SEC‑08 caps (≤512 CPU, ≤20k GPU).

* Audio voices: **≤ 48** concurrent.

## **9.6 Memory & Streaming**

* System RAM: **≤ 8 GB** working set min‑spec.

* VRAM: **≤ 5 GB** min‑spec; **≤ 7 GB** rec.

* Texture streaming pool: **1.5 GB** interior, **2.5 GB** exterior.

* Async loading screens for large layer swaps (Kadath transitions).

* Pak chunking by chapter; shared core pak for devices/UI.

## **9.7 Scalability Presets**

* **Low**: baked GI only, no volumetrics, low post, 0.75 res scale allowed.

* **Medium**: limited volumetrics, medium shadows, SSR off.

* **High**: volumetrics on budget, higher shadow resolution, SSR low.

* **Accessibility**: high‑contrast UI skin, reduced flash, lower camera shake.

## **9.8 Save/Load & Data**

* Format: compressed JSON + binary blobs for maps; slots: **3 manual + autos**.

* Contents: caseboard graph, evidence chain states, heat/reputation, device unlock flags, AI snapshot.

* Integrity: checksum per slot; versioned schema.

## **9.9 Telemetry & QA**

* Telemetry events: evidence logged, arrest/kill outcomes, stealth resolution rate, mission duration, crashes.

* Storage: local JSON logs with opt‑in upload; anonymized session ID.

* Crash handling: UE Crash Reporter; symbols preserved per build.

* KPI gates mirror SEC‑04 and SEC‑05 targets.

## **9.10 Localization & Fonts**

* UE Localization Dashboard; cultures: en‑US base, configurable expansions.

* Device text uses resource keys; font fallbacks per SEC‑08.

* All strings ≤14 chars for device labels; wrap at 24–28 chars.

## **9.11 Accessibility Hooks**

* Global toggles: subtitles on, color‑blind safe palettes, reduced camera shake, reduced flashing, input remap, hold‑to‑press toggle.

* Device skins: Green/Amber/Gray with WCAG pairs per SEC‑08.

## **9.12 Networking & Online**

* Core game is offline.

* Optional telemetry upload and crash reports; no account system.

## **9.13 Mod Support (post‑EA)**

* Expose data tables, device skins, audio cue routing, and simple blueprint actors.

* Load loose content or external pak folder `Mods/`.

* Basic in‑menu mod list with enable/disable; no code plugins.

## **9.14 Source Control & Branching**

* **Perforce** depot layout: `//DIPLOMAGIC/Dev`, `//DIPLOMAGIC/Release`, `//DIPLOMAGIC/ArtDrop`.

* Branch model: main → release branches per milestone; cherry‑pick hotfixes.

* LFS/Git allowed only for tooling docs outside `.uproject`.

## **9.15 Build & Release**

* CI: per‑commit cooks for Windows Dev build; nightly cooked Editorless.

* Milestone builds signed and versioned: `v{MAJOR.MINOR.PATCH}_{YYYY-MM-DD}`.

* Art/audio validation step: reference scanner for textures, triangle budgets, loudness.

## **9.16 Compliance & Legal**

* Ratings targets: ESRB M / PEGI 18 (see SEC‑02).

* Licensing: verify font and SFX licenses per SEC‑08.

* Privacy: plain‑language prompt for telemetry; no PII.

## **9.17 Risks & Mitigations**

* **Perf regressions**: lock budgets; perf CI gate; capture baselines per level.

* **Shader compile hitches**: precompile PSO cache; share DDC.

* **Asset bloat**: enforce naming, LODs, streaming budgets; weekly report.

## **9.18 Deliverables**

* Perf budget worksheet per level.

* CI scripts and UAT configs.

* PSO cache and DDC sharing guide.

* Telemetry schema and dashboard spec.

* Localization glossary and test plan.

## **9.19 Approvals**

On approval: archive to MASTER as `[SEC-09-TECH] v0.1` and update manifest. Next: **SEC‑10 Production Plan & Milestones**.

# **Patch Instructions for Existing MASTER — SEC-10**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-10-PRODUCTION |` and replace the entire line with:

`| SEC-10-PRODUCTION | Production plan | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

### **9.x Device I/O & Storage (1994 constraints)**
- FieldPad storage via **PCMCIA Type‑II ATA/SRAM** or **CF Type‑I** using **CF→PC Card** adapter.
- Practical throughput ≤ 1–2 MB/s; photo write/read operations are slow.
- Photo caps aligned with TDD: ≤ 60 per mission, ~200 KB each.
- Connectors: **RJ‑11** for modem cards, **RJ‑45** for 10Base‑T NICs, optional **RS‑232 DE‑9** on device/dock.

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# SEC-09 — Period Audit (1994) for CH5–CH6
Repo dir: /Patches
Date: 2025-08-15

## Allowed tech (examples)
MicroTAC phones, numeric pagers, payphones, Polaroids, analog CCTV, paper logs, teletype/BOLO/FD‑302.

## Disallowed tech (flag any occurrence)
smartphone, Wi‑Fi, Bluetooth, GPS, SMS, SIM, StarTAC, digital camera, internet upload from field devices.

## Doc targets
- `SEC-03-NARRATIVE - Narrative.md` (CH5, CH6)
- `SEC-05-SYSTEMS - Systems & Mechanics.md`
- `SEC-06-WORLD - World, Levels, & Content.md`
- `SEC-07-UI - UI-UX (Devices, HUD, Menus).md`
- README/ToC
- Patches/Trackers in this PR

## Commands (pick one family)

### ripgrep
```
rg -n "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" -S
```

### grep
```
grep -RniE "StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera" .
```

### PowerShell
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SMS|SIM|digital camera'
```

## Results
| File | Term | Line | Action |
|---|---|---|---|
|  |  |  |  |

## Sign‑off
- Narrative: ______  Date: ____
- Systems:  ______  Date: ____
- QA:       ______  Date: ____

Ambient phrase only: “the stars are right tonight.”

# [SEC-08-ARTAUDIO] Art Direction & Audio
Version: v0.2  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-06-WORLD` — World, Levels, & Content
- `SEC-07-UI` — UI/UX (Devices, HUD, Menus)
- `SEC-09-TECH` — Technology & Performance Targets
- `SEC-10-PRODUCTION` — Production Plan & Milestones

## **8.1 Visual Pillars**

* PS1‑era austerity + modern clarity (fog, lights, post).

* Readable silhouettes first. Texture thrift.

* 1994 authenticity for props, signage, and UI.

## **8.2 Reference Package (deliver to Art Dir.)**

* Mood boards: **Real / New Kadath / Unknown Kadath**.

* Prop sheets: 1994 utilities, payphones, radios, lockers.

* Typeface refs: bitmap device sans, highway/OSHA signage fonts.

* Material library: plastic, painted metal, concrete, paper, glass.

* Lighting refs: sodium vapor, fluorescent, halogen, flashlight cones.

## **8.3 Color Palettes (master)**

**World Core (neutral, low‑sat):**

* **Splinter Black** `#0B0B0E`

* **Fog Gray** `#8D9199`

* **Concrete** `#5E666F`

* **Steel Blue** `#3B5368`

* **Sodium Amber** `#C48A1B`

* **Emergency Red** `#B21E2B`

**Device Skins (SEC‑07 parity):**

* **FieldPad Green** `#1C6B3C`

* **TAPLINE Amber** `#D09A2A`

* **MEDSTAT Gray** `#C7C9CC`

* **CRT Phosphor** `#00C853`

ASCII swatches:

████ Splinter Black #0B0B0E   ████ Fog Gray #8D9199   ████ Concrete #5E666F

████ Steel Blue    #3B5368   ████ Sodium Amber #C48A1B ████ Emergency Red #B21E2B

████ FieldPad Green #1C6B3C  ████ TAPLINE Amber #D09A2A ████ MEDSTAT Gray #C7C9CC

### **8.3.1 Locale Palettes**

| Locale | Primary | Accents | Notes |
| ----- | ----- | ----- | ----- |
| **Real‑Day** | Concrete `#5E666F`, Fog Gray `#8D9199` | Steel Blue `#3B5368`, Sodium Amber `#C48A1B` | Utility, signage pops |
| **Real‑Night** | Splinter Black `#0B0B0E`, Steel Blue `#3B5368` | Emergency Red `#B21E2B`, Sodium Amber `#C48A1B` | Patrol readability |
| **New Kadath** | Steel Blue `#3B5368`, Concrete `#5E666F` | CRT Phosphor `#00C853` | Subtle surreal shift |
| **Unknown Kadath** | Splinter Black `#0B0B0E` | Phosphor `#00C853`, Emergency Red `#B21E2B` | High contrast cues |
| **Industrial/Utilities** | Concrete `#5E666F` | TAPLINE Amber `#D09A2A` | Devices, wiring, meters |

### **8.3.2 Contrast Guidance (WCAG)**

* Target **≥4.5:1** for body, **≥3:1** for large text/icons.

* Approved pairs (AA pass):

  * `#FFFFFF` on `#1C6B3C` (FieldPad),

  * `#0B0B0E` on `#D09A2A` (TAPLINE),

  * `#FFFFFF` on `#3B5368`,

  * `#FFFFFF` on `#5E666F` (large text).

* Do not put `#FFFFFF` on `#C7C9CC` except for large text with stroke.

## **8.4 Modeling & LOD**

* Triangle budgets (target): hero chars **6–10k**, majors **4–6k**, grunts **2–4k**; hero props **1–3k**.

* LODs: LOD0/1/2 at **1.0/0.6/0.35** screen fractions; drop small geo first.

* Prioritize silhouette and normal hints over micro‑detail.

## **8.5 Materials & Shading**

* Few master materials; instance for tint/wear.

* Dithered gradients for 8–16‑bit look; limited roughness range.

* Decals for grime, leaks, signage; avoid high‑freq tiling.

## **8.6 Lighting & Fog**

* Mixed: baked GI where stable, dynamic keys for patrols and flickers.

* Temperature: sodium streets **2000–2200K**, fluorescents **4000–4500K**, halogen **3000K**.

* Volumetrics as gameplay: stealth cover vs readability.

* Kadath layers warp: slight non‑Euclidean offsets, color bleeding, shadow bend.

## **8.7 Post‑Processing**

* Film grain subtle; 90s chroma bleed minimal; CRT scanline option toggle.

* Chromatic aberration off by default.

* Camera shake configurable per Accessibility.

## **8.8 VFX**

* Splinter anomalies: refraction cones, audio‑reactive shimmer, particulate falloff.

* Environmental: steam, fluorescent buzz flicker, dust motes.

* Combat: modest muzzle flash, decal‑light footprints, low‑gore blood with pooling caps.

## **8.9 Animation Style**

* 24 fps keyframed look; occasional pose hold to evoke era.

* Clara cautious weight; Avery authoritative stance.

* Minimal facial rigs; rely on posture and camera.

## **8.10 UI Tie‑ins (from SEC‑07)**

* Two‑tone devices, bitmap type, 320×240 virtual grid.

* HUD minimal; visibility/noise glyphs; hold meters with ticks.

---

## **8.11 Audio Pillars**

* Dread via implication.

* 1994 soundscape: pagers, trunked radios, CRTs, HVAC.

* POV contrast: Avery comms; Clara breath/handling/space.

## **8.12 SFX Taxonomy**

* Movement, devices, world, human, paranormal, weapons.

* Ensure material sets by surface: concrete, dirt, grass, metal, wood, water.

## **8.13 Music Direction**

* Analog synths, tape wow/flutter, bowed metals, sparse piano; low‑drone strings for Splinter.

* Motifs: **Avery** procedural ostinato; **Clara** fragile two‑note rise; **Splinter** inharmonic cluster.

* Stems for **Stealth / Investigate / Combat / Aftermath**.

* Diegetic sources: radios, TVs, PA systems; mild LPF for occlusion.

## **8.14 Implementation (Audio Tech)**

* Middleware: **Wwise** (fallback: UE Audio).

* Mix bus: Master → Music / SFX / VO / UI → sub‑buses.

* RTPCs: Heat, Visibility, Stress, Health, LocationLayer.

* Ducking: Dialogue over SFX by **−6 dB**; UI under VO.

* Reverb zones: tunnels, rooms, Kadath diffuse.

* Loudness: true‑peak ≤ **−1 dBTP**; dialogue ≈ **−18 LUFS** short‑term.

## **8.15 VO & Dialogue — Pipeline**

* **Casting specs:** restrained natural reads; minimal melodrama.

* **Mic chain:** LDC with pop filter → clean preamp → 48 kHz/24‑bit WAV.

* **Session:** one actor per folder; one line per file; 1 s room tone head/tail per scene.

* **File naming:** `vo_<char>_<scene>_<lineID>_take##.wav`.

* **Slate:** soft clap + verbal slate at start of each scene.

* **Processing:** light HPF only; no FX baked.

## **8.16 Audio Deliverables — Spec**

* **Format:** WAV PCM **48 kHz / 24‑bit**.

* **Channels:** SFX mono unless spatial, Music stereo stems, VO mono.

* **Headroom:** peaks ≤ **−3 dBFS**; tails faded.

* **Loops:** seamless, zero‑cross boundaries, 10–50 ms ramps.

* **Naming:**

  * SFX `sfx_<cat>_<object>_<action>_v##.wav`

  * Music `mx_<state>_<cue>_<stem>.wav`

  * UI `ui_<device>_<app>_<action>.wav`

## **8.17 Music Stems Map & Cue Sheet Template**

**Stems per state:**

* *Stealth:* pad, pulse, texture.

* *Investigate:* pad, ticks, motif.

* *Combat:* drums, bass, lead, hits.

* *Aftermath:* drone, piano, noise bed.

Cue Sheet (example):

CUE: M\_CH3\_Tunnels\_Stealth  BPM: 84  Key: Em

Stems: pad, pulse, texture   Loop: 0:45

Enter: Visibility\<0.3 AND Heat\<0.2

Exit: Alert==true OR Combat==true

## **8.18 VFX Performance Caps & LOD**

* **Per‑frame particles (CPU):** ≤ **512** visible.

* **GPU sprites:** ≤ **20k** total; overdraw heatmap checked per milestone.

* **Fog volumes:** ≤ **3** large per level; avg overdraw \< **1.5×**.

* **Niagara LOD:** tick rate scales by distance; collisions off for small sprites.

* **Budget gates:** VFX time ≤ **2 ms** on min‑spec at target res.

## **8.19 UE5 Material/Post Stack Presets**

* **AA:** TSR default; TAAU fallback.

* **Post chain:** Exposure (manual), minimal Bloom, Film Grain low, Vignette low; **Chromatic Aberration OFF**.

* **Master materials:** `M_Master_Surface`, `M_Master_Emissive`, `M_Master_Glass`, `M_Master_Decal`.

* **Instances only** in levels; no per‑asset unique shaders.

* **Don’t:** full‑screen color‑grade swaps per room; do localized volumes.

## **8.20 Fonts, Licenses, Fallbacks**

* **Device UI (bitmap):** *VT323* (SIL OFL).

* **HUD/UI Sans:** *Inter* (SIL OFL).

* **Headings/Labels:** *IBM Plex Sans* (SIL OFL).

* **Monospace (debug):** *JetBrains Mono* (Apache 2.0).

* **Fallback stacks:**

  * Sans: `Inter, IBM Plex Sans, -apple-system, Segoe UI, Roboto, Arial, sans-serif`

  * Mono: `JetBrains Mono, Courier New, monospace`.

* If using commercial fonts, acquire licenses and update this section.

## **8.21 Asset Naming & Folders (UE5‑ready)**

**Folders** (`/Content/Diplomagic/...`):

* `Art/Characters`, `Art/Props`, `Art/Environments`, `Art/Materials`, `UI`, `VFX`, `Audio/SFX`, `Audio/Music`, `Audio/VO`, `Design/Blueprints`.

**Prefixes**: `SM_` StaticMesh, `SK_` SkeletalMesh, `T_` Texture, `M_` Material, `MI_` MaterialInstance, `NI_` Niagara, `BP_` Blueprint, `AN_` Anim, `S_` Sound, `CUE_` SoundCue, `UMG_` Widget.  
 **Examples**: `SM_Tunnel_Vent_Cap_A`, `T_UI_Device_Amber_01`, `S_UI_FieldPad_Click_A`, `CUE_Mx_Stealth_Pad_A`.

## **8.22 Budgets by Level Type (starting targets)**

| Level Type | Visible Tris/frame | Draw Calls | Texture Streaming Budget |
| ----- | ----- | ----- | ----- |
| Interior/Corridor | ≤ 0.8 M | ≤ 1,200 | ≤ 1.5 GB |
| Hub | ≤ 1.0 M | ≤ 1,500 | ≤ 2.0 GB |
| Exterior | ≤ 1.5 M | ≤ 1,800 | ≤ 2.5 GB |

Notes: tune with profiling; reserve headroom for VFX and AI.

## **8.23 Concept Art Package Checklist (per location)**

* Key art (wide, hero).

* Callouts: materials, signage, props.

* Palette swatches with hex.

* Turnarounds for hero props.

* Lighting moods: day/night/Kadath.

* Blockout plan overlay with routes.

* VFX and audio notes.

## **8.24 Deliverables (Art & Audio)**

* Mood boards and palette sheet.

* Kitbash packs per locale.

* VFX bible for Splinter.

* Audio style guide + cue sheet template.

* Wwise project skeleton and routing.

* Accessibility checklist.

## **8.25 Approvals**

On approval: archive to MASTER as `[SEC-08-ARTAUDIO] v0.2` and update manifest. Next: **SEC‑09 Technology & Performance**.

# **Patch Instructions for Existing MASTER — SEC-09**

## **1) Replace this single manifest row**

Find the row that begins with `| SEC-09-TECH |` and replace the entire line with:

`| SEC-09-TECH | Tech spec | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2) Append this section to the end of MASTER (add a `` before it)**

# SEC-08 — CH5–CH6 Audio & Soundscape
Repo dir: /Patches

## Pillars (no music bias)
- **1994 texture:** tape hiss, CRT hum, analog radio.  
- **Kadath motif:** distant horn-calls; low choral beds.  
- **Raid clarity:** readable tells for charges, valves, chant.

## Key cues
- **Phrase motif:** whisper layers of “the stars are right tonight” only in cult chant beds; never spoken by party/NPCs.  
- **Zombies:** wet shuffle, jaw clack; aggro swell at 2 kHz.  
- **Night Gaunt:** ceiling skitter, air split before dive.  
- **Cultist rite:** pulse drone + syllabic mutter; build to bell.  
- **Beast:** hoof scrape + bellow; rising whoosh on charge.  
- **Warden Shade:** glassy ring; null when Ward Jam active.  
- **Star Vampire:** phase shimmer; reveal snap with Lights/flare.  
- **Valve turn:** dry metal groan; in-order triad confirms A→B→C.  
- **Charge plant/det:** canvas rip + sticky whump; 2 s fuse tick.  
- **Blue-on-blue:** single staccato beep + hard fail sting.

## Spaces
- **Deep D-LAMP:** moist reverb, slow drips, fan thrum, O2 low tone.  
- **Iron Highway:** tire grit, tunnel slap, engine knock.  
- **Annex:** concrete slapback, distant K‑9 bark, breaker pop.  
- **Vault:** rotating catwalk clack, pylon hum, gimbal groan.

## Mix rules
- Prioritize tells over bed during combat.  
- Side-chain chants under gunfire by −6 dB.  
- Keep UI tones short, dry, mono. No modern whooshes.

## Implementation notes
- Loop stems ≤ 60 s; randomize heads/tails.  
- One-shot library tagged by enemy/event.  
- Memory budget conservative; reuse stems across CH5→CH6.

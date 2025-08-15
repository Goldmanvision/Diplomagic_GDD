# One‑Pager — CH5–CH6 Root Merge
Repo dir: /Patches

**What**: Replace CH5/CH6; add systems/world/UI for CH6 raid.  
**Why**: Tighten pacing, align with rogue pivot, codify raid ROE.  
**How**: Text-only patches; root paste with helpers; QA scripts included.

**Non‑negotiables**
- 1994 period; MicroTAC/pagers/payphones/Polaroids/analog CCTV
- Prompts ≤14 chars
- CH6 = raid; lethal authorized; neutralizations score‑neutral
- Blue‑on‑Blue = fail; evidence cap 3
- Ambient phrase only: “the stars are right tonight.”

**Reviewer entry points**
- Narrative: `ROOT_SEC-03_*`
- Systems: `ROOT_Systems_Snippet_Replacements.md`
- World/UI: `ROOT_SEC-06-07_World_UI_CH5-CH6_Merge.md`, `SEC-06-CH6_Ascii_Map.md`
- QA: E2E script, scorecard, telemetry spec

**Merge**
- Branch: feat/ch5-6-root-merge → squash merge → tag `v0.6-ch5-6-merge`.

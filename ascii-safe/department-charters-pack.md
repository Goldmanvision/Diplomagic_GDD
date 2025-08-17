# Department Charters Pack
Version: 0.1  
Date: 2025-08-16  
Exports: `.md` only  
All content: 1994/1989 period‑accurate; sources: Narrative Playbook + Outline.

---
## 1) Narrative Department — Charter
**Purpose**: Deliver scene specs, dialogue, and branching that align to Playbook/Outline.  
**In**: scene beats, dialogue, UI text, collectibles lore.  
**Out**: `scene_spec_*.md`, `dialogue_*.md`, `collectibles_*.md`.

**Inputs → Outputs**  
Inputs: Playbook refs, Outline refs, Mail questions.  
Outputs: scene spec 1‑pager, dialogue drafts, asset lists, risks.

**Gates**  
1) Source linkage to Playbook/Outline section IDs.  
2) Period checks complete (media, slang, locations).  
3) Spec complete: goals, beats, puzzles, assets, risks.  
4) Branch coverage table + failstates.  
5) UI strings list for IBM Simon/Palm/Newton patterns.  
6) Tests: narrative consistency, continuity, and save/restore points.

**Templates**  
- Scene Spec 1‑pager: Goals | Beats | Puzzles | Assets | Risks | Sources | Tests.  
- Dialogue Page: Scene ID | Characters | Lines | Conditions | Notes.

**Suggested paths**: `/narrative/scenes/`, `/narrative/dialogue/`, `/narrative/collectibles/`.

**SLAs**: Draft ≤ 2d per scene; revision turn ≤ 24h.  
**Metrics**: rework rate, blocker count, branch defect rate.

---
## 2) Combat & Systems Department — Charter
**Purpose**: Specify mechanics and tuning. Provide testable parameters.  
**In**: design pillars, controls, math.  
**Out**: `mechanics_*.md`, `tuning_*.md`, `control_map.md`.

**Inputs → Outputs**  
Inputs: Narrative constraints, platform inputs, QA findings.  
Outputs: mechanics specs, parameter tables, edge‑case notes, test harness notes.

**Gates**  
1) Pillars stated and traced to mechanics.  
2) Parameter tables with ranges and defaults.  
3) 1994 input schemes validated; accessibility baseline noted.  
4) Save/load behaviors defined.  
5) Failure modes and exploits considered.  
6) Tests: deterministic checks and tuning scenarios.

**Templates**  
- Mechanics Spec: Pillar → Rule → Parameter → Event → Expected outcome.  
- Tuning Table: Param | Min | Max | Default | Test case.

**Suggested paths**: `/design/systems/`, `/design/controls/`, `/design/tuning/`.

**SLAs**: First pass ≤ 3d per mechanic; hotfix spec ≤ 24h.  
**Metrics**: exploit count, tuning iteration count, test coverage.

---
## 3) Statblocks & Enemies Department — Charter
**Purpose**: Define enemies/NPCs with behaviors and numbers.  
**In**: AI states, resistances, drops, spawn rules.  
**Out**: `enemy_*.md`, `npc_*.md`, `spawn_tables.md`.

**Inputs → Outputs**  
Inputs: Combat parameters, Narrative beats, level pacing.  
Outputs: stat schemas, behavior trees, spawn/drop tables.

**Gates**  
1) Schema complete: HP, ATK, DEF, speed, AI states, senses.  
2) Difficulty bands defined; scaling rules stated.  
3) Spawn rules tied to scene IDs.  
4) Drops and economy vetted by Systems.  
5) Tests: balance checks, edge behaviors, soft‑lock prevention.

**Templates**  
- Statblock: Field | Value | Rationale | Source scene.  
- Spawn Table: Scene | Enemy | Count | Trigger | Cooldown.

**Suggested paths**: `/data/statblocks/`, `/data/spawn/`.

**SLAs**: First enemy archetype ≤ 2d; variants ≤ 1d.  
**Metrics**: TTK distribution, wipe rate, soft‑lock incidents.

---
## 4) Authenticity & Research Department — Charter
**Purpose**: Verify all period claims. Provide references.  
**In**: research requests, citations, photos/ads analogues.  
**Out**: `period_check_*.md`, `refs_*.md`, `glossary_1994.md`.

**Inputs → Outputs**  
Inputs: Playbook/Outline refs, web.run citations where needed.  
Outputs: fact checks, approved analogues, red flags, glossary entries.

**Gates**  
1) Every claim cross‑checked to at least one reputable source.  
2) Conflicts logged with dates; decisions proposed.  
3) Tech/media usage matches 1994/1989 capabilities.  
4) Legal/ethical notes flagged.  
5) Tests: sample scenarios validated against sources.

**Templates**  
- Fact Check: Claim | Verdict | Sources | Notes.  
- Analogue Sheet: In‑game | Real‑world | Differences | Risk.

**Suggested paths**: `/research/checks/`, `/research/refs/`.

**SLAs**: Triage ≤ 24h; deep dive ≤ 3d.  
**Metrics**: red‑flag turnaround, citation completeness.

---
## 5) QA & UX Department — Charter
**Purpose**: Find defects and UX frictions early.  
**In**: test plans, heuristics, bug triage.  
**Out**: `test_plan_*.md`, `bug_triage_*.md`, `ux_findings_*.md`.

**Inputs → Outputs**  
Inputs: specs, builds, user stories.  
Outputs: prioritized bugs, repro steps, UX recommendations, pass/fail reports.

**Gates**  
1) Heuristics list per feature.  
2) Test matrix: input devices, OS, perf budgets.  
3) Severity taxonomy applied; blockers surfaced to Mail.  
4) Regression list maintained.  
5) Tests: save/load, failstates, narrative continuity checkpoints.

**Templates**  
- Bug Card: Title | Build | Steps | Expected | Actual | Severity | Owner.  
- Test Plan: Scope | Risks | Matrix | Cases | Exit.

**Suggested paths**: `/qa/plans/`, `/qa/bugs/`, `/qa/reports/`.

**SLAs**: Blocker triage ≤ same day; report per build ≤ 24h.  
**Metrics**: defect escape rate, time‑to‑triage, PASS% per gate.

---
## 6) Steam Operations Department — Charter
**Purpose**: Prepare store presence and release ops.  
**In**: capsule art, copy, tags, builds, depots.  
**Out**: `steam_store_*.md`, `release_checklist.md`, `build_notes_*.md`.

**Inputs → Outputs**  
Inputs: approved descriptions, screenshots, builds, achievements list.  
Outputs: store copy, asset checklists, release timelines, Deck settings.

**Gates**  
1) Copy matches Playbook tone; no spoilers.  
2) Asset specs meet Steam requirements.  
3) Tags and categories justified.  
4) Build/Depot/Branch mapping written; rollback plan noted.  
5) Tests: page preview review, Deck verification checklist.

**Templates**  
- Store Copy: Short | Long | Key features | Tags | Legal.  
- Release Checklist: Assets | Build IDs | Depots | Dates | Owners.

**Suggested paths**: `/ops/steam/store/`, `/ops/steam/builds/`.

**SLAs**: Store draft ≤ 3d; pre‑launch checklist T‑14d.  
**Metrics**: review rounds, asset rejection rate, Deck pass.

---
## Integration Touchpoints
- All departments route handoffs through **Mail (Postmaster)** using Handoff Checklist.  
- Mail maintains `/DECISIONS.md` and `/CHANGELOG.md` proposals.  
- Weekly integration note consolidates status.

## Naming conventions
Chats: `GDD Rebuild <YYYY-MM-DD HHmm ET> — <Department>`.  
Files: `/<dept>/<topic>_<YYYYMMDD>.md` or as per folder above.

## Change Log
- 2025-08-16: v0.1 created by Mail (Postmaster).


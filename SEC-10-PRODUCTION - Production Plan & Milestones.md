# [SEC-10-PRODUCTION] Production Plan & Milestones
Version: v0.1 • 2025-08-11  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-08-ARTAUDIO — Art Direction & Audio`
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-12-RISKS — Risks, Legal, Ratings`
- `SEC-13-APPENDICES — Appendices`

## **10.1 Scope & Assumptions**

* Solo developer with targeted contractors.

* Tech per SEC‑09; art/audio per SEC‑08; systems per SEC‑05; loops per SEC‑04.

* Release track: **Demo Halloween 2025 → Early Access Q2 2026 → Full Release Q1 2027**.

* Platforms: PC at full release; consoles post‑launch.

## **10.2 Team & Vendors (baseline)**

| Role | Mode | Notes |
| ----- | ----- | ----- |
| Creative/Tech Director (Nick) | FT | Design, code, integration, PM |
| 3D Artist (environments/props) | Contract | 15–25 hrs/wk Nov’25–Oct’26 |
| Character Artist/Rigger | Contract | 8–12 wks across slice→beta |
| Animator | Contract | 10–15 hrs/wk Jan’26–Nov’26 |
| UI/UX Designer | Contract | 6–10 wks across SEC‑07 deliverables |
| Technical Artist (Shaders/VFX) | Contract | 6–8 wks for Splinter VFX \+ perf |
| Sound Designer | Contract | 12–16 wks spread; Wwise impl |
| Composer | Contract | 10–14 wks, stems system |
| QA Lead (external) | Vendor | 2× passes: EA and pre‑gold |
| Localization Vendor | Vendor | Strings, LQA pre‑gold |

## **10.3 High‑Level Schedule**

| Phase | Window | Goals |
| ----- | ----- | ----- |
| **P0 Pre‑Pro Refresh** | Aug–Sep 2025 | Lock GDD v1.0, pipelines, perf budgets |
| **P1 Vertical Slice** | Sep–Nov 2025 | 1 polished mission (Clara), core devices, HUD; **Demo Oct 31, 2025** |
| **P2 EA Core** | Dec 2025–May 2026 | Ship Ch1–3, core loops complete, tuning; **Early Access by Jun 2026** |
| **P3 Content Build‑out** | Jun–Oct 2026 | Add Ch4–5, NYC hub, re‑entry states; perf parity |
| **P4 Beta** | Nov–Dec 2026 | Feature‑complete, content‑complete; only bug/perf |
| **P5 Gold** | Jan–Mar 2027 | Cert‑ready PC build, marketing assets, launch ops |

## **10.4 Milestones — Entry/Exit & Deliverables**

### **M1: Vertical Slice (due Nov 15, 2025\)**

**Entry:** SEC‑04/05 baseline implemented; device UI MVP; perf captures at target map.
 **Exit:** One Clara mission shippable; TAPLINE scan+triangulate; FieldPad photo→tag→warrant; MEDSTAT triage; HUD minimal; controller parity; demo branch tagged.
 **Deliverables:** Steam demo build, trailer cut, press kit v0.

### **M2: Early Access (due Jun 15, 2026\)**

**Entry:** Ch1–3 playable end‑to‑end; caseboard saves; ROE loop stable.
 **Exit:** Telemetry online (opt‑in), difficulty presets, accessibility baseline, crash‑free P90 ≥99.0%.
 **Content:** \~7–9 missions; NYC tunnels preview; devices feature‑complete V1.
 **Deliverables:** EA build, roadmap, patch plan, community guidelines.

### **M3: Content Expansion (Oct 31, 2026\)**

**Entry:** Stable EA; art perf budget holding.
 **Exit:** Add Ch4–5, hub re‑use loops, antagonist arcs Qi/Kent; arrest systems tuned; VO pass 1\.
 **Deliverables:** Major content update, marketing beats, LQA plan.

### **M4: Beta (Dec 15, 2026\)**

**Entry:** Feature‑complete; all chapters implemented.
 **Exit:** Content‑complete; bug backlog triaged; crash‑free P90 ≥99.5%; perf budgets met; accessibility check pass.
 **Deliverables:** Beta candidate builds, test plan, known issues.

### **M5: Gold (Mar 15, 2027\)**

**Entry:** All Blocker/Critical fixed; audio mix final; balance locked.
 **Exit:** Gold master signed; store assets delivered; mod tools beta post‑EA finalized.
 **Deliverables:** Release build, soundtrack stems pack, press kit v1.0.

## **10.5 Content Quotas (targets)**

| Asset | Slice | EA | Beta/Gold |
| ----- | ----- | ----- | ----- |
| Missions (playable) | 1 | 7–9 | 13–16 |
| Unique locales | 1 | 4–5 | 7 |
| Devices apps | 3 | 6 | 6 \+ polish |
| Enemy archetypes | 2 | 4 | 6 |
| Weapons/tools | 3 | 6 | 8 |
| VO lines (approx) | 50 | 400 | 800 |

## **10.6 Budget Ranges (rough order)**

* Art external: $35–60k.

* Audio external (SFX+Music): $20–40k.

* QA+LQA vendor passes: $10–25k.

* Misc (licenses, marketing, services): $5–15k.

* Total external range: **$70–140k** over 18–20 months.

* Internal time: tracked via timesheets; opportunity cost not priced here.

## **10.7 Pipelines & PM**

* **Source control:** Perforce with streams; weekly checkpoint tags mirror GDD checkpoints.

* **Branches:** `Dev`, `Release/*`, `ArtDrop`.

* **Builds:** CI nightlies; slice/EA/beta/gold branches locked.

* **Tasking:** 2‑week sprints; Definition of Done includes perf \+ accessibility checks.

* **Reviews:** Milestone gates require KPI dashboard and perf captures.

## **10.8 QA Strategy**

* Unit smoke tests on devices and evidence chain.

* Checklists per SEC‑07/08/09.

* Telemetry review weekly during EA.

* External test passes: pre‑EA, pre‑beta, pre‑gold.

* Bug policy: Blocker/Critical stop the line; High within 72h; Medium within sprint; Low as capacity allows.

## **10.9 Localization**

* Scope: UI, menus, HUD, device text, subtitles.

* String freeze at Beta; LQA pass before Gold.

* Languages beyond en‑US determined by demand.

## **10.10 Marketing & Community**

* Demo \+ EA beats, devlogs, controlled roadmap.

* Clear mod policy; community standards.

## **10.11 Risks & Mitigations**

* **Contractor availability:** pre‑book, backups, reduce critical path coupling.

* **Perf misses:** enforce budgets, cut set‑dress, prioritize silhouettes.

* **Scope creep:** milestone gates with quota tables; defer to post‑launch.

## **10.12 Deliverables**

* Timeline Gantt (simple), resource plan, cost tracker, risk register, publisher one‑pager.

## **10.13 Approvals**

On approval: archive to MASTER as `[SEC-10-PRODUCTION] v0.1` and update manifest. Next: **SEC‑11 QA, Localization, Accessibility**.

# **Patch Instructions for Existing MASTER — SEC-11**

## **1\) Replace this single manifest row**

Find the row that begins with `| SEC-11-QA |` and replace the entire line with:

`| SEC-11-QA | QA, loc, accessibility | v0.1 | 2025-08-11 | approved | archived to Master |`

## **2\) Append this section to the end of MASTER (add a `
` before it)**

\[\[PAGEBREAK\]\]

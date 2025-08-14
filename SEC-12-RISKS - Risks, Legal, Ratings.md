# [SEC-12-RISKS] Risks, Legal, Ratings
Version: v0.1  
Date: 2025-08-11  
Owner: Nick Goldman

### Related sections
- `SEC-09-TECH — Technology & Performance Targets`
- `SEC-10-PRODUCTION — Production Plan & Milestones`
- `SEC-11-QA — QA, Localization, Accessibility`
- `SEC-13-APPENDICES — Appendices`
- `SEC-14-QA — Quality Assurance Test Plan`

## **12.1 Key Risks Register**

| ID | Risk | Cat. | Prob. | Impact | Owner | Triggers | Mitigations |
|---|---|---|---|---|---|---|---|
| R‑01 | Scope creep across dual‑POV + devices | Prod | M | H | Nick | New features added post‑slice | Lock pillars; change‑control; defer to post‑launch |
| R‑02 | Performance misses on fog/VFX | Tech | M | H | Tech Art | GPU spikes; overdraw heatmaps | SEC‑08 caps; VFX budget gate; perf CI |
| R‑03 | Device UI overload/confusion | UX | M | M | UI | Playtest misuse >5% | Progressive disclosure; tutorials via cases; accessibility mode |
| R‑04 | Procedural realism frustrates | Design | M | M | Design | Negative playtest verbatims | Optional briefs; hint tiers; difficulty sliders |
| R‑05 | Dual‑protagonist content debt | Prod | M | H | Nick | Slip on shared spaces re‑use | Shared locations; modular objectives; reuse kits |
| R‑06 | Legal/ratings issue (minors in peril) | Legal | L | H | Legal | Platform flag; ratings query | No on‑screen harm to minors; implied peril only; content warnings |
| R‑07 | Audio/Font licensing gaps | Legal | M | H | Audio/UI | Missing license docs | Use OFL/Apache fonts per SEC‑08; track SFX/music licenses; audit before beta |
| R‑08 | Contractor availability | Prod | M | M | PM | Missed sprint deliverables | Pre‑book alternates; flexible scope; buffer time |
| R‑09 | Save corruption/state bugs | Tech | L | H | Eng | Crash on load; bad schema | Versioned schema; autosave validation; load tests |
| R‑10 | Mod misuse (post‑EA) | Comm | L | M | PM | Offensive content shared | In‑menu warnings; disable online sharing; policy + moderation |
| R‑11 | Libel/brand infringement | Legal | L | H | Legal | Real brand slips in | Fictional brands; art review checklist; legal pass |
| R‑12 | Story/imagery controversy | PR | L | M | PM | Social media flare‑ups | Clear themes doc; content toggles; press kit Q&A |

## **12.2 Legal & Compliance Checklist**

### IP & Contracts
- Wordmark **DIPLOMAGIC**: run clearance search; consider TM file (Nice Class 9, 41).
- Work‑for‑hire + IP assignment for all contractors; NDAs as needed.
- Model/voice releases for VO.
- Avoid real organizations/brands; use fictional names (e.g., Brightstar).

### Licenses
- **Fonts:** VT323, Inter, IBM Plex Sans, JetBrains Mono (open licenses) — see SEC‑08. Store license files in `/Docs/Licenses/`.
- **SFX/Music:** track sources and rights; prefer custom or CC‑BY/royalty‑free with commercial allowance. No viral copyleft for shipped audio.
- **Software:** comply with UE5/Marketplace EULAs; track any OSS (MIT/BSD/Apache) with NOTICE file.

### Privacy & Telemetry
- Opt‑in only. No PII. Random session IDs. Retention ≤ 180 days. Plain‑language consent screen.
- Crash reports scrubbed of usernames/paths where possible.

### Accessibility & Claims
- Do not state compliance beyond tested features. Publish an accessibility features list matching SEC‑07/11.

### Export/Regulatory
- Standard US export compliance. No encryption beyond engine defaults.

### Platforms (PC)
- Steam/Epic checklists: save path, controller prompts, crash reporter, quit to desktop, high‑DPI icon, privacy text.

## **12.3 Ratings Strategy (Targets)**

- **ESRB:** Mature 17+ expected. Likely content descriptors: Violence, Blood, Strong Language, Intense Violence (select scenes).
- **PEGI:** 18 likely for violence/horror intensity.

### Design guardrails
- No sexual content. No torture‑porn.
- **Minors:** no graphic harm on‑screen; peril implied or off‑screen only; fade/abstraction when needed.
- Reduced‑gore toggle and content warnings (scene‑specific).
- Language filtered to maintain target rating.

### Submission kit
- Unedited gameplay video of representative scenes (stealth, arrest, combat, Kadath).
- Written content questionnaire aligned to above guardrails.

## **12.4 Sensitive Content & Ethics**
- Law enforcement portrayal: procedural focus without endorsing brutality; ROE enforced; arrests preferred.
- Cult imagery: fictional symbols; avoid real‑world groups.
- Real places/people: fictionalized locales; no real persons implied.

## **12.5 Paperwork & Templates**
- Contractor MSA + SOW templates.
- VO agreement and rate card.
- Music commission agreement with deliverables (stems, looping).
- Asset ingestion checklist (naming, LODs, loudness, licenses).
- OSS NOTICE and third‑party attributions file.

## **12.6 External Reviews (Pre‑Gold)**
- Legal read‑through of narrative and UI text.
- License audit for fonts/SFX/music.
- Ratings pre‑submission check.
- Accessibility review against published features list.

## **12.7 Deliverables**
- Risk register spreadsheet (live).
- Legal/licenses binder.
- Ratings submission pack.
- Accessibility features list for store pages.
- Press kit Q&A on themes and guardrails.

## **12.8 Approvals**
On approval: archive to MASTER as `[SEC-12-RISKS] v0.1` and update manifest. Next: **SEC‑13 Appendices**.

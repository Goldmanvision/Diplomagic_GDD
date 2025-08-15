# Patch: CH2 — Avery “Inner Checkpoint”
Version: v0.1 • 2025-08-15
Owner: Nick Goldman

## Summary
Define Avery’s CH2 infiltration at the Jackson, SC compound. Add inner-gate passphrase mechanic (“the stars are right tonight”), non‑lethal rules of engagement with IA penalties, 1994 comms (fax FD‑302, teletype), evidence flow, scoring, prompts, and shared Alert hooks that impact Clara’s CH2 call‑intercept windows.

## Goals
- Penetrate inner checkpoint without civilian harm.
- Identify and detain a ring leader.
- Seize ledgers, rosters, and tapes referencing Brightstar.
- Coordinate with Aiken Co. SO (randomized deputy token `{DeputyName}`).

## Beats
1) **Field briefing:** Franklin leads; Krill joins. Issue passphrase and ROE.  
2) **Recon:** Tag rotations, note inner gate challenge, mark civilians.  
3) **Approach:** Cover or distraction; optional payphone coordination with Aiken Co. SO.  
4) **Inner gate challenge:** Avery must say exactly: “the stars are right tonight.” Wrong line → `Alert=High`. One fallback via Badge+Warrant bluff check; failure escalates alert.  
5) **Outbuilding search:** Seize cash ledger, rosters, microcassettes referencing Brightstar calls.  
6) **Detain Deacon analogue:** Prefer non‑lethal; secure .38 revolver as evidence.  
7) **Evidence chain:** Bag+tag; file FD‑302; fax to field office; send teletype BOLOs; book detainees with `{DeputyName}`.  
8) **Exfil + hook:** Save `F_GromleyCleared=1`. Deputy references “trail behind daycare.”

## Evidence
- Cash ledger, rosters, .38 revolver, microcassettes re: Brightstar, gate logbook.  
- Chain: property inventory → FD‑302 → fax → teletype notifications.

## Rules of Engagement (1994)
- Non‑lethal preferred. Lethal or unjustified force triggers IA penalties and score loss.  
- Magazine counts limited; no weapon lights. SIG P226 or S&W 13 only.

## Scoring (adds)
+5 each arrest, +3 each evidence bagged, +2 FD‑302 filed, +2 teletype sent  
−5 lethal force, −3 civilian endangered, −2 Alert High at end

## UI prompts (≤14 chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

## Flags / Vars
F_GromleyCleared, F_PassphraseSaid, Alert, AlertEnd, DeputyName, EvidenceCount

## Shared Alert Hook
If `Alert` escalates to High here, Clara’s CH2 “Call Intercept” base window shortens (already defined on Clara systems).

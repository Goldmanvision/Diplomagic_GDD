# Patch: CH2 — Avery “Inner Checkpoint”
Version: v0.1.1 • 2025-08-15
Owner: Nick Goldman

## Summary
Define Avery CH2 infiltration at the Jackson, SC compound. Add inner gate passphrase mechanic ("the stars are right tonight"), non-lethal rules of engagement, 1994 comms, evidence flow, scoring, prompts, and shared Alert hooks. Update: NPC-initiated lethal force is score neutral.

## Goals
- Penetrate inner checkpoint without civilian harm.
- Identify and detain a ring leader.
- Seize ledgers, rosters, and tapes referencing Brightstar.
- Coordinate with Aiken Co. SO using deputy token {DeputyName}.

## Beats
1) Field briefing. Franklin leads. Krill joins. Passphrase and ROE issued.  
2) Recon. Tag rotations. Note inner gate challenge. Mark civilians.  
3) Approach. Cover or distraction. Optional payphone to Aiken Co. SO.  
4) Inner gate challenge. Say exactly: "the stars are right tonight." Wrong line sets Alert High. One fallback via Badge plus Warrant bluff.  
5) Outbuilding search. Seize cash ledger, rosters, microcassettes that reference Brightstar calls.  
6) Detain Deacon analogue. Prefer non-lethal. Secure .38 revolver as evidence.  
7) Evidence chain. Bag and tag. File FD-302. Fax to field office. Send teletype BOLOs. Book with {DeputyName}.  
8) Exfil and hook. Save F_GromleyCleared=1. Deputy references trail behind the daycare.

## Evidence
Cash ledger. Rosters. .38 revolver. Microcassettes about Brightstar. Gate logbook.

## Rules of engagement
Non-lethal preferred. Lethal or unjustified force normally reduces score. Exception: if an NPC initiates lethal force, any player lethal response in that encounter is score neutral.

## Scoring
+5 arrest. +3 evidence bagged. +2 FD-302 filed. +2 teletype sent.  
-5 lethal force. -3 civilian endangered. -2 Alert High at end.  
Exception: NPC-initiated lethal force is score neutral. No bonus. No penalty.

## UI prompts (14 or fewer chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

## Flags and vars
F_GromleyCleared, F_PassphraseSaid, Alert, AlertEnd, DeputyName, EvidenceCount

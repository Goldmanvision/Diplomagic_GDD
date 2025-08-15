# Patch: CH5 — “D-LAMP Lead & Betsy Finale”
Version: v0.3 • 2025-08-15
Owner: Nick Goldman
Repo dir: /Patches

## Summary
Extends CH5 endgame. Avery follows Fred Franklin’s packet to **D-LAMP**; Clara resolves **Betsy** via conditional branch. If **Hauser pistol logged** and **Betsy pin sigils logged** and **SRS warrant active**, FBI raids Betsy’s house and bypasses the boss. Otherwise Clara fights **Wendigo Betsy**. Outcome converges: **Clara + Reddy follow Avery**.

## Key Beats (additions)
- **Avery — D-LAMP:** retrieve packet from Franklin’s effects; recon campus; inside or stakeout; capture lab POs and phone log intersections. Flags: `F_DLampLocated`, `F_DLampEntered?`, `F_DLampLead`.
- **Clara — Betsy:** conditional **raid bypass** or **boss fight**. Flags: `F_BetsyRaidBypass` or `F_BetsyBossDefeated` and `F_BetsyHouseCleared`.
- **Converge:** motel rendezvous; packet sync; route to SRS/D-LAMP in CH6.

## Evidence
D-LAMP purchase orders, dock logs, call intersections; Betsy house seizure list (raid) or recovered notes (boss).

## UI prompts (≤14 chars)
Badge, Pretext, Stakeout, Search, Bag, Tag, Knock, Warrant, Breach, Hide, Dodge, Shove, Cast L, Cast R, Shield, Ward Jam, Cuff

## Flags
F_DLampLocated, F_DLampEntered, F_DLampLead, F_BetsyRaidBypass, F_BetsyBossDefeated, F_BetsyHouseCleared, F_ClaraFollowsAvery

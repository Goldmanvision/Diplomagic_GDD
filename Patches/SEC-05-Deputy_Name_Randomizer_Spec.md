# SEC-05 — Deputy Name Randomizer
Repo dir: /Patches

## Goal
Randomize `{DeputyName}` per new game. 1960–1980 US birth cohort, Southern common names. Neutral ethnicity; no unique celebrities.

## Seed
- Use game seed or hash of save start time.
- Deterministic per save; different across saves.

## Pool (samples)
Mark Collins, Darryl Hayes, Terry Bishop, Ralph Jenkins, Wayne Porter, Tony Ramirez, Glen Walker, Eric Lawson, Keith Turner, Dennis Brooks, Shawn Parker, Billy Harris, Allan Cooper, Leonard Gray, Harold Reed

## Rules
- On first use, pick from pool by seed index.
- Reserve name in save; never re-roll mid‑story.
- UI: show “Deputy {DeputyName}” only; no surname required if elided.
- If cultural review flags a name, swap pool entry.

## API (pseudo)
```
idx = seed % len(pool)
DeputyName = pool[idx]
```

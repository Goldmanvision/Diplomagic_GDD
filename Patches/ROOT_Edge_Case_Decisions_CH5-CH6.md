# Edge-Case Decisions — CH5–CH6 Root Merge
Repo dir: /Patches

- **ROE vs civilians:** CH6 has none by design; if any are added later, they must disable raid ROE locally and restore scoring penalties.
- **DeputyName display:** If randomizer yields long names, UI may elide surname to keep prompts ≤14.
- **Phrase usage:** Ambient chant only — “the stars are right tonight.” No player/NPC direct input.
- **Evidence overflow:** If player collects >3 in CH6, only first 3 count toward score; rest remain for narrative.
- **Blue-on-Blue grace:** Shield-absorbed hits don’t fail; >10 m single shotgun pellet exception to avoid false positives.
- **Return to D‑LAMP after Annex breach:** Lock rover route to prevent softlocks.
- **Ammo starvation:** If ammo <25%, spawn throttling applies per tuning spec.
- **Night Gaunt in bright areas:** Ensure light-stagger feedback icon even under bright lighting.

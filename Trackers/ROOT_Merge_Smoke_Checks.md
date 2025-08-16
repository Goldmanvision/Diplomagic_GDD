# ROOT_Merge_Smoke_Checks.md
Quick, subjective checks after rendering docs and building the content.

## Structure
- [ ] SEC-03: CH5 and CH6 headings render; ToC anchors resolve.
- [ ] SEC-05: snippet IDs are unique; no duplicate anchors.
- [ ] SEC-06: ASCII map link resolves; Service Passage is the only CCTV zone; Vault has **no CCTV** text.
- [ ] SEC-07: HUD lists `Evidence 0/3` and `BlueOnBlue`; prompts match master and are ≤14 characters.

## Rules surface
- [ ] CH6 = raid; lethal authorized; neutralizations score-neutral.
- [ ] Blue-on-Blue hard fail (−10) with stated exceptions visible somewhere in docs.
- [ ] Breaker ≈90 s; K‑9 reroute described.

## Period
- [ ] No modern tech terms in UI prompts or narrative.
- [ ] FieldPad/MEDSTAT connectivity text limited to cable or SENTINEL.

## Readability
- [ ] No orphan headings or empty sections.
- [ ] No TODO placeholders except `<DEPUTY_NAME>` token where required.

## Outcome
- [ ] Ready to tag validations complete and request review on PR.

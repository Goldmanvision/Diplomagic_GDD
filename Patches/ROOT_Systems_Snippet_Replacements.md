# ROOT_Systems_Snippet_Replacements.md
> SEC-05 insertion blocks. 1994 period. Ambient phrase only: “the stars are right tonight.”

[SNIP-SEC05-SPELLS-SYSTEM]
Phrases equip L/R. Scrolls single-use. Mana calm-regen (no combat spike). Cast L/R available when bound. UI shows Cast L, Cast R.

[SNIP-SEC05-DEPUTY-RANDOM]
Deputy name randomized per session. Use <DEPUTY_NAME> token in text. Seed from save GUID + clock drift. No fixed names in strings.

[SNIP-SEC05-EVIDENCE-CAP-CH6]
Evidence cap in CH6 = 3. HUD shows Evidence 0/3. Gating: deny fourth pickup with prompt “Evidence full”.

[SNIP-SEC05-BLUE-ON-BLUE]
Blue-on-Blue = hard fail (−10). Exceptions: Shield-absorbed friendly hit; single shotgun pellet >10 m. Log to BlueOnBlue flag for HUD.

[SNIP-SEC05-CAMERA-RULES]
Cameras only in Service Passage. No CCTV in Vault. Photo evidence allowed only where cameras exist. Radiation zones block photography.

[SNIP-SEC05-K9-REROUTE]
K-9 reroute via handler diversion or scent decoy. Success opens 90 s patrol gap. Failure increases patrol density for 60 s.

[SNIP-SEC05-BREAKER-COOLDOWN]
Breaker ≈90 s to recycle after trip. Interact prompt disabled during cooldown; display “Breaker cooling”.

[SNIP-SEC05-TECH-CONSTRAINTS-1994]
No smartphone/Wi-Fi/Bluetooth/GPS/SMS. Use landlines, pagers, fax, film, Polaroid. FieldPad/MEDSTAT sync by cable or SENTINEL link only.

[SNIP-SEC05-HUD]
HUD must include: Evidence 0/3, BlueOnBlue flag, Cast L, Cast R, Equip L, Equip R. Prompts ≤14 characters.

### SEC-05 • CH6 Evidence Cap + Blue-on-Blue Guards

```pseudo
if Chapter == 6:
  EVIDENCE_CAP = 3

  onEvidenceInteract(item):
    if EvidenceCount >= EVIDENCE_CAP:
      HUD.flash("Evidence 3/3")
      disableInteract(item)
      return
    EvidenceCount += 1
    HUD.setEvidence(EvidenceCount, EVIDENCE_CAP)

  # Blue-on-Blue hard fail with exceptions
  onHit(event):
    if isFriendly(event.target):
      if event.absorbed_by_shield: return
      if event.weapon == "shotgun" and event.pellets_hit == 1 and event.distance_m > 10: return
      failMission(reason="Blue-on-Blue", penalty=-10)
      HUD.flag("BlueOnBlue")

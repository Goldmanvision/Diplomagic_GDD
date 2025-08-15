# SEC-05 — CH4 Boss, Spells, and Mana Systems
Repo dir: /Patches

## American Cult Boss — Mechanics
- **Phases (3):**
  1) **Gun & Glyphs:** .38 revolver; ward circles reflect bullets. **TK Push** breaks circles.  
  2) **Cosmic Rites:** Sweeping beams; use **Shield** or cover. Summons 2 **Warden Shades**.  
  3) **Anchor Break:** Boss reinforces loop with chant (“the stars are right tonight”). Interrupt with **Counter** or TK object hit.
- **Resists:** Reduced small‑arms damage when wards up; normal when down.  
- **Win:** Health to zero after final ward collapse. **Lethal authorized.** Civilian harm still penalized.

## Reddy TK (CH4)
- **TK Push:** Staggers boss, breaks ward circles.  
- **TK Shield (1x):** Party‑wide soak for 3s.

## Spellbook — Learnable Phrases (multi‑use)
- Stored in **FieldPad/MEDSTAT** “Phrases” list.  
- **Equip model:** Two slots (**Left/Right**). Single or dual wield.  
- **Casting:** **Cast L**/**Cast R** triggers the equipped phrase.  
- **Mana Pool:** `ManaMax`, `Mana`, `ManaRegen` (regen only at Camp or via rare tonics).  
- Example phrases unlocked in CH4:  
  - **Fast Travel** — return to **Avery’s car**; **Cost:** High; **Cooldown:** Chapter‑scoped lockout.  
  - **Shield** — brief damage reduction; **Cost:** Medium.  
  - **Ward Jam** — suppress one ward for 5s; **Cost:** Medium.  
  - Additional phrase choices per character can be awarded here or later.
- **Persistence:** Learned phrases persist across chapters via flags.

## Scrolls — Single‑Use Spells
- Appear as **Inventory** items. Consumed on use.  
- Not equip‑slot based. No persistence after use.

## Variables / Flags
- `ManaMax`, `Mana`, `ManaRegen`, `Cooldown_FastTravel`  
- `SpellsKnown[]`, `SpellsEquippedL`, `SpellsEquippedR`  
- `Scrolls[]` inventory list  
- `F_Spellbook`, `F_Spell_FastTravel`, `F_Spell_Clara`, `F_Spell_Avery`, `F_Spell_Reddy`

## Scoring Hooks
+5 Boss defeated, +3 evidence page, +2 no civilian harm, −3 alert escalated inside city. Lethal vs Boss is **neutral** for ROE penalties.

## 1994 Constraints
- Firearms: Avery SIG P226 or S&W 13; Boss .38; no weapon lights.  
- Comms: No SENTINEL in Kadath. Post‑escape phone = **Motorola MicroTAC**.

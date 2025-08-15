### Inner Checkpoint Passphrase
- Challenge requires exact verbal match: “the stars are right tonight.”  
- Logic: `if input == exact_phrase → Clearance; else → Alert += 1`.  
- One retry via “Badge+Warrant” bluff check; failure sets `Alert=High`.

### Rules of Engagement (1994)
- Non‑lethal arrests score higher; lethal or unjustified force applies IA penalties.  
- Magazine scarcity; no weapon lights; period‑correct sidearms: SIG P226 or S&W 13.  
- Scoring: +5 Arrest, +3 Evidence Bagged, +2 FD‑302, +2 Teletype; −5 Lethal, −3 Civilian Endangered, −2 Alert High end.

### Evidence Chain (Paper Era)
- Bag+tag items; complete FD‑302; fax to field office; teletype BOLOs to regional partners.  
- Variables: `EvidenceCount`, `FD302Filed`, `TeletypeSent`.

### Shared Alert Hook
- If Avery CH2 ends `Alert=High`, shorten Clara CH2 Call Intercept base window (Low→Med, Med→High thresholds).

### UI Prompts (≤14 chars)
Badge, Warrant, Say Phrase, Cuff, Arrest, Reload, Holster, Search, Bag, Tag, Evidence, Radio, Map, Fax 302, Teletype

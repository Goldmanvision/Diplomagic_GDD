# ROOT_Validation_Grep_Patterns.md
Scope: One-pass text sweeps for CH5–CH6 merge. Use either PowerShell (Windows) or bash. Record hits in the Results Summary.

## PowerShell
```powershell
# Prompt length check (from master list)
gc Patches/ROOT_SEC-07_UI_Prompts_Master.md |
  ? {$_ -match '^\s*-\s*(.+)$'} |
  % { if ( $matches[1].Length -gt 14 ) { "LONG PROMPT: $($matches[1]) [$($matches[1].Length)]" } }

# HUD flags
Select-String -Path **/* -Pattern "Evidence 0/3","BlueOnBlue"

# CH6 raid rules present
Select-String -Path **/* -Pattern "CH6 = raid","Lethal authorized","Neutralizations score-neutral"

# Blue-on-Blue rules and exceptions
Select-String -Path **/* -Pattern "Blue-on-Blue = hard fail","Shield-absorbed",">10 m single shotgun pellet"

# Cameras and breaker timing
Select-String -Path **/* -Pattern "Cameras only in Service Passage","No CCTV in Vault","breaker.*90 ?s"

# K-9 reroute mention
Select-String -Path **/* -Pattern "K-9 reroute"

# Period checks: forbid modern tech
Select-String -Path **/* -Pattern "smartphone","Wi-?Fi","Bluetooth","GPS","SMS" -CaseSensitive | % { "FORBIDDEN TERM: $($_.Path):$($_.LineNumber): $($_.Line)" }

# Spells systems
Select-String -Path **/* -Pattern "Phrases equip L/R","Scrolls single-use","Mana calm-regen"

# Ambient phrase exact
Select-String -Path **/* -Pattern "the stars are right tonight"

# Evidence cap CH6
Select-String -Path **/* -Pattern "Evidence cap in CH6 = 3"
```

## bash
```bash
awk -F'- ' '/^- /{s=$2; if(length(s)>14) printf("LONG PROMPT: %s [%d]
",s,length(s))}' Patches/ROOT_SEC-07_UI_Prompts_Master.md
grep -R -nE "Evidence 0/3|BlueOnBlue" .
grep -R -nE "CH6 = raid|Lethal authorized|Neutralizations score-neutral" .
grep -R -nE "Blue-on-Blue = hard fail|Shield-absorbed|>10 m single shotgun pellet" .
grep -R -nE "Cameras only in Service Passage|No CCTV in Vault|breaker.?90 ?s" .
grep -R -n "K-9 reroute" .
grep -R -nEi "smartphone|wi-?fi|bluetooth|gps|sms" . && echo "FORBIDDEN TERM FOUND"
grep -R -nE "Phrases equip L/R|Scrolls single-use|Mana calm-regen" .
grep -R -n "the stars are right tonight" .
grep -R -n "Evidence cap in CH6 = 3" .
```

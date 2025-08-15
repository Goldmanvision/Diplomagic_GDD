# Windows PowerShell — Find/Replace Helpers (CH5–CH6)
Repo dir: /Patches

> Use with caution. Prefer manual paste. These help search validation items on Windows.

## Search for disallowed tech
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'StarTAC|smartphone|Wi-?Fi|Bluetooth|GPS|SIM|digital camera' -SimpleMatch:$false
```

## Verify MicroTAC present
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'MicroTAC'
```

## Remove legacy non-lethal text (preview only)
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'non-\s*lethal preferred|IA penalties'
```

## Blue-on-Blue rule present
```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'Blue-?on-?Blue|friendly-?fire.*fail'
```

## Prompt length heuristic (>14 letters/spaces)
```powershell
Get-ChildItem -Recurse -File | Where-Object {$_.Name -like 'SEC-07*'} | ForEach-Object {
  Select-String -Path $_.FullName -Pattern '\b[A-Za-z][A-Za-z ]{14,}\b' -AllMatches
}
```

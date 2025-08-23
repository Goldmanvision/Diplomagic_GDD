# windows_build_packaging_wizard
**Macro name:** `windows_build_packaging_wizard`  
**Trigger:** `wiz pack-win`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** ZIP, installer (Inno Setup / NSIS), optional code signing, runtimes, SmartScreen, checksums.  
**Risks:** Missing DLLs, unsigned EXE warnings, long paths, AV false positives. Use ASCII‑safe names.

---

## Step 1 — Build output sanity
**Goal:** Clean, self‑contained Win64 build.

Actions
```text
• Produce a Shipping/Release Win64 build to: .\build\win64\
• Confirm Diplomagic.exe launches on a clean VM
• Remove editor/dev files and logs
```
Success: Launch OK on a vanilla VM user account.  
Prompt: `y` / `n`.

---

## Step 2 — Runtime dependencies
**Goal:** Ensure required redistributables are present or documented.

Options
```text
• Bundle VC++ Redistributable installer alongside the game (vcredist_x64.exe)
• Or statically link CRT if supported by your toolchain (not common for UE/Unity)
• Document minimum OS and GPU driver requirements in README.txt
```
Success: Game starts without missing DLL errors.  
Prompt: `y` / `n`.

---

## Step 3 — Folder layout for packaging
**Goal:** Predictable root for ZIP/installer.

Layout
```text
Diplomagic_Win64_v0.1.0\
  Diplomagic.exe
  <Engine content folders>
  LICENSE.txt
  README.txt
```
Rules
```text
• No extra nesting (one folder root only)
• ASCII names; keep path length < 200
```
Success: Folder ready at .\build\Diplomagic_Win64_v0.1.0\.  
Prompt: `y` / `n`.

---

## Step 4 — Create ZIP package (baseline)
**Goal:** Fast, no‑installer distribution.

PowerShell
```powershell
$src = ".\build\Diplomagic_Win64_v0.1.0\*"
$dst = ".\build\Diplomagic_Win64_v0.1.0.zip"
Compress-Archive -Path $src -DestinationPath $dst -Force
```
Success: ZIP created and opens cleanly; extract → game runs.  
Prompt: `y` / `n`.

---

## Step 5 — Optional code signing (EXE + DLL)
**Goal:** Reduce SmartScreen friction.

Prereqs
```text
• Have a code‑signing certificate (EV or OV)
• Install cert to local machine or provide .pfx + password securely
```

SignTool (Windows SDK)
```powershell
$ts = "http://timestamp.digicert.com"
signtool sign /fd SHA256 /tr $ts /td SHA256 /a ".\build\win64\Diplomagic.exe"
# Repeat for key DLLs if needed
signtool verify /pa ".\build\win64\Diplomagic.exe"
```
Success: `Successfully signed` and `Successfully verified`.  
Prompt: `y` / `n`.

---

## Step 6 — Inno Setup installer (option A)
**Goal:** Simple GUI installer with Start Menu entry.

Create script `.\pack\innosetup\Diplomagic.iss`:
```ini
[Setup]
AppName=DIPLOMAGIC
AppVersion=0.1.0
DefaultDirName={pf}\DIPLOMAGIC
DefaultGroupName=DIPLOMAGIC
OutputBaseFilename=Diplomagic_Setup_0.1.0
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
SetupIconFile=.\pack\innosetup\icon.ico

[Files]
Source: ".\build\Diplomagic_Win64_v0.1.0\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\DIPLOMAGIC"; Filename: "{app}\Diplomagic.exe"
Name: "{commondesktop}\DIPLOMAGIC"; Filename: "{app}\Diplomagic.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\vcredist_x64.exe"; Parameters: "/quiet /norestart"; StatusMsg: "Installing VC++ runtime..."; Check: NeedsVC()

[Code]
function NeedsVC(): Boolean;
begin
  Result := not RegKeyExists(HKLM, 'SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64');
end;
```

Build with Inno Setup Compiler (ISCC):
```powershell
& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" ".\pack\innosetup\Diplomagic.iss"
```
Success: `Diplomagic_Setup_0.1.0.exe` created under `.\pack\innosetup\Output`.  
Prompt: `y` / `n`.

---

## Step 7 — NSIS installer (option B)
**Goal:** Alternative lightweight installer.

Create script `.\pack\nsis\Diplomagic.nsi`:
```nsi
OutFile "Diplomagic_Setup_0.1.0.exe"
InstallDir "$PROGRAMFILES64\DIPLOMAGIC"
RequestExecutionLevel admin

Section "Install"
  SetOutPath "$InstDir"
  File /r ".\build\Diplomagic_Win64_v0.1.0\*"
  CreateShortCut "$SMPROGRAMS\DIPLOMAGIC\DIPLOMAGIC.lnk" "$InstDir\Diplomagic.exe"
  CreateShortCut "$DESKTOP\DIPLOMAGIC.lnk" "$InstDir\Diplomagic.exe"
SectionEnd
```
Compile with `makensis.exe`.  
Success: Installer EXE created.  
Prompt: `y` / `n`.

---

## Step 8 — Verify installer on clean VM
**Goal:** Install/uninstall cleanly on a fresh Windows user.

Checks
```text
• Installs under Program Files
• App launches from Start Menu and Desktop
• Uninstall removes files and shortcuts
• Optional: Installer EXE signed (Step 5)
```
Success: All checks pass.  
Prompt: `y` / `n`.

---

## Step 9 — Checksums and release folder
**Goal:** Provide integrity info for users and mirrors.

PowerShell
```powershell
Get-FileHash .\build\Diplomagic_Win64_v0.1.0.zip -Algorithm SHA256 > .\build\Diplomagic_Win64_v0.1.0.zip.sha256.txt
Get-FileHash .\pack\innosetup\Output\Diplomagic_Setup_0.1.0.exe -Algorithm SHA256 > .\pack\innosetup\Output\Diplomagic_Setup_0.1.0.exe.sha256.txt
```
Create `.\release\Windows\` and move final files + checksums there.  
Success: Release folder populated.  
Prompt: `y` / `n`.

---

## Step 10 — SmartScreen and AV sanity
**Goal:** Minimize warnings.

Guidelines
```text
• Prefer signed EXE and installer (Step 5)
• Avoid packing/obfuscation tools
• Keep version info and company metadata set in EXE properties
• If warned, submit installer to vendor false‑positive portals
```
Success: No warnings on the clean VM.  
Prompt: `y` / `n`.

---

## Step 11 — Platform‑specific notes
**Goal:** Package per channel rules.

Steam
```text
• Do NOT ship an installer; upload the plain game folder to your content depot
• Split symbols to a separate depot if used
```

itch.io
```text
• Use ZIP; push with butler
• Keep path stability between releases for saves/configs
```

Standalone web
```text
• Provide both ZIP and installer; publish SHA256 next to downloads
```
Success: Channel targets mapped.  
Prompt: `y` / `n`.

---

## Step 12 — Archive and tag
**Goal:** Traceability for the artifact.

Actions
```text
• Tag the repo (e.g., v0.1.0)
• Archive the final ZIP and installer to offline storage
• Save build logs and dependency versions
```
Success: Tag visible; archives stored.  
Prompt: `y` to finish, `n` for targeted troubleshooting.

---

## Troubleshooting quick refs
```text
• “MSVCP140.dll missing” → include vcredist_x64.exe or install via installer step
• Game runs only as admin → avoid writing to Program Files; store saves in %LOCALAPPDATA%
• Paths too long → enable long paths in Windows + Git; shorten folder names
• SmartScreen blocks unsigned EXE → sign binaries or distribute ZIP with instructions
```

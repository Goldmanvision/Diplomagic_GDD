# engine_vcs_builds_wizard
**Macro name:** `engine_vcs_builds_wizard`  
**Trigger:** `wiz engine`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Git + LFS setup, repo hygiene, Unity and Unreal build scripts, Windows packaging.  
**Risks:** Large binaries without LFS, wrong ignores, missing toolchains, long paths. Use ASCII‑safe names.

---

## Step 1 — Select engine(s)
**Goal:** Decide which engine paths to enable.  
Options: `Unity`, `Unreal`, or `Both` (if keeping parallel prototypes).  
**Prompt:** Reply `y` if your choice is clear. Reply `n` to ask questions or adjust.

---

## Step 2 — Repo structure
**Goal:** Stable, shallow layout at repo root.
```
/build/                 # local build outputs (gitignored)
/scripts/               # CI and local build scripts
/tools/                 # helper tools configs
/Docs/                  # design docs (or external)
/Engine/Unity/          # Unity project root (if Unity)
/Engine/Unreal/         # Unreal .uproject folder (if Unreal)
README.md
```
If migrating an existing project, keep actual engine root names but avoid spaces.  
**Success:** Folders exist or plan documented.  
**Prompt:** `y` / `n`.

---

## Step 3 — Install and initialize Git LFS
**Goal:** Ensure large binaries don’t bloat history.
```bash
git lfs install
```
**Success:** “Git LFS initialized” message.  
**Prompt:** `y` / `n`.

---

## Step 4 — Add .gitattributes for LFS
**Goal:** Track binary asset types in LFS.

Create `.gitattributes` at repo root:
```gitattributes
# Unity common binary assets
*.psd filter=lfs diff=lfs merge=lfs -text
*.png filter=lfs diff=lfs merge=lfs -text
*.jpg filter=lfs diff=lfs merge=lfs -text
*.jpeg filter=lfs diff=lfs merge=lfs -text
*.tga filter=lfs diff=lfs merge=lfs -text
*.tif filter=lfs diff=lfs merge=lfs -text
*.tiff filter=lfs diff=lfs merge=lfs -text
*.bmp filter=lfs diff=lfs merge=lfs -text
*.gif filter=lfs diff=lfs merge=lfs -text
*.exr filter=lfs diff=lfs merge=lfs -text
*.hdr filter=lfs diff=lfs merge=lfs -text
*.fbx filter=lfs diff=lfs merge=lfs -text
*.obj filter=lfs diff=lfs merge=lfs -text
*.blend filter=lfs diff=lfs merge=lfs -text
*.wav filter=lfs diff=lfs merge=lfs -text
*.ogg filter=lfs diff=lfs merge=lfs -text
*.mp3 filter=lfs diff=lfs merge=lfs -text
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.mov filter=lfs diff=lfs merge=lfs -text

# Unreal native binaries
*.uasset filter=lfs diff=lfs merge=lfs -text
*.umap   filter=lfs diff=lfs merge=lfs -text
```
Commit:
```bash
git add .gitattributes
git commit -m "chore: add LFS tracking for assets"
git push
```
**Success:** Committed and pushed.  
**Prompt:** `y` / `n`.

---

## Step 5 — Add .gitignore
**Goal:** Ignore generated files.

Create `.gitignore` at repo root (merge with existing if present):
```gitignore
# common
/build/
/tools/**/cache/
/scripts/**/temp/
*.log
.DS_Store
Thumbs.db

# Unity
/Engine/Unity/Library/
/Engine/Unity/Temp/
/Engine/Unity/Obj/
/Engine/Unity/Build/
/Engine/Unity/Logs/
/Engine/Unity/Packages/PackageCache/
/Engine/Unity/UserSettings/

# Unreal
/Engine/Unreal/Binaries/
/Engine/Unreal/DerivedDataCache/
/Engine/Unreal/Intermediate/
/Engine/Unreal/Saved/
/Engine/Unreal/.vs/
```
Commit:
```bash
git add .gitignore
git commit -m "chore: add gitignore for Unity/Unreal"
git push
```
**Success:** Committed and pushed.  
**Prompt:** `y` / `n`.

---

## Step 6 — Unity project settings (if Unity)
**Goal:** Make merges feasible and keep meta files.

In Unity Editor:
```
Edit → Project Settings → Editor:
  Asset Serialization: Force Text
  Version Control: Visible Meta Files
```
Save. Verify `ProjectSettings/ProjectVersion.txt` and `Packages/manifest.json` are version‑pinned.  
**Success:** Settings applied and visible in Git.  
**Prompt:** `y` / `n`.

---

## Step 7 — Unity build script and batch build (Windows x64)
**Goal:** Repeatable local build without UI.

Create C# at `Engine/Unity/Assets/Editor/BuildScript.cs`:
```csharp
using UnityEditor;
using System.IO;

public static class BuildScript {
  public static void BuildWindows64() {
    var outputDir = "build/win64";
    Directory.CreateDirectory(outputDir);
    var scenes = new[] {
      "Assets/Scenes/Main.unity" // adjust
    };
    BuildPipeline.BuildPlayer(scenes, Path.Combine(outputDir, "Diplomagic.exe"),
      BuildTarget.StandaloneWindows64, BuildOptions.None);
  }
}
```

Run from shell (adjust Unity path and projectPath):
```bash
"C:\Program Files\Unity\Hub\Editor\2022.3.40f1\Editor\Unity.exe" ^
  -batchmode -nographics -quit ^
  -projectPath "%CD%\Engine\Unity" ^
  -executeMethod BuildScript.BuildWindows64 ^
  -logFile "%CD%\build\unity_build.log"
```
**Success:** `build/win64/Diplomagic.exe` exists; log has no errors.  
**Prompt:** `y` / `n`.

---

## Step 8 — Unreal toolchain and batch build (Windows x64)
**Goal:** Cook, package, and archive a Win64 build.

Prereqs:
```
• Install Visual Studio Build Tools with C++ (MSVC) and Windows 10/11 SDK.
• Install a matching Unreal version (e.g., UE_5.3).
```

Commands (adjust paths and uproject):
```batch
REM Generate project files (first time or after plugin changes)
"C:\Program Files\Epic Games\UE_5.3\Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe" -Mode=GenerateProjectFiles -Project="C:\repo\Engine\Unreal\Diplomagic.uproject"

REM Build, cook, stage, pak, and archive
"C:\Program Files\Epic Games\UE_5.3\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun ^
 -project="C:\repo\Engine\Unreal\Diplomagic.uproject" ^
 -noP4 -platform=Win64 -clientconfig=Shipping -build -cook -stage -pak -archive ^
 -archivedirectory="C:\repo\build\win64_unreal"
```
Result appears under `build/win64_unreal/Windows`.  
**Success:** EXE present; run smoke test.  
**Prompt:** `y` / `n`.

---

## Step 9 — Versioning and tagging
**Goal:** Tie builds to immutable tags.

```bash
git tag -a v0.1.0 -m "Diplomagic v0.1.0"
git push origin v0.1.0
```
Embed version in Unity `PlayerSettings` or Unreal `Project Settings → Packaging` as needed.  
**Success:** Tag visible on remote.  
**Prompt:** `y` / `n`.

---

## Step 10 — Package for distribution
**Goal:** Zip with clean root.

Windows zip layout:
```
Diplomagic_Win64_v0.1.0.zip
  Diplomagic.exe
  (Unity) Data folders… or (Unreal) Windows content
  LICENSE.txt
  README.txt
```
Create zip (PowerShell example):
```powershell
Compress-Archive -Path .\build\win64\* -DestinationPath .\build\Diplomagic_Win64_v0.1.0.zip -Force
```
**Success:** Zip created; size reasonable; runs when extracted.  
**Prompt:** `y` / `n`.

---

## Step 11 — CI placeholders (optional)
**Goal:** Prep for GitHub Actions runners.

Unity job (ubuntu-latest or windows-latest):
```yaml
- uses: actions/setup-dotnet@v4
- name: Unity build (placeholder)
  run: echo "Integrate a Unity license and builder like game-ci/unity-actions later"
```

Unreal job (windows-latest):
```yaml
- name: Unreal build (placeholder)
  run: echo "Integrate RunUAT with cached artifacts later"
```
**Success:** Workflow skeletons committed.  
**Prompt:** `y` to finish, `n` for targeted troubleshooting.

---

## Troubleshooting quick refs
```
• LFS pointer files in build → ran build from a shallow/partial checkout; run `git lfs pull`.
• Unity cannot find scenes → fix scene paths in BuildScript.cs.
• Unreal missing toolchain → install MSVC + Windows SDK, restart shell.
• Long path errors → enable long paths in git and Windows.
• Huge repo size → audit binaries outside LFS; `git lfs migrate import` if needed.
```

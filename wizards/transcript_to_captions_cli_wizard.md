# transcript_to_captions_cli_wizard
**Macro name:** `transcript_to_captions_cli_wizard`  
**Trigger:** `wiz captions`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Fully offline speech‑to‑text for WAV/MP3/MP4 → SRT/VTT, Windows first.  
**Risks:** Wrong sample rate, noisy input, GPU not used, missing models on air‑gapped machines.

---

## Step 1 — Choose an engine
**Goal:** Pick one offline engine.

Options
```text
A) whisper.cpp (single .exe, CPU inference, no Python; recommended for simplicity)
B) faster-whisper (Python, faster on GPUs; requires venv and model download)
```
Decision: Choose A or B.  
Prompt: `y` after you decide, `n` for guidance.

---

## Step 2A — Install whisper.cpp (if you chose A)
**Goal:** Get the CLI and a model.

Actions (Windows)
```text
• Download whisper.cpp Windows release (main.exe) to F:\tools\whispercpp\
• Download a model file to F:\tools\whispercpp\models\
  - ggml-base.en.bin  (~150 MB)  → fast, English only
  - ggml-medium.en.bin (~1.5 GB) → higher accuracy, English only
```
Success: `F:\tools\whispercpp\main.exe` and a `.bin` model exist.  
Prompt: `y` / `n`.

---

## Step 2B — Install faster-whisper (if you chose B)
**Goal:** Set up a Python CLI with GPU/CPU support.

Commands (PowerShell)
```powershell
# create venv
python -m venv .venv && .\.venv\Scripts\Activate.ps1

# install runtime
python -m pip install -U pip wheel
python -m pip install faster-whisper soundfile
```
Models
```text
• Pick model size: tiny.en, base.en, small.en, medium.en
• First run will download the model to a cache; for offline, pre-download on a connected box and copy to the cache folder.
```
Success: `python -c "import faster_whisper"` runs without error.  
Prompt: `y` / `n`.

---

## Step 3 — Prepare media
**Goal:** Normalize audio for best accuracy.

Convert any input to 16‑bit mono 16 kHz WAV with ffmpeg:
```powershell
ffmpeg -y -i ".\input.mp4" -ac 1 -ar 16000 -vn ".\work\input_16k.wav"
```
Success: `work\input_16k.wav` exists.  
Prompt: `y` / `n`.

---

## Step 4A — Transcribe with whisper.cpp (SRT + VTT)
**Goal:** Produce captions with timestamps.

Commands
```powershell
# paths
$WH = "F:\tools\whispercpp\main.exe"
$MODEL = "F:\tools\whispercpp\models\ggml-base.en.bin"   # or medium.en

# run (English, word timestamps on, diarization off)
& $WH -m $MODEL -f ".\work\input_16k.wav" -osrt -ovtt -of ".\out\input" -l en -pp -pc -nt
```
Outputs
```text
.\out\input.srt
.\out\input.vtt
```
Success: Files exist with readable timestamps.  
Prompt: `y` / `n`.

---

## Step 4B — Transcribe with faster-whisper (SRT + VTT)
**Goal:** Same deliverables via Python.

Create `.\tools\fw_transcribe.ps1`:
```powershell
param(
  [string]$In = ".\work\input_16k.wav",
  [string]$OutStem = ".\out\input",
  [string]$Model = "medium.en",
  [switch]$CPU
)
$env:KMP_DUPLICATE_LIB_OK = "TRUE"
$useCPU = $CPU.IsPresent ? "1" : "0"
$code = @"
import sys, os
from faster_whisper import WhisperModel

inp = sys.argv[1]
out = sys.argv[2]
model_name = sys.argv[3]
use_cpu = sys.argv[4] == "1"

device = "cpu" if use_cpu else "auto"
compute_type = "float32" if use_cpu else "float16"
model = WhisperModel(model_name, device=device, compute_type=compute_type)

segments, info = model.transcribe(inp, language="en", vad_filter=True)
def srt_timestamp(t):
    h=int(t//3600); m=int((t%3600)//60); s=int(t%60); ms=int((t-int(t))*1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

# Write SRT
with open(out + ".srt", "w", encoding="utf-8") as f:
    for i,(seg) in enumerate(segments, start=1):
        f.write(f"{i}\\n{srt_timestamp(seg.start)} --> {srt_timestamp(seg.end)}\\n{seg.text.strip()}\\n\\n")

# Write VTT
with open(out + ".vtt", "w", encoding="utf-8") as f:
    f.write("WEBVTT\\n\\n")
    for seg in model.transcribe(inp, language="en", vad_filter=True)[0]:
        start = f"{int(seg.start//3600):02d}:{int((seg.start%3600)//60):02d}:{seg.start%60:06.3f}".replace('.',',')
        end   = f"{int(seg.end//3600):02d}:{int((seg.end%3600)//60):02d}:{seg.end%60:06.3f}".replace('.',',')
        f.write(f"{start} --> {end}\\n{seg.text.strip()}\\n\\n")
"@
$py = ".\.venv\Scripts\python.exe"
& $py - <<#PY $code PY#>> "$In" "$OutStem" "$Model" "$useCPU"
```
Run:
```powershell
.\tools\fw_transcribe.ps1 -In ".\work\input_16k.wav" -OutStem ".\out\input" -Model "medium.en"
```
Success: `out\input.srt` and `out\input.vtt` created.  
Prompt: `y` / `n`.

---

## Step 5 — Naming and QC
**Goal:** Stable filenames and quick verification.

Convention
```text
/media/captions/<segment>/<segment>_<YYYYMMDD>_en.srt
/media/captions/<segment>/<segment>_<YYYYMMDD>_en.vtt
```
QC
```powershell
# spot-check first 10 lines
Get-Content .\out\input.srt -TotalCount 20
# validate VTT header
Select-String -Pattern "^WEBVTT" -Path .\out\input.vtt
```
Success: Files follow naming and pass checks.  
Prompt: `y` / `n`.

---

## Step 6 — Optional: burn-in for previews
**Goal:** Hardsub quick preview files.

```powershell
ffmpeg -y -i ".\input.mp4" -vf "subtitles=.\out\input.srt:force_style='Fontsize=18'" -c:a copy ".\out\input_preview.mp4"
```
Success: Preview plays with baked subtitles.  
Prompt: `y` / `n`.

---

## Step 7 — Integrate with OBS + pipeline
**Goal:** Keep assets consistent across departments.

Checklist
```text
• Store SRT/VTT next to each final clip deliverable.
• Use CFR outputs and -ar 48000 in final encodes; captions remain separate.
• Steam Ops: prefer VTT for web preview; SRT for archival.
```
Success: Captions present for one sample clip.  
Prompt: `y` to finish, `n` for help on any sub-step.

---

## Troubleshooting quick refs
```text
• “No such model” → wrong filename; ensure the .bin (whisper.cpp) or model name (faster-whisper) matches.
• Garbled text → high noise or music; use 16 kHz mono source and try a larger model.
• Slow transcription → use base.en or tiny.en for speed, or B with GPU.
• Unicode issues → ensure UTF‑8 when viewing/editing SRT/VTT.
```

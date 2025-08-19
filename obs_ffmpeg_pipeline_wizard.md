# obs_ffmpeg_pipeline_wizard
**Macro name:** `obs_ffmpeg_pipeline_wizard`  
**Trigger:** `wiz capture`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** OBS capture profiles, clean audio routing, ffmpeg remux/transcode, deliverables.  
**Risks:** Wrong encoder, dropped frames, bad audio mix, variable framerate clips. Use ASCII‑safe paths.

---

## Step 1 — Install and verify tools
**Goal:** OBS and ffmpeg available on the capture machine.

Actions
```text
• Install OBS Studio (current stable).
• Install ffmpeg (static build) and add to PATH.
• Optional: Install MediaInfo for QC.
```
Verify:
```bash
obs --version 2>&1 | head -n1 || echo "OBS GUI only"
ffmpeg -version | head -n1
```
Success: ffmpeg version prints.  
Prompt: `y` / `n`.

---

## Step 2 — Create dedicated OBS Profile + Scene Collection
**Goal:** Isolate settings for Diplomagic.

Actions
```text
• Profile: DIPLOMAGIC_Capture
• Scene Collection: DIPLOMAGIC
• Settings → Video:
  - Base (Canvas): 1920x1080
  - Output (Scaled): 1920x1080
  - FPS: 60 (use 30 if footage targets 30)
```
Success: New profile + scene collection active.  
Prompt: `y` / `n`.

---

## Step 3 — Audio routing with separate tracks
**Goal:** Record mic and game on separate tracks + a master mix.

Settings
```text
• Settings → Audio:
  - Sample Rate: 48 kHz
  - Channels: Stereo
  - Disable unused Desktop/Mic devices to avoid duplicates.
• Add sources:
  - Desktop Audio (game/system)
  - Mic/Aux (voice)
```
Track map
```text
• Settings → Output → Recording → Check Tracks: 1,2,3
• Edit → Advanced Audio Properties:
  - Desktop Audio → Tracks: 1 and 3
  - Mic/Aux → Tracks: 1 and 2
  - Ensure Track 1 (master) contains both
```
Success: Metering shows both sources; track checkboxes set.  
Prompt: `y` / `n`.

---

## Step 4 — Recording format and encoder
**Goal:** Crash‑safe container and sane encoder defaults.

Settings → Output → Recording (switch Output Mode to “Advanced”):
```text
Type: Standard
Recording Format: MKV          # safer than MP4; remux later
Recording Path: C:\media\capture\raw   # ASCII‑safe path
Audio Track(s): 1,2,3
Encoder: NVIDIA NVENC (new)    # or x264 if no NVENC
Rescale Output: Off
```

Encoder tuning
```text
NVENC:
  Rate Control: CQP
  CQ: 18–22 (18 = higher quality)
  Keyframe Interval: 2 s
  Preset: Quality
  Profile: high
  Look‑ahead: Off (optional On if GPU headroom)
  Psycho Visual Tuning: On

x264:
  Rate Control: CRF
  CRF: 18–20
  Keyframe Interval: 2
  CPU Usage Preset: veryfast or faster (balance quality/CPU)
  Profile: high
```
Success: Test recording shows no drops.  
Prompt: `y` / `n`.

---

## Step 5 — Replay buffer and hotkeys (optional)
**Goal:** Capture last moments without rolling all the time.

Settings
```text
• Output → Replay Buffer: Enable, 45–120 s (depends on RAM)
• Hotkeys: Start/Stop Recording, Save Replay
```
Success: Hotkeys respond; replay writes files.  
Prompt: `y` / `n`.

---

## Step 6 — Scene basics and overlays
**Goal:** Clean capture with optional watermark.

Actions
```text
• Add source: Game Capture (or Window/Display as needed)
• Optional: Add Text (Trailer slate) and Image (small watermark)
• Lock sources to avoid accidental moves
```
Success: Preview shows correct feed.  
Prompt: `y` / `n`.

---

## Step 7 — Remux MKV → MP4
**Goal:** Convert safely with no re‑encode.

Option A — OBS GUI:
```text
• File → Remux Recordings → select MKV → Remux
• Optionally enable “Automatically remux to mp4” in Advanced settings
```

Option B — ffmpeg CLI:
```bash
ffmpeg -i "C:\media\capture\raw\clip.mkv" -c copy "C:\media\capture\intermediate\clip.mp4"
```
Success: MP4 plays; duration matches MKV.  
Prompt: `y` / `n`.

---

## Step 8 — Transcode deliverables (ffmpeg)
**Goal:** Create distribution‑ready files.

A) 1080p60 H.264 master
```bash
ffmpeg -i "in.mp4" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 60 -g 120 \
  -c:a aac -b:a 320k "out_1080p60_h264.mp4"
```

B) 1080p30 H.264
```bash
ffmpeg -i "in.mp4" -vf fps=30 -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 30 -g 60 \
  -c:a aac -b:a 320k "out_1080p30_h264.mp4"
```

C) 720p30 social
```bash
ffmpeg -i "in.mp4" -vf "scale=-2:720,fps=30" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 192k "out_720p30_social.mp4"
```
Success: Files encode without errors; spot‑check playback.  
Prompt: `y` / `n`.

---

## Step 9 — Audio loudness and cleanup
**Goal:** Normalize dialog/music levels and remove silence.

EBU R128 loudness (one‑pass)
```bash
ffmpeg -i "in.mp4" -filter:a "loudnorm=I=-16:TP=-1.5:LRA=11" -c:v copy "out_loudnorm.mp4"
```

Trim ends
```bash
ffmpeg -ss 00:00:03 -to 00:01:07 -i "in.mp4" -c copy "out_trimmed.mp4"
```
Fade in/out
```bash
ffmpeg -i "in.mp4" -vf "fade=t=in:st=0:d=0.5,fade=t=out:st=56.5:d=0.5" \
  -af "afade=t=in:st=0:d=0.5,afade=t=out:st=56.5:d=0.5" -c:a aac -b:a 320k \
  -c:v libx264 -crf 18 -preset slow "out_fade.mp4"
```
Success: Levels consistent; heads/tails clean.  
Prompt: `y` / `n`.

---

## Step 10 — Lossless mezzanine (optional)
**Goal:** Archive‑grade master for future edits.

ProRes 422 HQ (MOV)
```bash
ffmpeg -i "in.mp4" -c:v prores_ks -profile:v 3 -pix_fmt yuv422p10le -c:a pcm_s16le "out_prores422hq.mov"
```

FFV1 (MKV)
```bash
ffmpeg -i "in.mp4" -c:v ffv1 -level 3 -g 1 -c:a flac "out_ffv1.mkv"
```
Success: Files large but visually lossless.  
Prompt: `y` / `n`.

---

## Step 11 — Folders and naming
**Goal:** Predictable paths for automation.

Structure
```text
C:\media\capture\raw\
C:\media\capture\intermediate\
C:\media\capture\final\
```
Naming
```text
DIPLOMAGIC_<segment>_<YYYYMMDD>_<res><fps>.mp4
# Example: DIPLOMAGIC_Trailer_v0.1_20250818_1080p60.mp4
```
Success: Paths created; one sample file renamed.  
Prompt: `y` / `n`.

---

## Step 12 — QC checklist
**Goal:** Ship only clean files.

Checks
```text
• No dropped frames; steady frame pacing
• Constant framerate ( CFR ) on deliverables
• Audio 48 kHz stereo, no clipping
• Bitrate/CRF appropriate; file size reasonable
• Plays in VLC and target platform uploader
```
Success: QC passed on one sample clip.  
Prompt: `y` to finish, `n` for targeted troubleshooting.

---

## Troubleshooting quick refs
```text
• Stutters → cap FPS to 60; disable V‑sync; use Game Capture vs Display Capture
• NVENC overload → lower CQ or FPS; use Quality preset; close background apps
• Variable framerate → always transcode to CFR with explicit -r and -g
• Silent mic/game track → recheck track routing in Advanced Audio Properties
• Green/purple video → force sRGB; update GPU drivers
```

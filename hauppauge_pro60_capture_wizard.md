# hauppauge_pro60_capture_wizard
**Macro name:** `hauppauge_pro60_capture_wizard`  
**Trigger:** `wiz pro60`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Driver/firmware, OBS device config, audio routing, passthrough, QC.  
**Risks:** HDCP on source HDMI, USB bandwidth/power, mismatched frame rates, color range.

---

## Step 1 — Hardware and firmware
**Goal:** Stable device on Windows.

Actions
```text
• Connect Pro 60 via USB 3.x port (rear I/O preferred).
• HDMI IN: source (PC/console/camera). HDMI OUT: display (passthrough).
• Install Hauppauge Capture (Windows) to get drivers and control panel.
• Update device firmware from the Hauppauge Capture app if prompted.
• Optional: Insert SD card only if you plan standalone recording (not needed for OBS).
```
Success: Device enumerates; preview works in Hauppauge Capture.  
Prompt: `y` / `n`.

---

## Step 2 — HDCP and signal sanity
**Goal:** Ensure the HDMI signal is capturable.

Checks
```text
• Consoles: disable HDCP in system settings for gameplay capture.
• PCs/cameras: avoid HDCP-protected outputs (Blu‑ray, streaming apps).
• Output a clean 1080p60 signal if possible (reduces conversions).
```
Success: Live preview shows motion; no protected‑content error.  
Prompt: `y` / `n`.

---

## Step 3 — OBS source setup
**Goal:** Add the capture card with correct formats.

OBS steps
```text
• Sources → + → Video Capture Device (DirectShow) → Name: Pro60
• Device: HD PVR Pro 60 (or similar UVC name)
• Resolution/FPS Type: Custom
• Resolution: 1920x1080
• FPS: 60
• Video Format: NV12 (preferred) or YUY2 if GPU/encoder requires
• Color Space: 709
• Color Range: Limited (match source/display)
• Buffering: Off (reduces latency)
• Audio Output Mode: Capture audio only
• Audio device: HD PVR Pro 60 (if exposed)
```
Success: Preview updates at 60 fps; audio meters move.  
Prompt: `y` / `n`.

---

## Step 4 — Audio routing and monitoring
**Goal:** Separate tracks and low‑latency monitoring.

OBS settings
```text
• Settings → Audio → Sample Rate: 48 kHz; Channels: Stereo
• Output → Recording → enable Tracks 1,2 (and 3 if you want a master)
• Advanced Audio Properties:
  - Pro60 source → Tracks: 1 and 3
  - Mic/Aux → Tracks: 2 and 3
  - Monitoring: “Monitor and Output” only if you hear no echo/loop
```
Success: Game/program audio and mic land on separate tracks.  
Prompt: `y` / `n`.

---

## Step 5 — Encoder choice and file format
**Goal:** Smooth 1080p60 capture.

Recommendations
```text
• Recording format: MKV (safer) → later remux to MP4/MOV
• NVENC (new) if available; else x264 at CRF ~18–20
• Keyframe interval 2 s; profile high
• Drive: record to fast SSD/NVMe; avoid USB HDDs
```
Success: Short test record plays back without drops.  
Prompt: `y` / `n`.

---

## Step 6 — Passthrough display
**Goal:** Zero‑lag play on the external display.

Actions
```text
• Use the Pro 60 HDMI OUT to your display.
• Ensure display refresh matches source (60 Hz for 60 fps capture).
• Avoid playing from the OBS preview (adds latency).
```
Success: Gameplay feels normal on passthrough; OBS preview is slightly behind.  
Prompt: `y` / `n`.

---

## Step 7 — Standalone recording (optional)
**Goal:** Record to SD card without a PC.

Steps
```text
• Insert exFAT SD card.
• Use the hardware REC button to start/stop.
• Later, ingest the .MOV files to the workstation and remux/transcode as needed.
```
Success: Files appear on SD; copy speed OK.  
Prompt: `y` / `n`.

---

## Step 8 — Troubleshooting matrix
**Goal:** Resolve common issues fast.

Symptoms → Actions
```text
No signal in OBS:
  • Close Hauppauge Capture (only one app can hold the device)
  • Re‑select Resolution/FPS Type: Custom → set 1080p60
  • Try Video Format YUY2 if NV12 fails

Black screen with audio:
  • HDCP still enabled; disable on console or change source
  • Use different HDMI cable/port; confirm 60 Hz output

Stutters/dropped frames:
  • Lower FPS to 30 to test; record to local SSD
  • Use NVENC and reduce CQ/CRF; close background apps

Audio desync:
  • Disable “Use Device Timestamps” or set buffering Off
  • Set global sample rate to 48 kHz and re‑add source
```
Success: One minute test record passes QC (no drops, no desync).  
Prompt: `y` to finish, `n` for targeted troubleshooting.

---

## Notes
```text
• The device passes through up to 4K to your display but captures up to 1080p60.
• Power or bandwidth issues on front‑panel USB ports can cause disconnects; prefer rear I/O.
• Keep firmware and Hauppauge Capture updated when prompted.
```

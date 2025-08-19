# discord_webhooks_wizard
**Macro name:** `discord_webhooks_wizard`  
**Trigger:** `wiz discord`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Create Discord webhooks, test posts, embeds, mentions, GitHub Actions, and safety.  
**Risks:** Leaked webhook URL, rate limits, malformed JSON. Keep the URL secret; rotate if leaked.

---

## Step 1 — Create a webhook
**Goal:** Get a webhook URL in the target channel.

Actions
```text
Discord → Server Settings → Integrations → Webhooks → New Webhook
• Name: Postmaster Bot (or per‑channel name)
• Channel: #diplomagic‑ops (or desired)
• Copy Webhook URL → store in a secret manager
```
Success: You have a URL like `https://discord.com/api/webhooks/<id>/<token>`.  
Prompt: `y` / `n`.

---

## Step 2 — Store the URL securely
**Goal:** Keep the URL out of commits/logs.

Options
```text
• GitHub: Settings → Secrets and variables → Actions → New repository secret
  Name: DISCORD_WEBHOOK_URL  Value: <the url>
• Local shell: export DISCORD_WEBHOOK_URL="<the url>"
• CI self‑hosted: use env vault or OS secret store
```
Success: Secret saved.  
Prompt: `y` / `n`.

---

## Step 3 — Send a simple test
**Goal:** Verify connectivity and JSON.

Bash (curl)
```bash
curl -H "Content-Type: application/json" -X POST \
  -d '{"content":"Hello from Postmaster."}' \
  "$DISCORD_WEBHOOK_URL"
```

PowerShell
```powershell
$body = @{ content = "Hello from Postmaster." } | ConvertTo-Json
Invoke-RestMethod -Uri $env:DISCORD_WEBHOOK_URL -Method Post -ContentType "application/json" -Body $body
```
Success: Message appears in the channel.  
Prompt: `y` / `n`.

---

## Step 4 — Mentions and formatting
**Goal:** Notify people without noise.

Examples
```text
• Mention a user: <@USER_ID>
• Mention a role: <@&ROLE_ID>
• Suppress embed link preview: wrap URL in <>
• Code block: use triple backticks ```
```
Find IDs: enable Developer Mode → right‑click user/role → “Copy ID”.  
Success: A test message pings the right target.  
Prompt: `y` / `n`.

---

## Step 5 — Rich embeds
**Goal:** Structured status cards.

Bash (single embed)
```bash
read -r -d '' JSON << 'EOF'
{
  "username": "Postmaster Bot",
  "embeds": [{
    "title": "Build Deployed",
    "description": "Diplomagic_GDD MkDocs published",
    "url": "https://diplomagic.goldmanvision.com",
    "color": 5814783,
    "fields": [
      {"name": "Branch", "value": "`gh-pages`", "inline": true},
      {"name": "Commit", "value": "`$(git rev-parse --short HEAD)`", "inline": true}
    ],
    "footer": {"text": "Mail Dept"},
    "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  }]
}
EOF
curl -H "Content-Type: application/json" -X POST -d "$JSON" "$DISCORD_WEBHOOK_URL"
```
Success: Embed appears with fields and footer.  
Prompt: `y` / `n`.

---

## Step 6 — Attachments (files)
**Goal:** Send logs or zips under 8–25 MB limit (plan‑dependent).

Bash (multipart)
```bash
curl -F "payload_json={\"content\":\"Build log\"}" \
     -F "file1=@build/unity_build.log" \
     "$DISCORD_WEBHOOK_URL"
```
Success: File shows with the message.  
Prompt: `y` / `n`.

---

## Step 7 — GitHub Actions notifier
**Goal:** Post to Discord from CI on success/failure.

`.github/workflows/notify_discord.yml`
```yaml
name: Notify Discord
on:
  workflow_run:
    workflows: ["Build and Deploy MkDocs (Project)"]
    types: [completed]

jobs:
  notify:
    if: ${{ github.event.workflow_run.conclusion != 'skipped' }}
    runs-on: ubuntu-latest
    steps:
      - name: Post to Discord
        env:
          WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_URL }}
          STATUS: ${{ github.event.workflow_run.conclusion }}
          RUN_URL: ${{ github.event.workflow_run.html_url }}
        run: |
          if [ "$STATUS" = "success" ]; then COLOR=3066993; else COLOR=15158332; fi
          TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
          PAYLOAD=$(cat <<EOF
          { "embeds": [{
              "title": "MkDocs pipeline: $STATUS",
              "url": "$RUN_URL",
              "color": $COLOR,
              "timestamp": "$TS"
          }]}
          EOF
          )
          curl -H "Content-Type: application/json" -d "$PAYLOAD" "$WEBHOOK"
```
Commit and push.  
Success: Notifications appear after the tracked workflow completes.  
Prompt: `y` / `n`.

---

## Step 8 — Trello/Notion echoes (optional)
**Goal:** Mirror high‑signal events only.

Options
```text
• Trello Butler → send email to a Discord email integration or use third‑party relay.
• Notion → use a Zapier/Make scenario to post to Discord when Status changes to Blocked.
```
Success: One mirrored event lands in Discord without spam.  
Prompt: `y` / `n`.

---

## Step 9 — Threading and channels
**Goal:** Prevent channel spam.

Actions
```text
• Create a per‑build thread in #ops for noisy logs; keep #announcements high‑signal only.
• Name threads with date and repo (e.g., 2025‑08‑18‑GDD‑MkDocs).
```
Success: Messages routed to correct place.  
Prompt: `y` / `n`.

---

## Step 10 — Safety and rotation
**Goal:** Recover fast if the URL leaks.

Checklist
```text
• Restrict who can manage webhooks.
• If leaked: delete webhook in Discord UI, create a new one, rotate secret in GitHub.
• Search repos/CI logs for any plaintext URLs and purge where possible.
```
Success: You know the rotation path.  
Prompt: `y` to finish, `n` for targeted troubleshooting.

---

## Troubleshooting quick refs
```text
• 400 Bad Request → JSON malformed; validate with jq or an online linter.
• 401/404 → wrong URL or deleted webhook; recreate and update secret.
• Rate limited (429) → back off; include a small sleep and batch messages.
• Mentions not pinging → ensure the app has permission to mention roles/everyone.
```

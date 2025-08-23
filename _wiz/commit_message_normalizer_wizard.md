# commit_message_normalizer_wizard
**Macro name:** `commit_message_normalizer_wizard`  
**Trigger:** `wiz commit-msg`  
**Mode:** One step at a time. After each step, reply `y` (done → next) or `n` (repeat/fix).  
**Scope:** Conventional Commits guard: `type(scope): summary` with optional `!` for breaking.  
**Risks:** Windows line endings, non-exec hooks, merge commits.

---

## Step 1 — Add versioned hooks path
**Goal:** Keep hooks in the repo.

```bash
mkdir -p .githooks
git config core.hooksPath .githooks
git add .githooks
git commit -m "chore: init hooks path" || true
git push || true
```
Success: `git config --get core.hooksPath` returns `.githooks`.  
Prompt: `y` / `n`.

---

## Step 2 — Commit template (optional but recommended)
**Goal:** Guide authors in the editor.

Create `.gitmessage.txt`:
```text
type(scope)!: summary

# Body: what/why. Wrap ~72 chars. Skip if trivial.
# Footer: BREAKING CHANGE: <details> or refs (e.g., Closes #123)
```

Configure:
```bash
git config commit.template .gitmessage.txt
git add .gitmessage.txt
git commit -m "chore: add commit template" || true
git push || true
```
Success: `git commit` opens with the template.  
Prompt: `y` / `n`.

---

## Step 3 — Guard hook (POSIX shell; works on Git for Windows)
**Goal:** Enforce format and basic hygiene.

Create `.githooks/commit-msg`:
```bash
#!/usr/bin/env bash
# Guard Conventional Commits: type(scope)!: summary
# Allowed types
types='build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test'

file="$1"
first_line="$(head -n1 "$file" | tr -d '\r')"

# Allow merge/revert auto messages
if echo "$first_line" | grep -Eq '^(Merge|Revert) '; then exit 0; fi

# Trim leading/trailing spaces
first_line="$(echo "$first_line" | sed -E 's/^[[:space:]]+|[[:space:]]+$//g')"

# Validate: type, optional scope, optional !, colon+space, summary
if ! echo "$first_line" | grep -Eq "^(${types})(\([a-z0-9._-]+\))?(!)?: [^ ].+"; then
  echo "✖ Invalid commit header:"
  echo "  '$first_line'"
  echo "  Expected: type(scope)!: summary"
  echo "  Types: ${types//|/, }"
  exit 1
fi

# Length checks
subject_len="${#first_line}"
if [ "$subject_len" -gt 72 ]; then
  echo "✖ Subject too long ($subject_len > 72). Keep it concise."
  exit 1
fi

# No trailing punctuation
if echo "$first_line" | grep -Eq '[\.\!\?]$'; then
  echo "✖ Drop trailing punctuation in subject."
  exit 1
fi

# Enforce LF endings to avoid CI hook issues
if file "$file" | grep -qi 'CRLF'; then
  dos2unix "$file" >/dev/null 2>&1 || true
fi

exit 0
```

Make executable and add LF policy:
```bash
git add .githooks/commit-msg
git update-index --chmod=+x .githooks/commit-msg
printf ".githooks/* text eol=lf\n" >> .gitattributes
git add .gitattributes
git commit -m "chore: add commit-msg hook (Conventional Commits)"
git push
```
Success: Hook is executable and tracked.  
Prompt: `y` / `n`.

---

## Step 4 — Windows convenience wrappers (optional)
**Goal:** Ensure Git finds a runner even if sh.exe not on PATH.

Create `.githooks/commit-msg.bat`:
```bat
@echo off
REM Delegates to POSIX script via Git Bash if available
setlocal
set SH="%ProgramFiles%\Git\bin\sh.exe"
if exist %SH% (
  %SH% ".githooks/commit-msg" %1
  exit /b %ERRORLEVEL%
) else (
  echo Git Bash not found. Install Git for Windows.
  exit /b 1
)
```

Commit:
```bash
git add .githooks/commit-msg.bat
git commit -m "chore: windows wrapper for commit-msg"
git push
```
Success: Wrapper present.  
Prompt: `y` / `n`.

---

## Step 5 — Test
**Goal:** Confirm pass/fail behavior.

Good:
```bash
git commit --allow-empty -m "feat(core): add save system"
```

Bad (should fail):
```bash
git commit --allow-empty -m "update stuff"
git commit --allow-empty -m "feat: This message is intentionally way over the recommended seventy-two character limit to trigger guard"
git commit --allow-empty -m "fix(core): trailing period."
```
Success: Good passes. Bad fails with clear messages.  
Prompt: `y` / `n`.

---

## Step 6 — Exceptions and tuning
**Goal:** Adjust without weakening.

Options
```text
• Allow longer subjects: change 72 to 100 in the hook.
• Add new types: extend the `types` list.
• Skip the hook on CI-only bumps: run `git commit -m "chore: release vX.Y.Z" --no-verify`.
```
Success: Policy matches your repo.  
Prompt: `y` to finish, `n` for help.

---

## Troubleshooting quick refs
```text
• Hook not running → confirm core.hooksPath is set and files are executable.
• CRLF errors → ensure .githooks/* uses LF; Git for Windows will execute via sh.exe.
• Always failing → print the header: add `echo "$first_line"` for debugging.
```

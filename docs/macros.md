# DIPLOMAGIC — Macro Pack v0.1

- **Maintainer:** Macro Manager (McMa, subcontractor for Goldmanvision)
- **Installed:** 2025-08-17 09:00 ET
- **Scope:** Workspace-local tokens that expand to exact text blocks. No background work.
- **Exports:** `.md` by default.
- **Risk:** Chat resets or app updates can drop macro context. Keep this file under version control.

**Aliases:** The Macro Manager may be addressed as **McMa** in this workspace.

## Invocation
- Zero-arg macros: type the token.
- Macros with args: `name: arg1 | arg2 | ...` → arguments are inserted in the visible placeholders in order.
- Messages to Postmaster default to fenced code blocks.

## Macros

| Token | Purpose | Output type | Notes |
|---|---|---|---|
| `ptstamp` | Generate standardized chat title stamp | inline text | `GDD Rebuild <YYYY-MM-DD HHmm ET>` |
| `deptcode` | Return Mail Dept identity | inline text | `Department: Mail` / `Codename: Postmaster.` |
| `mydept` | Show current chat's department context | fenced code block | Returns ```<Department> : <Codename>``` |
| `mail-template` | Mail handoff skeleton | fenced block | For inter-department messages |
| `handoff-checklist` | Structured handoff fields | fenced block | Includes Gates and links |
| `decision-entry` | /DECISIONS.md entry | markdown snippet | Date-headed section |
| `changelog-entry` | /CHANGELOG.md entry | markdown snippet | Timestamped section |
| `scene-spec` | One-page scene shell | markdown page | Points to Playbook/Outline sections |
| `dialogue-page` | Dialogue writing shell | markdown snippet | Minimal columns |
| `enemy-statblock` | Enemy/system schema | markdown snippet | PS1-era style data |
| `spawn-row` | Spawn table row | plain text | Paste into spawn tables |
| `bug-card` | QA report card | fenced block | For QA & UX |
| `store-copy` | Steam store copy shell | markdown snippet | Steam Ops use |

## Templates

### `ptstamp`
```
GDD Rebuild <YYYY-MM-DD HHmm ET>
```

### `deptcode`
```
Department: Mail
Codename: Postmaster.
```

### `mydept`
```<Department> : <Codename>```

### `mail-template`
```
From: Postmaster (Mail)
To: <Department — Codename>
Subj: <Subject>

<Body>

Constraints: 1994/1989 accuracy; exports .md; no background work.
```

### `handoff-checklist`
```
Handoff Checklist
Scope:
Inputs:
Outputs:
Owners:
Gates: G1..G6
Risks:
Links: /DECISIONS.md, /CHANGELOG.md, GitHub source-of-truth
```

### `decision-entry`
```
## <YYYY-MM-DD> — Decision
Context:
Options:
Decision:
Rationale:
Impact:
Owner:
Links:
```

### `changelog-entry`
```
### <YYYY-MM-DD HH:MM ET>
Changed:
Added:
Removed:
Notes:
PR/Commit:
```

### `scene-spec`
```
# Scene Spec — <scene_id>
Goals:
Beats:
Puzzles:
Assets:
Risks:
Sources: Playbook §<ref>, Outline §<ref>
Tests: G1..G6
```

### `dialogue-page`
```
Scene ID:
Characters:
Lines:
Conditions:
Notes:
```

### `enemy-statblock`
```
Enemy: <name>
HP | ATK | DEF | Speed | Senses
AI States:
Resistances:
Drops/Economy:
Source scene:
Rationale:
```

### `spawn-row`
```
Scene | Enemy | Count | Trigger | Cooldown
```

### `bug-card`
```
Title:
Build:
Steps:
Expected:
Actual:
Severity:
Owner:
```

### `store-copy`
```
Short:
Long:
Key features:
Tags:
Legal:
Assets checklist:
```

## Change Control
- Version this file in Git at `docs/macros.md` or similar.
- When macros change, add a `changelog-entry` and a `decision-entry` explaining the rationale.

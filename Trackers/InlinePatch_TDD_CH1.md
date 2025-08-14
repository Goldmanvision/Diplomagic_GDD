# Inline Patch — TDD CH1 Device Hooks
Version: v0.1 — 2025-08-14 12:08Z
Owner: Nick Goldman

## BEGIN PATCH: TDD — CH1 Device Hooks

### MEDSTAT Notes unlock
- On card insert, enable Notes UI and call SEC‑05 CaseNote creation.
- Toast string key: `toast.note_logged_from_chart`.

### Roadside custody
- Use portable locker actor; same contract as 0A locker window.

## END PATCH

# Contributing

This repo favors small, reviewable PRs. Even if `main` is temporarily unprotected, use PRs whenever possible.

## Branching
- Feature: `feat/<scope>-<short-desc>`
- Chore/infra: `chore/<short-desc>`
- Fix: `fix/<scope>-<short-desc>`

## Commits
- Conventional commits: `feat:`, `fix:`, `chore:`, `docs:`, `ci:`
- Example: `feat(epilogue): packaging + state tracker`

## PRs
- Keep to ≤ 300 lines changed when feasible.
- Include a short rationale and validation notes.
- CI must be green before merge (when enabled).
- Squash or merge-commit; stay consistent per release cycle.
- To skip the local UI pack workflow, include `[skip local-ui]` in a commit message or add a `skip-local-ui` label to the PR.

## Line Endings
On Windows, Git may warn about CRLF. This repo enforces LF via `.gitattributes`. Do **not** change editor defaults; Git will normalize on commit.

## Review Checklist (docs)
- Period-accurate references (1994, with Avery 1989 prologue).
- Align to Playbook and Outline. No off-canon additions.
- Update `/Trackers` when `/Patches` change.
- Update `CHANGELOG.md` on notable merges.

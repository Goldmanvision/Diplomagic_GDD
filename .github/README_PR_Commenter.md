# PR Commenter — Rules Check

Install
1) Repo → Settings → Secrets → Actions → add **OPENAI_API_KEY**.
2) Repo → Settings → Actions → Workflow permissions → **Read and write**.
3) Copy `.github/workflows/pr-commenter.yml` into the repo.

Behavior
- Lists changed files and truncated patches.
- Calls OpenAI once (`gpt-4o-mini`) to check: 1994 period, prompts ≤14, CH6 raid rules, CH7 city rules.
- Posts a short PASS/FAIL comment to the PR. No files are written.

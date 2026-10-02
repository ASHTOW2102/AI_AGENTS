# ChangeScribe

ChangeScribe turns Conventional Commit messages into deterministic Markdown release notes.

It groups changes by type, preserves scopes, separates breaking changes, retains unparseable messages for review, and recommends a semantic-version bump: major for breaking changes, minor for features, and patch for fixes or performance work.

Optional AI polishing receives only parsed commit metadata. The deterministic Markdown always remains available.

## Input

Create a JSON array containing complete commit messages:

```json
[
  "feat(api): add cursor pagination",
  "fix: handle empty input",
  "feat!: remove legacy endpoint"
]
```

## Setup and usage

```bash
cd ChangeScribe
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python cli.py commits.json --local --output release-notes.md
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Scope

Version recommendations depend on accurate commit messages. Review ignored commits and breaking-change declarations before publishing a release.

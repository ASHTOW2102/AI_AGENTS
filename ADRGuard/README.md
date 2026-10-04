# ADRGuard

ADRGuard audits Architecture Decision Records (ADRs) before incomplete decisions become permanent technical debt.

It detects:

- missing or unsupported lifecycle status;
- missing or overly thin Context, Decision, Alternatives, and Consequences sections;
- TODO, TBD, FIXME, and template placeholders;
- accepted decisions that still contain open questions;
- superseded records without a replacement link;
- broken local Markdown links when a source path is provided.

The deterministic audit works without credentials. With OPENAI_API_KEY, the agent can add a remediation explanation using only sanitized finding metadata; the ADR body is not sent to the model.

## Setup

~~~bash
cd ADRGuard
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations and load it with your preferred environment manager. Never commit .env.

## Usage

~~~bash
python cli.py example_adr.md --no-model
python cli.py docs/adr/001-database.md
~~~

The command prints JSON and exits with 0 for a clean ADR, 2 for findings, or an argparse error for invalid input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

ADRGuard checks documentation quality and lifecycle hygiene. It does not decide whether an architecture choice is technically correct.

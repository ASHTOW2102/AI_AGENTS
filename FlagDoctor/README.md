# FlagDoctor

FlagDoctor audits feature-flag inventories before temporary switches become permanent operational debt.

It detects duplicate keys, expired enabled flags, stale disabled flags, missing owners, release or experiment flags without expiry, disabled flags with non-zero rollout, and enabled flags without target environments.

The deterministic audit works without credentials. With OPENAI_API_KEY, the agent turns sanitized findings into a cleanup plan; targeting rules and customer data are unnecessary.

## Setup

~~~bash
cd FlagDoctor
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations. Never commit .env.

## Usage

~~~bash
python cli.py example_flags.json --no-model
python cli.py flags.json --stale-days 45
~~~

Input contains evaluated_at and a flags array. The CLI exits 0 for a clean inventory, 2 for findings, or with an argparse error for malformed input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

FlagDoctor reviews supplied metadata. It never changes flag state and cannot prove that code paths are safe to remove. Confirm usage, dependencies, and rollback plans before cleanup.

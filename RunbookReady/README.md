# RunbookReady

RunbookReady audits runbook metadata for missing owners, stale reviews, absent rollback steps, and untested procedures.

It is deterministic, works locally without credentials, and emits structured JSON for CI or human review.

## Setup

~~~bash
cd RunbookReady
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

## Usage

~~~bash
python cli.py example_input.json
~~~

The CLI exits 0 for a clean audit and 2 when findings require review.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

RunbookReady evaluates supplied metadata only and never changes production systems. Confirm results against source records and organisational policy.

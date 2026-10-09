# ChangeWindow

ChangeWindow audits planned changes for missing owners, peak-hour timing, absent rollback plans, and overlapping services.

The agent is deterministic, runs locally without credentials, and produces structured JSON for CI checks or human review.

## Setup

~~~bash
cd ChangeWindow
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

## Usage

~~~bash
python cli.py example_input.json
~~~

The CLI exits 0 when no configured risks are found and 2 when findings need review.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

ChangeWindow evaluates supplied metadata only and never changes production systems. Confirm findings against source records and organisational policy before acting.

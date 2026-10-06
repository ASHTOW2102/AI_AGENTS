# QueueWatch

QueueWatch audits queue snapshots for excessive backlog, stale messages, dead-letter buildup, and missing consumers.

It is deterministic, runs locally without credentials, and emits JSON suitable for CI checks or human review.

## Setup

~~~bash
cd QueueWatch
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

This agent evaluates exported metadata only. It does not connect to production systems or make changes. Validate findings against the live system and your organisation's policies before acting.

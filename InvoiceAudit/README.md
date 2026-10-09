# InvoiceAudit

InvoiceAudit recalculates invoice totals and flags duplicate numbers, negative amounts, tax mismatches, and invalid balances.

The agent is deterministic, runs locally without credentials, and produces structured JSON for CI checks or human review.

## Setup

~~~bash
cd InvoiceAudit
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

InvoiceAudit evaluates supplied metadata only and never changes production systems. Confirm findings against source records and organisational policy before acting.

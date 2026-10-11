# MaskingAudit

MaskingAudit audits field inventories for unmasked sensitive data, production samples, missing owners, and reversible masking.

It runs locally without credentials and returns structured JSON for CI checks or human review.

## Setup

~~~bash
cd MaskingAudit
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

MaskingAudit evaluates supplied metadata only and never changes production systems. Confirm results against source records and organisational policy.

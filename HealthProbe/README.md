# HealthProbe

HealthProbe audits health-check metadata for long intervals, slow timeouts, missing dependencies, and shallow checks.

It runs locally without credentials and returns structured JSON for CI checks or human review.

## Setup

~~~bash
cd HealthProbe
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

HealthProbe evaluates supplied metadata only and never changes production systems. Confirm results against source records and organisational policy.

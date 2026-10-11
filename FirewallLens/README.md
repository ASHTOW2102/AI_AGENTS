# FirewallLens

FirewallLens audits firewall-rule exports for world-open access, unrestricted admin ports, missing owners, and permanent temporary rules.

It runs locally without credentials and returns structured JSON for CI checks or human review.

## Setup

~~~bash
cd FirewallLens
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

FirewallLens evaluates supplied metadata only and never changes production systems. Confirm results against source records and organisational policy.

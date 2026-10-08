# SecretLease

SecretLease audits secret metadata without reading secret values, finding overdue rotation, missing owners, broad scope, and absent expiry.

The agent is deterministic, runs locally without credentials, and emits structured JSON suitable for CI checks or human review.

## Setup

~~~bash
cd SecretLease
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

## Usage

~~~bash
python cli.py example_input.json
~~~

The CLI exits 0 when no configured risks are detected and 2 when findings require review.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

SecretLease evaluates supplied metadata only. It does not connect to production systems or make changes. Confirm findings against the live system and your organisation's policies before acting.

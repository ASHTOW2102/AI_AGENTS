# AccessReview

AccessReview audits account-access exports for dormant users, missing owners, admin privileges, and absent review dates.

The agent is deterministic, runs locally without credentials, and emits structured JSON suitable for CI checks or human review.

## Setup

~~~bash
cd AccessReview
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

AccessReview evaluates supplied metadata only. It does not connect to production systems or make changes. Confirm findings against the live system and your organisation's policies before acting.

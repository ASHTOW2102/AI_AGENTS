# PasswordGuard

PasswordGuard audits password-policy exports for short passwords, missing breached-password checks, unsafe resets, and absent lockouts.

It runs locally without credentials and returns structured JSON for CI checks or human review.

## Setup

~~~bash
cd PasswordGuard
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

PasswordGuard evaluates supplied metadata only and never changes production systems. Confirm results against source records and organisational policy.

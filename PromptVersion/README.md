# PromptVersion

PromptVersion audits prompt metadata for missing versions, owners, regression tests, change notes, and rollback copies.

It runs locally without credentials and emits structured JSON for CI or human review.

## Setup

~~~bash
cd PromptVersion
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

## Usage

~~~bash
python cli.py example_input.json
~~~

The CLI exits 0 for a clean audit and 2 when findings need review.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

This agent audits supplied metadata only and does not alter live systems. Verify results before acting.

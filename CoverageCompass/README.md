# CoverageCompass

CoverageCompass converts coverage.py JSON into a risk-ranked test backlog instead of treating coverage as a single percentage.

It prioritizes files using:

- line-coverage deficit against your target;
- uncovered line count;
- missing branch count;
- source size;
- a strong penalty for executable files with zero coverage;
- unusually large excluded-line counts.

The analysis runs locally without credentials. With OPENAI_API_KEY, the agent can turn sanitized metrics into a test-plan explanation. Source code is never sent to the model.

## Setup

~~~bash
cd CoverageCompass
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations. Never commit .env.

## Generate a report

~~~bash
coverage run -m pytest
coverage json -o coverage.json
~~~

## Usage

~~~bash
python cli.py coverage.json --no-model
python cli.py coverage.json --threshold 85 --top 5
python cli.py example_coverage.json --no-model
~~~

The CLI prints JSON and exits with 0 when the target is satisfied with no file risks, 2 when gaps remain, or an argparse error for malformed input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

CoverageCompass prioritizes measurable coverage gaps. It does not claim that high coverage proves correctness or replace mutation, integration, and system testing.

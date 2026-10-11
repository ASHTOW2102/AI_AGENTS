# EncryptionAudit

EncryptionAudit audits dataset metadata for missing encryption, weak algorithms, shared keys, and absent key rotation.

It runs locally without credentials and emits structured JSON.

## Setup

~~~bash
cd EncryptionAudit
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

## Usage

~~~bash
python cli.py example_input.json
~~~

The CLI exits 0 for a clean audit and 2 when review is needed.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

This agent audits supplied metadata only and does not change live systems. Verify results before acting.

# BackupBeacon

BackupBeacon audits backup-run metadata against a declared recovery policy before a silent failure becomes a disaster.

It detects RPO breaches, repeated failures, zero-byte successes, missing encryption/off-site/immutability protections, and missing or stale restore tests. It is read-only and never opens backup contents.

The deterministic audit needs no credentials. With OPENAI_API_KEY, it explains only sanitized findings.

## Setup

~~~bash
cd BackupBeacon
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations. Never commit .env.

## Usage

~~~bash
python cli.py example_audit.json --no-model
python cli.py backup_audit.json
~~~

Input uses timezone-aware ISO timestamps and includes evaluated_at, policy, backups, and restore_tests. The CLI exits 0 for a clean audit, 2 for findings, or with an argparse error for malformed input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

BackupBeacon validates reported evidence, not backup files. A successful job does not prove recoverability; representative restore tests remain essential.

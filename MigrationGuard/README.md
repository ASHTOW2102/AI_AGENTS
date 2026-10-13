# MigrationGuard

MigrationGuard audits planned database migrations before destructive changes or long locks reach production.

It detects destructive operations, excessive lock estimates, offline locking changes, duplicate IDs, missing rollbacks, untested migrations, and missing owners. The deterministic audit works without credentials. With `OPENAI_API_KEY`, the optional explanation receives only sanitized findings—not database contents or credentials.

## Setup

~~~bash
cd MigrationGuard
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy `.env.example` to `.env` only for optional AI explanations. Never commit a populated `.env`.

## Usage

~~~bash
python cli.py example_migrations.json --no-model
python cli.py migrations.json
~~~

The CLI exits 0 for a clean audit and 2 when findings require review.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

MigrationGuard evaluates supplied metadata only. It does not inspect a live database, estimate real query plans, create backups, or execute migrations. Rehearse every production migration in an equivalent environment.

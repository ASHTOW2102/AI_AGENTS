# EnvDoctor

EnvDoctor audits an environment file against its example template without exposing values in its report.

It detects missing and unexpected keys, empty or placeholder values, malformed lines, duplicate variables, and sensitive-looking high-entropy values that should stay out of version control. The CLI exits with status 2 for configuration errors.

Optional AI explanations receive only sanitized finding codes, key names, and messages—never environment values.

## Setup and usage

```bash
cd EnvDoctor
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python cli.py ../my-app/.env.example ../my-app/.env --local
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Safety

Run this locally. Do not paste secrets into chat, issue trackers, logs, or command arguments. A warning is heuristic and does not prove a value is a credential.

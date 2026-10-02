# OpenAPISentry

OpenAPISentry reviews OpenAPI 3.x JSON or YAML specifications before deployment.

The offline engine checks every HTTP operation for a unique operation ID, documentation, at least one 2xx response, and an explicit or inherited security requirement. Health and status paths may remain public. Errors produce exit status 2 for CI use.

Optional AI explanations receive only sanitized findings and endpoint locations, never request bodies, examples, or credentials.

## Setup and usage

```bash
cd OpenAPISentry
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python cli.py openapi.yaml --local
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Scope

This is a focused design review, not a full OpenAPI validator or penetration test. Use it alongside schema validation, authorization tests, rate-limit testing, and human security review.

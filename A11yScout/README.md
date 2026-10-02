# A11yScout

A11yScout performs a fast, offline accessibility review of static HTML.

It checks document language, image alt attributes, form-control labels, button accessible names, and skipped heading levels. Errors produce exit status 2 for CI use. Optional AI explanations receive findings only, never the page source.

## Setup and usage

```bash
cd A11yScout
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python cli.py page.html --local
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Scope

This is a focused static check, not a WCAG conformance claim. Combine it with browser-based automated tools, keyboard testing, screen-reader testing, contrast analysis, and review by disabled users.

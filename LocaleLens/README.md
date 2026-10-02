# LocaleLens

LocaleLens compares translated JSON with its base-language catalog. It detects missing or extra keys, empty translations, value-type mismatches, and changed interpolation placeholders. Errors produce exit status 2 for CI use. Optional AI explanations receive finding metadata only, never translation text.

## Setup and usage

```bash
cd LocaleLens
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python cli.py locales/en.json locales/fr.json --local
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Scope

LocaleLens checks structural consistency, not linguistic quality. Native-speaker review remains necessary for meaning, tone, grammar, plural rules, layout, and cultural appropriateness.

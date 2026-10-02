# SchemaScout

SchemaScout is a data-quality agent that learns a compact contract from a CSV file and checks later files for schema drift.

Its offline engine:

- infers integer, number, boolean, ISO-date, and string columns
- measures null counts and uniqueness
- flags mixed types and high-null columns
- exports a versioned JSON contract
- detects missing, unexpected, null, and type-invalid values
- exits non-zero when validation fails, making it suitable for CI

When an OpenAI key is configured, the agent can also explain the most important risks in the profile. Raw CSV rows are not sent; only the bounded profile is provided to the reviewer.

## Setup

```bash
cd SchemaScout
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env  # Windows
# cp .env.example .env  # macOS/Linux
```

## Usage

Create a profile and contract:

```bash
python cli.py profile customers.csv --contract customers.contract.json --local
```

Validate a later delivery:

```bash
python cli.py validate customers-next.csv customers.contract.json
```

Validation exits with status 2 when violations are found.

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Limitations

Inference is sample-based and contracts should be reviewed before production enforcement. CSV fields sent to optional AI review are limited to the generated profile examples; avoid using sensitive examples when enabling that mode.

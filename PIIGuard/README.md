# PIIGuard

PIIGuard detects and masks likely personal data before logs, support exports, or datasets are shared.

It recognizes email addresses, UK phone numbers, National Insurance numbers, UK postcodes, valid payment-card candidates, and IPv4 addresses. Card candidates must pass the Luhn checksum to reduce false positives.

The deterministic scanner works without credentials. If `OPENAI_API_KEY` is set, an optional explanation receives only finding types, masked sample lengths, and counts - never the original text.

## Setup

~~~bash
cd PIIGuard
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy `.env.example` to `.env` only for optional AI explanations. Never commit `.env`.

## Usage

~~~bash
python cli.py example_input.txt --no-model
python cli.py customer_export.csv --output customer_export.redacted.csv --no-model
python cli.py payload.json --output payload.redacted.json
~~~

The CLI exits 0 when no supported patterns are found and 2 when review is needed. It never overwrites the input unless you explicitly choose the same output path.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

Pattern matching cannot prove that data identifies a person and may produce false positives or miss unusual formats. PIIGuard is a pre-sharing safety check, not a full data-discovery, DLP, or UK GDPR compliance system. Review results and follow your organisation's retention and access policies.

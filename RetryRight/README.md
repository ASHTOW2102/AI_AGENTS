# RetryRight

RetryRight audits a JSON trace of repeated HTTP requests before bad retry behavior becomes an outage or duplicate transaction.

It detects:

- retries of POST/PATCH operations without an idempotency key;
- retries after terminal HTTP responses;
- ignored server Retry-After delays;
- immediate retries and decreasing backoff;
- retry loops that exceed an attempt budget.

The deterministic auditor runs without credentials. If OPENAI_API_KEY is set, the agent can add a plain-language explanation using only sanitized finding metadata. Request bodies, URLs, and headers are never sent to the model.

## Setup

~~~bash
cd RetryRight
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only if you want optional AI explanations, then load those variables using your preferred environment manager. Never commit .env.

## Trace format

The input is a JSON array in chronological order. Every event needs method and status. Retries also need delay_ms, which is the delay since the previous attempt. A response may include retry_after_ms. Set idempotency_key to true on the first event when the request is protected.

See example_trace.json for an intentionally unsafe trace.

## Usage

~~~bash
python cli.py example_trace.json --no-model
python cli.py example_trace.json --max-attempts 3 --min-delay-ms 100
~~~

The command prints JSON and exits with 0 for a clean policy, 2 when findings exist, or an argparse error for malformed input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

RetryRight reviews an observed retry sequence. It does not send HTTP requests, inspect payloads, or replace service-specific retry and idempotency design.

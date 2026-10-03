# HookSentry

HookSentry audits recorded webhook deliveries for security, replay, idempotency, ordering, and acknowledgement mistakes.

It detects:

- missing or invalid signature verification;
- timestamps outside a configurable replay window;
- duplicate delivery IDs and events processed more than once;
- failed processing incorrectly acknowledged with a 2xx response;
- successful processing answered with a retry-triggering status;
- out-of-order aggregate sequence numbers.

The deterministic auditor needs no credentials. With OPENAI_API_KEY, it can add a plain-language remediation explanation using only sanitized finding metadata. Webhook payloads and headers are never sent to the model.

## Setup

~~~bash
cd HookSentry
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations and load it with your preferred environment manager. Never commit .env.

## Trace format

Input is a chronological JSON array. Each delivery needs delivery_id, event_id, timezone-aware sent_at and received_at timestamps, signature_valid, processed, and http_status. Optional aggregate_key and sequence fields enable ordering checks.

See example_trace.json for an intentionally unsafe replay.

## Usage

~~~bash
python cli.py example_trace.json --no-model
python cli.py example_trace.json --tolerance-seconds 180
~~~

The CLI prints JSON and exits with 0 for a clean trace, 2 for findings, or an argparse error for malformed input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

HookSentry analyzes recorded metadata. It does not receive webhooks, validate a provider-specific cryptographic scheme, retain payloads, or replace a durable idempotency store.

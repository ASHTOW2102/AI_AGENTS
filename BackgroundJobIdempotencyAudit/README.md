# BackgroundJobIdempotencyAudit

Flags background job handlers that perform side effects (payments, emails, writes) without an idempotency key, causing duplicate side effects when the job framework retries after a crash.

## What it checks

Checks background job handlers with external side effects for idempotency keys and idempotent handling under at-least-once delivery.

## Usage

```python
from agent import audit

findings = audit({...})
for f in findings:
    print(f["severity"], f["issue"])
```

## Running tests

```bash
python -m unittest discover -s tests
```

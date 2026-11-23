# WebhookRetryIdempotencyAudit

Flags webhook receivers that support provider-side retry delivery but do not check an idempotency key, risking duplicate processing of the same event.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

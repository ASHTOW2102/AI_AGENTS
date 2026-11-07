# WebhookRetryStormAudit

Flags webhook delivery configurations prone to retry storms against degraded receivers.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

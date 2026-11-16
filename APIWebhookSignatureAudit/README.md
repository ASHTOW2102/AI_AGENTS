# APIWebhookSignatureAudit

Flags outbound webhook deliveries that are not signed, letting receivers be spoofed by forged payloads.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

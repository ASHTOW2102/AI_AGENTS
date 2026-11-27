# APIWebhookOutboundSSRFAudit

Flags outbound webhook configurations that allow delivering to internal/private IP destinations without validating the URL against an allowlist, a classic SSRF vector.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

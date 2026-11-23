# RateLimitBypassHeaderAudit

Flags API gateways that trust client-supplied headers to determine rate-limit identity, letting an attacker bypass limits by spoofing the header.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

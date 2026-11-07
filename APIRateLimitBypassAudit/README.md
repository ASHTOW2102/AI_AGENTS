# APIRateLimitBypassAudit

Detects API endpoints where rate limiting can be bypassed via alternate identifiers.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

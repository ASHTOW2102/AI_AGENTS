# CSRFTokenReuseAudit

Flags state-changing endpoints with no CSRF protection at all, or whose CSRF token is never validated against the current session.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

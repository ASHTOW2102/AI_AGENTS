# SearchQueryRateLimitAudit

Flags search query endpoints with no per-client rate limiting, risking expensive query abuse.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

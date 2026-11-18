# APIGraphQLBatchingAbuseAudit

Flags GraphQL endpoints that allow unbounded query batching, letting a single HTTP request bypass per-request rate limits.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

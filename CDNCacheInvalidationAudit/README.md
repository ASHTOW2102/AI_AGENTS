# CDNCacheInvalidationAudit

Audits CDN cache invalidation coverage and propagation delay for published content changes.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

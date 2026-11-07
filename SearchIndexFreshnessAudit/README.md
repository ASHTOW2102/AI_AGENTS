# SearchIndexFreshnessAudit

Flags search indexes with stale documents exceeding the acceptable reindex lag.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

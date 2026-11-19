# SearchResultCacheStalenessAudit

Flags search result caches with a TTL longer than the underlying index's update frequency, serving outdated results as if current.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

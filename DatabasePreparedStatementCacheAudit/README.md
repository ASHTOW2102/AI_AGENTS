# DatabasePreparedStatementCacheAudit

Flags database connection pools with prepared statement caching disabled, forcing a full parse/plan cycle on every query execution.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

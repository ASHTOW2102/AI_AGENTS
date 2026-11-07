# DatabaseQueryTimeoutAudit

Flags database queries with no statement timeout, risking long-held locks on slow queries.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

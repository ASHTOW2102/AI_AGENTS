# DatabaseLongRunningTransactionAudit

Flags database transactions open longer than acceptable, risking lock contention and bloat.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

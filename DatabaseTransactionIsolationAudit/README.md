# DatabaseTransactionIsolationAudit

Flags transactions that require serializable isolation for correctness but run at a weaker configured isolation level.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

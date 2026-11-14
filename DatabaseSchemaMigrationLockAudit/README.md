# DatabaseSchemaMigrationLockAudit

Flags database schema migrations that take exclusive table locks on large tables during business hours.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

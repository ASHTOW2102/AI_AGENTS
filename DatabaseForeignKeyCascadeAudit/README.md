# DatabaseForeignKeyCascadeAudit

Flags foreign keys with ON DELETE CASCADE pointing at financial or audit data, where a single parent delete can silently wipe out records that must be retained.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

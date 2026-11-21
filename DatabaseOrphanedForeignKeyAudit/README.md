# DatabaseOrphanedForeignKeyAudit

Flags database tables with rows whose foreign key no longer resolves to an existing parent row, indicating a missing or disabled constraint.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

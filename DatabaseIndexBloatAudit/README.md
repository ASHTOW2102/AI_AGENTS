# DatabaseIndexBloatAudit

Flags database indexes with excessive bloat ratio that degrade query performance.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

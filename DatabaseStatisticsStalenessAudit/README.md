# DatabaseStatisticsStalenessAudit

Flags database tables whose query-planner statistics are stale relative to the volume of changes since the last analyze.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

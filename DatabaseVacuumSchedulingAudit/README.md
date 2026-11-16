# DatabaseVacuumSchedulingAudit

Flags database tables with autovacuum disabled or badly tuned, risking bloat and transaction ID wraparound.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

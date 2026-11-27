# DatabaseReadReplicaLagThresholdAudit

Flags read replicas whose current replication lag exceeds the application's own configured maximum acceptable staleness.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

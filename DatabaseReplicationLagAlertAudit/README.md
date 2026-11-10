# DatabaseReplicationLagAlertAudit

Checks that database replication lag has an alerting threshold and is within acceptable bounds.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

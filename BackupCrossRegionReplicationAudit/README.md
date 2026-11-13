# BackupCrossRegionReplicationAudit

Flags backups stored only in their primary region without cross-region replication for disaster recovery.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

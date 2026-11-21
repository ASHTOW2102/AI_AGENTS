# BackupMultiRegionConsistencyAudit

Flags multi-region backup copies that have diverged from the primary copy's checksum, indicating a silent replication failure.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

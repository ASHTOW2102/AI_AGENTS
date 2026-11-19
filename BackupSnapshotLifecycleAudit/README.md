# BackupSnapshotLifecycleAudit

Flags disk snapshots that accumulate indefinitely with no lifecycle policy to expire old ones, inflating storage cost and attack surface.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

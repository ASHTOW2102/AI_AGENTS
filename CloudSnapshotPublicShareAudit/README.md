# CloudSnapshotPublicShareAudit

Flags disk/database snapshots shared publicly, at high severity when the snapshot is also known to contain sensitive data.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

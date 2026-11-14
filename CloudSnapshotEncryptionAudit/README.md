# CloudSnapshotEncryptionAudit

Flags cloud disk snapshots that are not encrypted or use a non-rotated encryption key.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

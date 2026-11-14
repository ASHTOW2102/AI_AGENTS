# BackupWriteOnceStorageAudit

Flags backups stored on mutable storage instead of write-once-read-many storage, risking ransomware tampering.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

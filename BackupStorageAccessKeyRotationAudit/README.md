# BackupStorageAccessKeyRotationAudit

Flags static access keys used to write backups to storage that have not been rotated within policy.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

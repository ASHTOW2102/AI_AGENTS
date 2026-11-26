# DatabaseBackupEncryptionAudit

Flags database backups that are not encrypted at rest, leaving a full data copy exposed if the backup storage is ever breached.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

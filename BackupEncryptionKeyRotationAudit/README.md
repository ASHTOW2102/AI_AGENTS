# BackupEncryptionKeyRotationAudit

Checks backup encryption keys for overdue rotation and insecure storage of the active key.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

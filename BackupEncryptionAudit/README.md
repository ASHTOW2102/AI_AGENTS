# BackupEncryptionAudit

Checks backup encryption, approved KMS use, rotation cadence, separation of keys from archives, and restore-principal counts.

## Usage

```python
from agent import audit
print(audit({"encrypted": True, "key_type": "managed_kms", "key_rotation_days": 180}))
```

Pass a backup policy dictionary; findings are returned as severity/issue records. This local audit requires no API key.

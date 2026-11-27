# CloudObjectLockRetentionAudit

Flags storage buckets holding compliance records with no object lock configured, so records can be deleted or altered before their legal retention period ends.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

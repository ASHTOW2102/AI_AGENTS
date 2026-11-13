# CloudIAMUnusedRoleAudit

Flags cloud IAM roles that have been unused for an extended period and should be revoked.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

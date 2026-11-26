# CloudKMSKeyUsageAudit

Flags cloud KMS keys whose decrypt permission is granted to any principal rather than a scoped allowlist.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

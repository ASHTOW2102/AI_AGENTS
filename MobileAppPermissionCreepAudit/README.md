# MobileAppPermissionCreepAudit

Audits mobile app permission requests for scope creep beyond declared feature needs.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

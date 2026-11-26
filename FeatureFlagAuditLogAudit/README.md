# FeatureFlagAuditLogAudit

Flags feature flag systems that do not log who changed a flag and when, leaving incident response with no change history to investigate.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

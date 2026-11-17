# FeatureFlagMultiTenantIsolationAudit

Flags feature flags evaluated globally instead of per-tenant, risking one tenant's rollout state leaking into another's.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

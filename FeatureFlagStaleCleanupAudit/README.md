# FeatureFlagStaleCleanupAudit

Flags fully-rolled-out feature flags that remain in the codebase long past their cleanup deadline.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

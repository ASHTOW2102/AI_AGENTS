# FeatureFlagDependencyCycleAudit

Flags feature flag configurations where flags depend on each other in a cycle, making it impossible to enable any of them cleanly.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

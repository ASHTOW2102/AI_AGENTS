# FeatureFlagRolloutVelocityAudit

Flags feature flag rollouts that jump from a small percentage straight to 100%, skipping the staged increments that would catch a regression early.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

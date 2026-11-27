# FeatureFlagRolloutPercentageAudit

Flags feature flags in a partial rollout with no kill switch, so a mid-rollout regression cannot be stopped without a code deploy.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

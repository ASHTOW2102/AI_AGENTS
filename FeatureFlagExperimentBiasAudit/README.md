# FeatureFlagExperimentBiasAudit

Flags feature flag experiments with randomization or sample-ratio issues that bias results.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

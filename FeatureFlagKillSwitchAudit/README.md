# FeatureFlagKillSwitchAudit

Checks that risky feature flags have a verified kill switch path for rapid rollback.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

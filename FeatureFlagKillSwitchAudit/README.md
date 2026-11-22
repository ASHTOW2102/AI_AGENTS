# FeatureFlagKillSwitchAudit

Flags critical features gated behind a feature flag with no remotely-toggleable kill switch, forcing a full deploy to disable a feature that is misbehaving in production.

## What it checks

Checks critical-path feature flags for a remotely-toggleable kill switch that doesn't require a redeploy or restart.

## Usage

```python
from agent import audit

findings = audit({...})
for f in findings:
    print(f["severity"], f["issue"])
```

## Running tests

```bash
python -m unittest discover -s tests
```

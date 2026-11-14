# FeatureFlagTargetingLeakAudit

Flags feature flag targeting rules that expose internal segment names or unreleased feature identifiers to client bundles.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

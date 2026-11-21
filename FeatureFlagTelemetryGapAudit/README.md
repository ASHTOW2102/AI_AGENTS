# FeatureFlagTelemetryGapAudit

Flags feature flags with no telemetry tied to their variants, making it impossible to tell whether a rollout is actually having the intended effect.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

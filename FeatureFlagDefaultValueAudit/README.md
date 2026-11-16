# FeatureFlagDefaultValueAudit

Flags feature flags whose default/fallback value when the flag service is unreachable is riskier than the safe default.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

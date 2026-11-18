# FeatureFlagApprovalWorkflowAudit

Flags high-risk feature flag changes that can be toggled in production without a second-person approval step.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

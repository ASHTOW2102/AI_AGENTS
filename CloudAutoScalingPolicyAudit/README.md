# CloudAutoScalingPolicyAudit

Flags auto scaling groups whose max capacity is not greater than min capacity, meaning no actual scaling range exists despite the policy.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ServerlessColdStartBudgetAudit

Flags serverless functions whose cold-start latency exceeds the budget set for their invocation path.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

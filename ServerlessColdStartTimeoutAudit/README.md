# ServerlessColdStartTimeoutAudit

Flags serverless functions whose average cold-start latency eats most of their configured timeout budget, risking spurious timeout failures.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

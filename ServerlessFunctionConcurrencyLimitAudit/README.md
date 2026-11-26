# ServerlessFunctionConcurrencyLimitAudit

Flags serverless functions whose reserved concurrency exceeds a downstream dependency's connection limit, risking connection exhaustion under load.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

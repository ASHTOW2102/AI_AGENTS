# CloudStorageLifecycleRuleAudit

Flags cloud storage buckets that store logs but have no lifecycle rule configured, letting log data accumulate and cost grow unbounded forever.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ServerlessEventSourceThrottleAudit

Flags serverless functions with event source mappings lacking concurrency throttles against downstream overload.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

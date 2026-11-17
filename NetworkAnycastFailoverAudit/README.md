# NetworkAnycastFailoverAudit

Flags anycast-routed services with no verified failover path when the nearest point of presence becomes unhealthy.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

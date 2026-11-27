# LoadBalancerCrossZoneAudit

Flags load balancers whose targets span multiple availability zones but cross-zone load balancing is disabled, leaving traffic distribution uneven and single-zone-fragile.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

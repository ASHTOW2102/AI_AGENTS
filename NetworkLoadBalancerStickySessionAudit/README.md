# NetworkLoadBalancerStickySessionAudit

Flags load balancers using sticky sessions keyed on a predictable cookie value, letting an attacker pin victims to an attacker-controlled backend.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

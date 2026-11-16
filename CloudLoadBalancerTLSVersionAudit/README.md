# CloudLoadBalancerTLSVersionAudit

Flags cloud load balancers that still permit deprecated TLS protocol versions.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

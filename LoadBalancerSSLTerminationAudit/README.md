# LoadBalancerSSLTerminationAudit

Flags load balancers that terminate TLS at the edge but forward backend traffic unencrypted, exposing requests to anyone on the internal network segment.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

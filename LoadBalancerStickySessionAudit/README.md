# LoadBalancerStickySessionAudit

Flags load balancers using sticky sessions with an unencrypted session cookie, exposing the session-routing identifier in plaintext.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

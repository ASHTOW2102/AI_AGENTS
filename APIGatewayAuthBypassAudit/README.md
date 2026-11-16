# APIGatewayAuthBypassAudit

Flags API gateway routes where internal service paths bypass the gateway's authentication layer.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

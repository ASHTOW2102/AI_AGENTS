# CloudNATGatewayScalingAudit

Flags cloud NAT gateways nearing their port-allocation limit, risking connection failures under load.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

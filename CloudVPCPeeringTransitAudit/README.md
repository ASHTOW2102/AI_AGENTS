# CloudVPCPeeringTransitAudit

Flags VPC peering connections that allow transitive routing to a third network the peer was never authorized to reach.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

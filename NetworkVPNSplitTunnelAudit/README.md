# NetworkVPNSplitTunnelAudit

Flags VPN configurations using split tunneling that route sensitive corporate traffic outside the tunnel.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

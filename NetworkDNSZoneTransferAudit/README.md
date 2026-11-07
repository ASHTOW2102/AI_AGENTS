# NetworkDNSZoneTransferAudit

Checks authoritative DNS servers for unrestricted zone transfer exposure.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

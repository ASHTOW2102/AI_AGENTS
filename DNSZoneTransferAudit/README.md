# DNSZoneTransferAudit

Flags authoritative DNS servers that allow full zone transfers (AXFR) from arbitrary hosts, leaking the entire internal DNS zone.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# MobileAppSSLPinningBypassAudit

Flags mobile apps with certificate pinning that can be bypassed because it only checks the leaf certificate, not the full chain.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

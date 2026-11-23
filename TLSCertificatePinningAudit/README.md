# TLSCertificatePinningAudit

Flags mobile apps that handle sensitive data over TLS without certificate pinning, leaving them exposed to MITM via a trusted-but-rogue CA.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

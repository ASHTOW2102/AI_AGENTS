# APIClientCertRotationAudit

Flags mutual-TLS API clients whose certificates are approaching expiry without an automated renewal process.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

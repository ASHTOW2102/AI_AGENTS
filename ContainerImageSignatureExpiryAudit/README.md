# ContainerImageSignatureExpiryAudit

Checks container image signing certificates for expiry and missing signature verification.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

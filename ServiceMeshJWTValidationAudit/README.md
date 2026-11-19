# ServiceMeshJWTValidationAudit

Flags service mesh sidecars configured to validate JWTs without pinning the expected issuer, accepting tokens from any trusted-looking issuer.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

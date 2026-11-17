# TokenBindingDeviceMismatchAudit

Flags sessions where the authentication token is used from a device fingerprint different from the one it was issued to.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# MobileAppUniversalLinkValidationAudit

Flags mobile apps that accept universal/app links without validating the signing team ID, letting another app hijack the link on a compromised or jailbroken device.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

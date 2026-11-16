# MobileAppDeepLinkValidationAudit

Flags mobile apps that handle deep links without validating the link's origin or target before navigation.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

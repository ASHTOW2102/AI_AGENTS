# MobileAppRootDetectionAudit

Checks that mobile apps handling sensitive operations detect rooted or jailbroken devices.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

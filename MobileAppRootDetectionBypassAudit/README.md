# MobileAppRootDetectionBypassAudit

Flags mobile apps handling sensitive data with no root/jailbreak detection, or whose detection is client-side only and trivially bypassable by hooking.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

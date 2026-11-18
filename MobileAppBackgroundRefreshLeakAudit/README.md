# MobileAppBackgroundRefreshLeakAudit

Flags mobile apps whose background refresh tasks continue fetching sensitive data after the user has logged out.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

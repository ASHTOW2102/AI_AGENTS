# TokenRefreshRaceConditionAudit

Flags OAuth clients where concurrent requests can each trigger an independent token refresh, racing and invalidating each other's tokens.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

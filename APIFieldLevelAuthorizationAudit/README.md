# APIFieldLevelAuthorizationAudit

Flags API endpoints that enforce authorization at the object level but not at the individual field level.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

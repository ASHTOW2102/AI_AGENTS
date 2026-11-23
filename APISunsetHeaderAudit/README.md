# APISunsetHeaderAudit

Flags deprecated API endpoints that do not advertise a Sunset header, leaving client developers with no machine-readable deprecation timeline.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

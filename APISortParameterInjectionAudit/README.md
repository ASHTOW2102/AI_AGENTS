# APISortParameterInjectionAudit

Flags API endpoints that pass a client-supplied sort parameter directly into a database ORDER BY clause.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

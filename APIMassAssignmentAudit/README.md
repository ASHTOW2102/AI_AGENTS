# APIMassAssignmentAudit

Flags API endpoints that bind client-supplied JSON fields directly to internal model attributes without an allowlist, enabling mass assignment of protected fields.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

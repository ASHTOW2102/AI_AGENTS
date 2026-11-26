# APISchemaVersioningAudit

Flags API changes marked as breaking that ship without a corresponding version bump, silently breaking existing clients.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# DataLakeAccessLoggingAudit

Flags data lake storage layers with object-level access logging disabled.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

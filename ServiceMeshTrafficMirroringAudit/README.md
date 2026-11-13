# ServiceMeshTrafficMirroringAudit

Flags service mesh traffic mirroring configurations that forward production payloads to non-production environments without sanitization.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

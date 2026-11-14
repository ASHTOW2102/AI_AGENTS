# ServiceMeshZoneAffinityAudit

Flags service mesh routing that ignores availability-zone locality, causing unnecessary cross-zone traffic cost and latency.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

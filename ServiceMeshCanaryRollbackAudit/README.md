# ServiceMeshCanaryRollbackAudit

Flags service mesh canary deployments with no automated rollback trigger tied to error-rate or latency regression.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

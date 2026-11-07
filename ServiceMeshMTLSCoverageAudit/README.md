# ServiceMeshMTLSCoverageAudit

Audits service mesh traffic for gaps in mutual TLS coverage between services.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

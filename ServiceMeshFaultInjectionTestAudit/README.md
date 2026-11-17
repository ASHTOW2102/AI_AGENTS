# ServiceMeshFaultInjectionTestAudit

Flags critical services that have never had fault injection testing performed against their mesh dependencies.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

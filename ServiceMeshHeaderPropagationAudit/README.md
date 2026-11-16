# ServiceMeshHeaderPropagationAudit

Flags services in a mesh that fail to propagate distributed tracing headers to downstream calls, breaking trace continuity.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

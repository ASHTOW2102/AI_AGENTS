# ServiceMeshRequestTimeoutPropagationAudit

Flags service mesh call chains where a callee's timeout is as long or longer than the caller's, so the callee keeps working on a request the caller already gave up on.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

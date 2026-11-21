# ServiceMeshRateLimitPropagationAudit

Flags services in a mesh where a global rate limit decision made at the edge is not propagated to internal callers, letting internal retries bypass it.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ServiceMeshCircuitBreakerAudit

Flags service mesh routes with no circuit breaker configured, letting a single failing dependency cascade into widespread resource exhaustion.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

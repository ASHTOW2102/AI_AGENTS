# ServiceMeshCircuitBreakerTuningAudit

Audits service mesh circuit breaker thresholds for defaults that are too permissive to protect downstream services.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ContainerHealthCheckLivenessAudit

Flags containers with no liveness probe configured (so a hung process is never restarted) or no readiness probe (so traffic reaches a container before it's ready).

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

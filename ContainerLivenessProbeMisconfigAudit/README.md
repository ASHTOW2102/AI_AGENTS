# ContainerLivenessProbeMisconfigAudit

Flags containers with liveness probes misconfigured to restart the container on transient slowness rather than true deadlock.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

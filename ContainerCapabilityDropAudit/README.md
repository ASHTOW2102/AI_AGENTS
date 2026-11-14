# ContainerCapabilityDropAudit

Checks containers drop unnecessary Linux capabilities instead of running with the full default set.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

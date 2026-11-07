# TokenRevocationLatencyAudit

Measures how long revoked tokens remain usable due to propagation delay in validation caches.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

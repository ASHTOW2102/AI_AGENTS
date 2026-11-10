# NetworkEgressAllowlistAudit

Flags workloads with unrestricted outbound network access instead of an explicit egress allowlist.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ServiceMeshMTLSEnforcementAudit

Flags service mesh mTLS policies set to permissive or disabled, allowing plaintext traffic between mesh workloads.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

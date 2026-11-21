# KubernetesEphemeralStorageQuotaAudit

Flags Kubernetes pods with no ephemeral storage limit, letting log or scratch writes fill the node disk and evict other workloads.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

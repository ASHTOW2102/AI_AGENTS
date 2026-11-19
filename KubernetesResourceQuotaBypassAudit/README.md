# KubernetesResourceQuotaBypassAudit

Flags Kubernetes namespaces with a ResourceQuota that pods can bypass by omitting resource requests entirely.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

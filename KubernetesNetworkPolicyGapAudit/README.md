# KubernetesNetworkPolicyGapAudit

Flags Kubernetes namespaces with no default-deny NetworkPolicy, leaving pod-to-pod traffic unrestricted.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

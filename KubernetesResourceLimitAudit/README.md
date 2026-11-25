# KubernetesResourceLimitAudit

Flags Kubernetes pods whose containers have no CPU or memory limit set, letting a single misbehaving container starve the whole node.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

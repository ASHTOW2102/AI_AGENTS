# KubernetesSecretRotationAudit

Flags Kubernetes secrets that have not been rotated within policy and lack automated rotation.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

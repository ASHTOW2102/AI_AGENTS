# KubernetesSecretEncryptionAtRestAudit

Flags Kubernetes clusters storing Secret objects in etcd without encryption at rest, exposing them to anyone with etcd backup access.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

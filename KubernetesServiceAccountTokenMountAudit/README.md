# KubernetesServiceAccountTokenMountAudit

Flags Kubernetes pods that auto-mount a service account token despite not calling the Kubernetes API.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

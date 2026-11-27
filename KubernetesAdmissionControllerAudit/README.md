# KubernetesAdmissionControllerAudit

Flags Kubernetes clusters with no pod security admission control enabled, allowing any pod spec including privileged ones to be scheduled.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

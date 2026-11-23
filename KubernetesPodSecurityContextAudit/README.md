# KubernetesPodSecurityContextAudit

Flags Kubernetes pods whose security context allows privilege escalation or does not require running as a non-root user.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

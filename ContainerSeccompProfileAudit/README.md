# ContainerSeccompProfileAudit

Audits containers for missing or overly permissive seccomp profiles.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

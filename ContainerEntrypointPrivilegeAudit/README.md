# ContainerEntrypointPrivilegeAudit

Flags container images whose entrypoint runs as root instead of a dedicated unprivileged user, widening the blast radius of a container-breakout bug.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ContainerRootlessRuntimeAudit

Checks that containers run under a rootless runtime configuration instead of root-mapped namespaces.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

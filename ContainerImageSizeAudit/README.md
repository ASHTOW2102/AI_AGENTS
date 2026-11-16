# ContainerImageSizeAudit

Flags container images that exceed a recommended size budget, slowing pulls and increasing attack surface.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

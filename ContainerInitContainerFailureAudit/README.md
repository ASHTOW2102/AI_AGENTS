# ContainerInitContainerFailureAudit

Flags Kubernetes pods whose init containers can fail silently, letting the main container start in a misconfigured state.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

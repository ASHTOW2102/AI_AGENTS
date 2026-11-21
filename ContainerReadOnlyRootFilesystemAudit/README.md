# ContainerReadOnlyRootFilesystemAudit

Flags containers running with a writable root filesystem when their workload never needs to write outside a declared volume.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

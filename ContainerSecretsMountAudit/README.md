# ContainerSecretsMountAudit

Flags containers that inject secrets as environment variables instead of mounted files, since env vars leak more easily via process listings, crash dumps, and child-process inheritance.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ContainerImageTagMutabilityAudit

Flags container registries that use a mutable 'latest' tag in production, or that have not enabled tag immutability at all.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

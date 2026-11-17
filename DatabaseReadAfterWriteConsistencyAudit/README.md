# DatabaseReadAfterWriteConsistencyAudit

Flags services reading from replicas immediately after a write without a mechanism to guarantee read-after-write consistency.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

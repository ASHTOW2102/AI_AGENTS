# DatabaseTriggerCascadeAudit

Flags database triggers that can recursively fire other triggers with no depth limit, risking runaway cascades on bulk writes.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

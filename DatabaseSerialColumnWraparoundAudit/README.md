# DatabaseSerialColumnWraparoundAudit

Flags database serial/auto-increment columns approaching their integer type's maximum value with no migration planned.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

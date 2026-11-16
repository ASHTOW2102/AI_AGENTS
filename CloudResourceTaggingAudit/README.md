# CloudResourceTaggingAudit

Flags cloud resources missing required ownership and cost-center tags needed for accountability and billing allocation.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

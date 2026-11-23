# DatabaseCompositeIndexRedundancyAudit

Flags database tables where one composite index is a strict column prefix of another, making the shorter index redundant dead weight on every write.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

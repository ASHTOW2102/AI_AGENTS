# SearchSynonymExpansionAudit

Flags search synonym lists that have gone stale past their own configured maximum review interval, letting query expansion drift from current product terminology.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

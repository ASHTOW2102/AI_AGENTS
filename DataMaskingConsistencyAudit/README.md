# DataMaskingConsistencyAudit

Flags datasets requiring cross-table join consistency whose masking is non-deterministic, breaking joins between separately masked copies of the same value.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

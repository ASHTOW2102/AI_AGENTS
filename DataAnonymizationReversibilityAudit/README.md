# DataAnonymizationReversibilityAudit

Flags anonymized datasets where a deterministic, unsalted transform makes re-identification via join attacks feasible.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

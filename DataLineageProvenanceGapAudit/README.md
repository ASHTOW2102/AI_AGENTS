# DataLineageProvenanceGapAudit

Flags derived datasets with no recorded lineage back to their source tables, making impact analysis and audits impossible.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

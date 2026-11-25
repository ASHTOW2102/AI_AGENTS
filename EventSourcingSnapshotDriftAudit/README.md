# EventSourcingSnapshotDriftAudit

Flags event-sourced aggregates whose stored snapshot predates the current schema version, risking a crash or silent misread when the snapshot is rehydrated.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

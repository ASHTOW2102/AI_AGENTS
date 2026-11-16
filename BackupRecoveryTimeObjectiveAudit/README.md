# BackupRecoveryTimeObjectiveAudit

Flags backup/restore procedures whose measured recovery time exceeds the business's recovery time objective.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

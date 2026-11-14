# DataExportAuditTrailAudit

Flags data export operations that leave no audit trail of who exported what and when.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

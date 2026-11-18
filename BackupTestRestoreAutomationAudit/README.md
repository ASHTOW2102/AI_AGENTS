# BackupTestRestoreAutomationAudit

Flags backup systems that rely on manual restore drills instead of an automated, regularly scheduled restore test.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

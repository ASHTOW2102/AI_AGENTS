# DatabaseDeadlockRetryStormAudit

Flags databases that retry deadlocked transactions with no backoff, so a deadlock under load triggers a self-reinforcing retry storm.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# TLSSessionResumptionAudit

Flags TLS servers supporting session resumption whose session ticket keys are never rotated, letting a single leaked key decrypt sessions indefinitely.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

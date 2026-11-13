# MobileAppClipboardLeakAudit

Flags mobile apps that copy sensitive data to the system clipboard without expiry or exclusion from clipboard history.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

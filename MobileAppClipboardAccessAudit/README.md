# MobileAppClipboardAccessAudit

Flags mobile apps that copy sensitive data to the system clipboard without clearing it after a timeout, leaving it readable by any other app.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

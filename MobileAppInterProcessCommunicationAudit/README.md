# MobileAppInterProcessCommunicationAudit

Flags mobile apps exposing exported components (activities, services, content providers) that accept input from other apps without permission checks.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

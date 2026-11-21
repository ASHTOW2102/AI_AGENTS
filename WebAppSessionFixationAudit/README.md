# WebAppSessionFixationAudit

Flags web applications that keep the same session identifier across login, letting an attacker fixate a victim's session before authentication.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

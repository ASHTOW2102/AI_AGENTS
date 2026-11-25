# WebAppOpenRedirectAudit

Flags redirect endpoints that do not validate the target URL, enabling open-redirect abuse in phishing links.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# APIRequestSmugglingAudit

Flags API endpoints vulnerable to request smuggling via inconsistent Content-Length/Transfer-Encoding handling.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

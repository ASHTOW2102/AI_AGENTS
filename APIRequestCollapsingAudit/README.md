# APIRequestCollapsingAudit

Flags expensive API endpoints with no request collapsing, letting a thundering herd of identical concurrent requests all hit the backend.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# APIConditionalRequestAudit

Flags API endpoints that don't support conditional requests (If-Match/If-None-Match), allowing lost-update race conditions on concurrent writes.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

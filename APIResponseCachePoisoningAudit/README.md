# APIResponseCachePoisoningAudit

Flags API endpoints at risk of cache poisoning from unkeyed request inputs reflected into cached responses.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

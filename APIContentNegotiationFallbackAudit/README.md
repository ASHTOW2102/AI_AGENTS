# APIContentNegotiationFallbackAudit

Flags API endpoints that silently fall back to a default response format when the Accept header is unrecognized, instead of returning 406.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

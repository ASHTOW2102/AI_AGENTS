# TokenIntrospectionCachingAudit

Flags resource servers that cache token introspection results longer than the token's own expiry window.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

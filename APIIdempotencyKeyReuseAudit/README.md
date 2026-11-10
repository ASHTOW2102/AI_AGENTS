# APIIdempotencyKeyReuseAudit

Flags API write endpoints that reuse idempotency keys across semantically different request bodies.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

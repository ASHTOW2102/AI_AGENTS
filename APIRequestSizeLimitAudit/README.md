# APIRequestSizeLimitAudit

Flags API endpoints that enforce no maximum request body size, leaving them open to memory-exhaustion via oversized payloads.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

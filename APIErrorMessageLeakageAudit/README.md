# APIErrorMessageLeakageAudit

Flags API endpoints that expose raw stack traces in error responses, leaking internal file paths, library versions, and logic to any client.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

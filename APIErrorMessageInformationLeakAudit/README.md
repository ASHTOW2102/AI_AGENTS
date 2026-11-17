# APIErrorMessageInformationLeakAudit

Flags API endpoints that return raw stack traces or internal exception messages to clients in error responses.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

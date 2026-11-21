# APIResourceExhaustionAudit

Flags API endpoints that accept unbounded array or nested-object input sizes, allowing a single request to exhaust server memory or CPU.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

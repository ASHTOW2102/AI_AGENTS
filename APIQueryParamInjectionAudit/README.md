# APIQueryParamInjectionAudit

Flags API endpoints that interpolate query string parameters directly into backend shell commands or file paths.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

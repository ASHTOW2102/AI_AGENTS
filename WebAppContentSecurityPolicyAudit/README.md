# WebAppContentSecurityPolicyAudit

Flags pages with no Content-Security-Policy header, or one that allows 'unsafe-inline' script execution.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

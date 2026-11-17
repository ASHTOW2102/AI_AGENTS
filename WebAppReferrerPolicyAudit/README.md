# WebAppReferrerPolicyAudit

Flags web pages with no Referrer-Policy header, leaking full URLs including query parameters to third-party sites.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

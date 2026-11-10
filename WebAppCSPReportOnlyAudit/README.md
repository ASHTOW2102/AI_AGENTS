# WebAppCSPReportOnlyAudit

Flags web applications stuck in Content-Security-Policy report-only mode without ever enforcing the policy.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

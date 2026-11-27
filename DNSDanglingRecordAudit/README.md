# DNSDanglingRecordAudit

Flags DNS records still pointing at a deprovisioned resource, a classic subdomain-takeover precondition.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

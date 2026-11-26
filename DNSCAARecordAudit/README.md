# DNSCAARecordAudit

Flags domains that issue certificates but have no CAA record restricting which certificate authorities may issue for them.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

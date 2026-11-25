# GitLFSQuotaAudit

Flags Git LFS storage usage approaching its quota, before pushes start failing outright.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

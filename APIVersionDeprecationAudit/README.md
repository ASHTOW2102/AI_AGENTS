# APIVersionDeprecationAudit

Audits deprecated API versions still receiving traffic without a sunset notice to clients.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

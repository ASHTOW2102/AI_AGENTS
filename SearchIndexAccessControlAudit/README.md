# SearchIndexAccessControlAudit

Flags search indexes that mix documents from multiple tenants or permission levels without per-document access filtering at query time.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# SearchQueryPIIRedactionAudit

Flags search query logging pipelines that store raw user queries without redacting PII before persistence.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

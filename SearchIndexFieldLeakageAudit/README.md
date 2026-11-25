# SearchIndexFieldLeakageAudit

Flags search indexes that include PII fields among their indexed and therefore searchable/returnable fields.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

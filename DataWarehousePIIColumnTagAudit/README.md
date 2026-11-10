# DataWarehousePIIColumnTagAudit

Flags data warehouse columns containing PII that are not tagged for access control and masking policies.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

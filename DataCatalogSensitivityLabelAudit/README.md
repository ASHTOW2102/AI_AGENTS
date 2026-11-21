# DataCatalogSensitivityLabelAudit

Flags data catalog assets containing known-sensitive column patterns that have no sensitivity label applied, so downstream tools can't enforce handling policy.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# WebAppFormAutocompleteAudit

Flags web forms that allow browser autocomplete on fields holding sensitive data like payment or SSN.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

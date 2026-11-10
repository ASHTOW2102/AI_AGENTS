# SearchAutocompleteInjectionAudit

Flags search autocomplete endpoints that reflect unsanitized user input into suggestion responses.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

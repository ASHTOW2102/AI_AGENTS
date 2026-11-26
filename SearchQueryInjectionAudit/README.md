# SearchQueryInjectionAudit

Flags search layers that build their query DSL via raw string concatenation of user input instead of a parameterized query builder.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

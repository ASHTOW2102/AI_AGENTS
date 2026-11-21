# SearchQueryCostBudgetAudit

Flags search queries with no estimated-cost cutoff, letting a single pathological query consume disproportionate cluster resources.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

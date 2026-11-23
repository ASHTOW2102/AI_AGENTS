# APIPaginationLimitAudit

Flags list endpoints that do not enforce a maximum page size, or whose enforced maximum is large enough to still enable resource-exhaustion scraping.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

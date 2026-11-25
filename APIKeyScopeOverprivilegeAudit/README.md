# APIKeyScopeOverprivilegeAudit

Flags API keys granted scopes beyond the minimum their intended use actually requires.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

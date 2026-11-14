# TokenScopeEscalationAudit

Flags token issuance flows that allow a client to request broader scopes than it was originally registered for.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

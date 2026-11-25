# OAuthScopeCreepAudit

Flags OAuth clients requesting scopes they never actually use, violating least privilege and widening the blast radius of a stolen token.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

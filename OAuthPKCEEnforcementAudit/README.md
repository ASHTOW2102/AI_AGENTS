# OAuthPKCEEnforcementAudit

Flags public OAuth clients (mobile/SPA, which cannot hold a secret) that do not enforce PKCE, leaving the authorization code flow open to interception.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

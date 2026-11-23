# OAuthRedirectURIValidationAudit

Flags OAuth clients whose redirect URI validation is wildcard or absent, enabling authorization-code theft via an attacker-controlled redirect.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

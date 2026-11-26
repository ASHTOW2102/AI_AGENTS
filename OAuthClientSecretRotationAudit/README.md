# OAuthClientSecretRotationAudit

Flags OAuth client secrets that have gone unrotated past their own configured maximum rotation interval.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

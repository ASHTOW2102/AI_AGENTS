# CloudFunctionEnvVarSecretAudit

Flags cloud functions storing credential-shaped values directly in plaintext environment variables instead of a secret manager.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ServerlessEnvironmentVariableSecretAudit

Flags serverless functions storing secrets as plaintext environment variables instead of a dedicated secrets manager.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

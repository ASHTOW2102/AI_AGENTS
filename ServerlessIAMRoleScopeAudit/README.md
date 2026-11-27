# ServerlessIAMRoleScopeAudit

Flags serverless function execution roles whose policy grants access to a wildcard resource instead of a scoped ARN.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

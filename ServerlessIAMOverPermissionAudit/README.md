# ServerlessIAMOverPermissionAudit

Flags serverless functions whose IAM execution role grants broader permissions than the function's declared actions require.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

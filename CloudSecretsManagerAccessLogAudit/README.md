# CloudSecretsManagerAccessLogAudit

Flags secrets manager entries with access logging disabled, making it impossible to detect unauthorized reads.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

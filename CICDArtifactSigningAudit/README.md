# CICDArtifactSigningAudit

Flags CI/CD pipelines that publish build artifacts to a public registry without cryptographically signing them, allowing undetected tampering.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# GitCommitSigningAudit

Flags repositories that do not require signed commits, making it impossible to verify a commit's actual author after the fact.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

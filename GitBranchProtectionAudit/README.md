# GitBranchProtectionAudit

Flags default branches that allow force pushes or do not require pull request review before merge.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

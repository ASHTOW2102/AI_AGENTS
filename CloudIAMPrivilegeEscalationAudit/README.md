# CloudIAMPrivilegeEscalationAudit

Flags IAM roles that combine the ability to create/attach policies with the ability to pass roles to services, a well-known privilege-escalation pair.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

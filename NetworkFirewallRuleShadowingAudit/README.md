# NetworkFirewallRuleShadowingAudit

Flags firewall rulesets where an earlier broad allow/deny rule shadows a later, more specific rule, making the specific rule dead code.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

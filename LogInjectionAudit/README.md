# LogInjectionAudit

Flags logging configurations that write raw, unsanitized request bodies to logs, letting attacker-controlled input forge or inject fake log entries.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

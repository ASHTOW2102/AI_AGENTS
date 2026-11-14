# WebAppClickjackingAudit

Flags web pages missing frame-busting headers that would allow clickjacking via iframe embedding.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

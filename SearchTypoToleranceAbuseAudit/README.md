# SearchTypoToleranceAbuseAudit

Flags search engines with fuzzy/typo-tolerant matching enabled that can be abused to enumerate near-matches of sensitive restricted terms.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

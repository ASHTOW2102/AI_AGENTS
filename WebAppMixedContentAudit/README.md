# WebAppMixedContentAudit

Flags HTTPS web pages that load active content (scripts, stylesheets) over plain HTTP, enabling man-in-the-middle injection.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# APIPaginationCursorTamperAudit

Flags paginated API endpoints whose cursor tokens are not signed, allowing clients to tamper with pagination state.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

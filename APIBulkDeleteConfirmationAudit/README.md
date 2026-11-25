# APIBulkDeleteConfirmationAudit

Flags bulk-delete endpoints with no confirmation token requirement, so a single mistaken or spoofed request can destroy many records at once.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

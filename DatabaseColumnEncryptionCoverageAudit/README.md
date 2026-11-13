# DatabaseColumnEncryptionCoverageAudit

Flags database tables with sensitive columns that are not covered by column-level encryption.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

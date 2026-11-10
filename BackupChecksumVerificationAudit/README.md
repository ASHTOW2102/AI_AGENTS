# BackupChecksumVerificationAudit

Checks that backup artifacts have post-write checksum verification to catch silent corruption.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# MobilePinningAudit

Audits mobile TLS certificate-pinning configuration for missing pins, absent backup pins, stale rotation schedules, and release builds with debug bypasses.

## Usage

```python
from agent import audit
print(audit({"pinning_enabled": True, "backup_pins": ["sha256/example"], "pin_rotation_days": 180}))
```

The input is a configuration dictionary; the result is a list of severity and issue records. No network access or API key is required.

# MobileScreenRecordingDetectionAudit

Checks that mobile apps detect and respond to active screen recording during sensitive-data display.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

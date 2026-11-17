# MobileAppOTAUpdateIntegrityAudit

Flags mobile apps that apply over-the-air code updates without verifying a cryptographic signature on the update bundle.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

# ContainerSBOMFreshnessAudit

Flags container images whose software bill of materials (SBOM) is stale relative to the image's last rebuild.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

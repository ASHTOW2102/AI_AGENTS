# ContainerImageProvenanceAudit

Flags container images with no verifiable build provenance attestation linking them to source and build pipeline.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

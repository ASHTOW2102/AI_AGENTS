# ContainerImageProvenanceAudit

Flags container deployments that pull images without verifying signed provenance (e.g. Sigstore/cosign attestation), allowing an unsigned or tampered image to be deployed undetected.

## What it checks

Checks container deployment configuration for signed image provenance verification and admission-time enforcement.

## Usage

```python
from agent import audit

findings = audit({...})
for f in findings:
    print(f["severity"], f["issue"])
```

## Running tests

```bash
python -m unittest discover -s tests
```

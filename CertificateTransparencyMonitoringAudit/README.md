# CertificateTransparencyMonitoringAudit

Flags domains with no Certificate Transparency log monitoring configured, delaying detection of mis-issued or rogue TLS certificates issued for the organization's domains.

## What it checks

Checks domain configuration for Certificate Transparency log monitoring and a restrictive CAA record.

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

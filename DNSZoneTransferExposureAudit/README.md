# DNSZoneTransferExposureAudit

Flags authoritative DNS servers that allow unrestricted zone transfer (AXFR) requests from arbitrary IP addresses, leaking the full internal DNS record set to anyone who asks.

## What it checks

Checks authoritative DNS server configuration for unrestricted zone transfer (AXFR) exposure.

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

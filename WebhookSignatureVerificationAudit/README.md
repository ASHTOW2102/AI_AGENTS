# WebhookSignatureVerificationAudit

Flags webhook receivers that process inbound payloads without verifying an HMAC signature header, allowing forged webhook events to be accepted as genuine.

## What it checks

Checks webhook receiver configuration for HMAC signature verification, constant-time comparison, and replay protection.

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

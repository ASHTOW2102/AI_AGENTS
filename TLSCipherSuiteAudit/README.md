# TLSCipherSuiteAudit

Flags TLS server configurations that still enable deprecated or weak cipher suites (e.g. RC4, 3DES, null ciphers) or protocol versions below TLS 1.2.

## What it checks

Checks TLS server configuration for deprecated weak cipher suites and minimum protocol version below TLS 1.2.

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

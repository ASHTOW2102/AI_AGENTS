# LogPIIRedactionAudit

Flags logging pipelines that write request/response payloads without redacting personally identifiable information, leaking PII into log storage and any downstream log consumers.

## What it checks

Checks logging configuration for PII redaction on full request/response payload logging and a retention policy.

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

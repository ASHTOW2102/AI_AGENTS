# ServiceAccountKeyRotationAudit

Flags service account credentials (API keys, static JSON keys) with no rotation policy or with an age exceeding the organization's rotation window.

## What it checks

Checks service account keys for a rotation policy and compliance with the maximum allowed key age.

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

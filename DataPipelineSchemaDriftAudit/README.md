# DataPipelineSchemaDriftAudit

Flags data pipeline stages that consume upstream data without schema validation, allowing silent schema drift (renamed, removed, or retyped columns) to corrupt downstream data.

## What it checks

Checks data pipeline stages for input schema validation and fail-closed behavior on schema mismatch.

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

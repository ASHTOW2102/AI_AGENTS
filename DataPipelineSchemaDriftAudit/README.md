# DataPipelineSchemaDriftAudit

Flags data pipelines where upstream schema drift is not caught before downstream consumption.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

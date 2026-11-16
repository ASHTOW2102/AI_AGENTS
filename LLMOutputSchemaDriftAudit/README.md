# LLMOutputSchemaDriftAudit

Flags LLM pipelines whose structured output has drifted from the expected schema without the application detecting it.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

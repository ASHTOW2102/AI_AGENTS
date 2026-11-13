# LLMToolCallValidationAudit

Flags LLM agent pipelines that execute tool calls without validating arguments against the tool's schema.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

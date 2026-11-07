# LLMPromptInjectionAudit

Flags LLM pipelines that lack isolation between trusted instructions and untrusted retrieved content.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

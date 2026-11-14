# LLMSystemPromptLeakAudit

Flags LLM applications where the system prompt can be extracted through adversarial user input.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

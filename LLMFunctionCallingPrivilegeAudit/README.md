# LLMFunctionCallingPrivilegeAudit

Flags LLM agents whose available tool functions grant more privilege than the agent's declared task requires.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

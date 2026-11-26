# APIHTTPPipeliningDesyncAudit

Flags proxy chains where the frontend and backend disagree on strict chunked-encoding parsing, a classic request-smuggling/desync precondition.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

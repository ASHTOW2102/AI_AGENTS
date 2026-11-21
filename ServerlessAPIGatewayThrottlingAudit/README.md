# ServerlessAPIGatewayThrottlingAudit

Flags API Gateway routes in front of serverless functions with no throttling configured, letting a traffic spike trigger runaway concurrent invocations and cost.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.

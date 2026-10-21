# RateLimitRuntimeAudit

Audits observed API throttling, associated server errors, limit saturation, alert coverage, and per-tenant isolation.

## Usage

```python
from agent import audit
print(audit({"throttled_requests": 12, "throttle_alert_configured": True,
             "limit_saturation_percent": 55, "per_tenant_limits": True}))
```

Provide aggregate runtime metrics; the tool returns severity and issue text without accessing a live service.

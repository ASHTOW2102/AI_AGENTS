# LoadBalancerHealthCheckAudit

Flags load balancer backend pools with health checks too shallow (e.g. a bare TCP connect) to detect an application that is listening but unable to serve requests correctly.

## What it checks

Checks load balancer backend health check depth (TCP-only vs. application-level) and dependency verification.

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

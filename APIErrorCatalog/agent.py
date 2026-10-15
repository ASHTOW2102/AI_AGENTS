"""Audit API error examples for stable, supportable contracts."""
import argparse, json
from pathlib import Path
def analyze(items):
    if not isinstance(items,list) or not items: raise ValueError("errors must be a non-empty array")
    findings=[]; seen=set()
    for i,x in enumerate(items,1):
        code=str(x.get("code","")).strip()
        if not code: raise ValueError(f"item {i}.code is required")
        if code in seen: findings.append({"code":"duplicate_code","severity":"high","item":i,"message":f"Error code {code} is duplicated."})
        seen.add(code)
        if not x.get("message"): findings.append({"code":"missing_message","severity":"medium","item":i,"message":f"{code} has no user-safe message."})
        status=x.get("status")
        if not isinstance(status,int) or not 400<=status<=599: findings.append({"code":"invalid_status","severity":"high","item":i,"message":f"{code} has an invalid HTTP status."})
        if status and status>=500 and not x.get("retryable"): findings.append({"code":"retry_unspecified","severity":"medium","item":i,"message":f"{code} does not declare retry behaviour."})
        if x.get("exposes_stack"): findings.append({"code":"stack_exposure","severity":"critical","item":i,"message":f"{code} exposes internal stack details."})
    return {"healthy":not findings,"items_checked":len(items),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)

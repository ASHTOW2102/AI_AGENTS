"""Audit recovery objectives and exercise evidence."""
import argparse,json
from datetime import date
from pathlib import Path
def analyze(items,today=None):
    today=today or date.today(); findings=[]
    for i,x in enumerate(items,1):
        name=str(x.get("service","")).strip()
        if not name: raise ValueError(f"item {i}.service is required")
        rto=x.get("rto_minutes"); rpo=x.get("rpo_minutes")
        if not isinstance(rto,(int,float)) or rto<=0: findings.append({"code":"invalid_rto","severity":"high","item":i,"message":f"{name} lacks a valid RTO."})
        if not isinstance(rpo,(int,float)) or rpo<0: findings.append({"code":"invalid_rpo","severity":"high","item":i,"message":f"{name} lacks a valid RPO."})
        tested=x.get("last_tested")
        if not tested: findings.append({"code":"untested","severity":"high","item":i,"message":f"{name} has no recovery-test evidence."})
        else:
            try: age=(today-date.fromisoformat(tested)).days
            except ValueError: raise ValueError(f"item {i}.last_tested must be YYYY-MM-DD")
            if age>365: findings.append({"code":"stale_test","severity":"high","item":i,"message":f"{name} recovery test is {age} days old."})
        if not x.get("owner"): findings.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{name} has no recovery owner."})
    return {"healthy":not findings,"items_checked":len(items),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)

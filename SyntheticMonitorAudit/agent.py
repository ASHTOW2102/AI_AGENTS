"""Audit synthetic checks for user-journey and alert coverage."""
import argparse,json
from pathlib import Path
def analyze(items):
    findings=[]
    for i,x in enumerate(items,1):
        name=str(x.get("name","")).strip()
        if not name: raise ValueError(f"item {i}.name is required")
        interval=x.get("interval_minutes")
        if not isinstance(interval,(int,float)) or interval<=0: raise ValueError(f"item {i}.interval_minutes must be positive")
        if interval>15 and x.get("critical"): findings.append({"code":"slow_critical_check","severity":"high","item":i,"message":f"{name} runs only every {interval} minutes."})
        if not x.get("alert_route"): findings.append({"code":"missing_alert_route","severity":"high","item":i,"message":f"{name} cannot notify an owner."})
        if not x.get("locations") or len(x["locations"])<2: findings.append({"code":"single_location","severity":"medium","item":i,"message":f"{name} lacks multi-location confirmation."})
        if not x.get("assertions"): findings.append({"code":"missing_assertions","severity":"high","item":i,"message":f"{name} checks availability without correctness assertions."})
    return {"healthy":not findings,"items_checked":len(items),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)

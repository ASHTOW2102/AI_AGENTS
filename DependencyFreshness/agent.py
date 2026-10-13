"""Prioritise stale dependency records using supplied release dates."""
import argparse,json
from datetime import date
from pathlib import Path
def analyze(items, today=None):
    today=today or date.today(); out=[]
    for i,x in enumerate(items,1):
        name=str(x.get("name","")).strip()
        if not name: raise ValueError(f"item {i}.name is required")
        try: released=date.fromisoformat(str(x.get("released_at","")))
        except ValueError: raise ValueError(f"item {i}.released_at must be YYYY-MM-DD")
        age=(today-released).days
        if age>730: out.append({"code":"very_stale","severity":"high","item":i,"message":f"{name} release is {age} days old."})
        elif age>365: out.append({"code":"stale","severity":"medium","item":i,"message":f"{name} release is {age} days old."})
        if x.get("latest_version") and x.get("version")!=x.get("latest_version"): out.append({"code":"upgrade_available","severity":"low","item":i,"message":f"{name} has a newer declared version."})
    return {"healthy":not out,"items_checked":len(items),"findings":out}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)

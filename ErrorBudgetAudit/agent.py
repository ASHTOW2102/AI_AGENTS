import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("service","")).strip();budget=x.get("budget_minutes");spent=x.get("spent_minutes")
  if not name:raise ValueError(f"item {i}.service is required")
  if not all(isinstance(v,(int,float)) and v>=0 for v in (budget,spent)):raise ValueError(f"item {i} budget values are invalid")
  remaining=budget-spent
  if remaining<0:f.append({"code":"budget_exhausted","severity":"critical","item":i,"message":f"{name} exceeded its error budget by {-remaining} minutes."})
  elif budget and remaining/budget<.2:f.append({"code":"budget_low","severity":"high","item":i,"message":f"{name} has under 20% error budget remaining."})
  if spent>0 and not x.get("review_owner"):f.append({"code":"missing_review_owner","severity":"medium","item":i,"message":f"{name} budget consumption has no owner."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

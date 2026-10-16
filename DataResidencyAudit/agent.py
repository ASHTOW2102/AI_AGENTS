import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("dataset","")).strip();region=str(x.get("region","")).upper()
  if not name:raise ValueError(f"item {i}.dataset is required")
  allowed={str(v).upper() for v in x.get("allowed_regions",[])}
  if not region:f.append({"code":"unknown_region","severity":"high","item":i,"message":f"{name} has no hosting region."})
  elif allowed and region not in allowed:f.append({"code":"residency_violation","severity":"critical","item":i,"message":f"{name} is hosted in disallowed region {region}."})
  if x.get("personal_data") and not x.get("transfer_basis") and len(allowed)>1:f.append({"code":"missing_transfer_basis","severity":"high","item":i,"message":f"{name} lacks transfer documentation."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{name} has no owner."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

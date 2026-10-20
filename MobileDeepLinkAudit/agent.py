import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("app")
  if not n:raise ValueError(f"item {i}.app required")
  if not x.get("host_allowlist"):f.append({"code":"missing_host_allowlist","severity":"critical","item":i,"message":f"{n} accepts untrusted deep-link hosts."})
  if not x.get("route_authorization"):f.append({"code":"missing_route_auth","severity":"critical","item":i,"message":f"{n} does not authorize linked routes."})
  if not x.get("parameter_validation"):f.append({"code":"unvalidated_parameters","severity":"high","item":i,"message":f"{n} does not validate link parameters."})
  if x.get("sensitive_action") and not x.get("user_confirmation"):f.append({"code":"no_action_confirmation","severity":"high","item":i,"message":f"{n} deep link can trigger sensitive actions silently."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

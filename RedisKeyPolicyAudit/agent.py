import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("namespace");key=x.get("key")
  if not n or not isinstance(key,str) or not key:raise ValueError(f"item {i} namespace/key required")
  ttl=x.get("ttl_seconds")
  if x.get("ephemeral") and (not isinstance(ttl,int) or ttl<=0):f.append({"code":"missing_ttl","severity":"high","item":i,"message":f"{n} ephemeral key has no expiry."})
  if len(key)>x.get("max_key_length",200):f.append({"code":"key_too_long","severity":"medium","item":i,"message":f"{n} key exceeds the length limit."})
  if not key.startswith(n+":"):f.append({"code":"missing_namespace_prefix","severity":"medium","item":i,"message":f"Key lacks namespace prefix {n}:."})
  if x.get("contains_personal_data"):f.append({"code":"personal_data_in_key","severity":"high","item":i,"message":"Redis key contains personal data."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

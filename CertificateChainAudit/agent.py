import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("hostname")
  if not n:raise ValueError(f"item {i}.hostname required")
  if not x.get("chain_complete"):f.append({"code":"incomplete_chain","severity":"high","item":i,"message":f"{n} certificate chain is incomplete."})
  if not x.get("hostname_match"):f.append({"code":"hostname_mismatch","severity":"critical","item":i,"message":f"{n} certificate does not match the hostname."})
  if not x.get("trusted_root"):f.append({"code":"untrusted_root","severity":"critical","item":i,"message":f"{n} chain has no trusted root."})
  if not x.get("revocation_checked"):f.append({"code":"revocation_unchecked","severity":"medium","item":i,"message":f"{n} certificate revocation was not checked."})
  if x.get("weak_signature"):f.append({"code":"weak_signature","severity":"high","item":i,"message":f"{n} chain uses a weak signature algorithm."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

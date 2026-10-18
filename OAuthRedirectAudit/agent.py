import argparse,json
from urllib.parse import urlparse
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  client=str(x.get("client","")).strip();uris=x.get("redirect_uris",[])
  if not client or not isinstance(uris,list) or not uris:raise ValueError(f"item {i} requires client and redirect_uris")
  for uri in uris:
   p=urlparse(uri)
   if "*" in uri:f.append({"code":"wildcard_redirect","severity":"critical","item":i,"message":f"{client} uses a wildcard redirect."})
   if p.scheme!="https" and p.hostname not in {"localhost","127.0.0.1"}:f.append({"code":"insecure_redirect","severity":"high","item":i,"message":f"{client} uses a non-HTTPS redirect."})
   if p.fragment:f.append({"code":"fragment_redirect","severity":"medium","item":i,"message":f"{client} redirect contains a fragment."})
  if not x.get("pkce_required"):f.append({"code":"pkce_optional","severity":"high","item":i,"message":f"{client} does not require PKCE."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

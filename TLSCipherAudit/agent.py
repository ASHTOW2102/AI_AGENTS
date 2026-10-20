import argparse,json
from pathlib import Path
WEAK=("3des","des-cbc","rc4","null","export","anon")
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("endpoint");ciphers=x.get("ciphers",[])
  if not n or not isinstance(ciphers,list):raise ValueError(f"item {i} endpoint/ciphers invalid")
  for cipher in ciphers:
   if any(w in str(cipher).lower() for w in WEAK):f.append({"code":"weak_cipher","severity":"critical","item":i,"message":f"{n} enables weak cipher {cipher}."})
  if not x.get("min_tls") or str(x["min_tls"]).lower() in {"tls1.0","tls1.1","1.0","1.1"}:f.append({"code":"legacy_protocol","severity":"high","item":i,"message":f"{n} permits an obsolete TLS version."})
  if not x.get("forward_secrecy"):f.append({"code":"no_forward_secrecy","severity":"medium","item":i,"message":f"{n} does not require forward secrecy."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

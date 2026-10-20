import argparse,json
from pathlib import Path
SENSITIVE={"access_token","refresh_token","session_id","password","secret"}
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("application");entries=x.get("entries",[])
  if not n or not isinstance(entries,list):raise ValueError(f"item {i} application/entries invalid")
  for e in entries:
   key=str(e.get("key","")).lower()
   if key in SENSITIVE and e.get("storage") in {"localStorage","sessionStorage","indexedDB"}:f.append({"code":"credential_in_browser_storage","severity":"critical","item":i,"message":f"{n} stores credential-like key {key} in browser storage."})
   if e.get("personal_data") and not e.get("expiry"):f.append({"code":"persistent_personal_data","severity":"high","item":i,"message":f"{n} stores personal data without expiry metadata."})
   if e.get("storage")=="localStorage" and e.get("cross_tab_sensitive"):f.append({"code":"cross_tab_exposure","severity":"medium","item":i,"message":f"{n} exposes sensitive state across tabs."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

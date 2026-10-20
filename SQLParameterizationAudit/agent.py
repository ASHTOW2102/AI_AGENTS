import argparse,json,re
from pathlib import Path
INTERPOLATION=re.compile(r"(?:\+\s*(?:user|input|param|request)|\x24\{(?:user|input|param)|\.format\s*\(|f[\"'].*\{)",re.I)
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("query")
  if not n or not isinstance(x.get("template"),str):raise ValueError(f"item {i} query/template required")
  if INTERPOLATION.search(x["template"]) and not x.get("parameterized"):f.append({"code":"possible_interpolation","severity":"critical","item":i,"message":f"{n} may interpolate untrusted values."})
  if x.get("raw_sql") and not x.get("reviewed"):f.append({"code":"unreviewed_raw_sql","severity":"high","item":i,"message":f"{n} uses unreviewed raw SQL."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

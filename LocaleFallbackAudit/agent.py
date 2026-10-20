import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  key=x.get("message_key");locales=x.get("locales",{})
  if not key or not isinstance(locales,dict):raise ValueError(f"item {i} key/locales invalid")
  default=x.get("default_locale")
  if default not in locales or not locales[default]:f.append({"code":"missing_default","severity":"high","item":i,"message":f"{key} lacks its default translation."})
  for locale,value in locales.items():
   if value in (None,"") and not x.get("runtime_fallback"):f.append({"code":"no_runtime_fallback","severity":"medium","item":i,"message":f"{key} locale {locale} is empty without fallback."})
  if not x.get("fallback_chain"):f.append({"code":"missing_fallback_chain","severity":"low","item":i,"message":f"{key} has no declared locale fallback chain."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

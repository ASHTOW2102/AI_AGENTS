import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  route=str(x.get("route","")).strip()
  if not route:raise ValueError(f"item {i}.route is required")
  types={str(v).lower() for v in x.get("content_types",[])};algos={str(v).lower() for v in x.get("algorithms",[])}
  if not algos:f.append({"code":"compression_disabled","severity":"medium","item":i,"message":f"{route} has no compression."})
  if "gzip" in algos and not {"br","zstd"}&algos:f.append({"code":"legacy_only","severity":"low","item":i,"message":f"{route} supports only legacy compression."})
  if any(t.startswith(("image/","video/","application/zip")) for t in types) and x.get("compress_binary"):f.append({"code":"binary_recompression","severity":"medium","item":i,"message":f"{route} recompresses binary formats."})
  if x.get("secrets_in_response") and x.get("compression_over_tls"):f.append({"code":"compression_side_channel","severity":"high","item":i,"message":f"{route} compresses secret-bearing TLS responses."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

import argparse,csv,json
from pathlib import Path
DANGEROUS=("=","+","-","@","\t","\r")
def analyze(rows):
 f=[]
 for i,row in enumerate(rows,1):
  if not isinstance(row,list):raise ValueError(f"row {i} must be an array")
  for col,value in enumerate(row,1):
   text=str(value).lstrip(" \t\r")
   if text.startswith(DANGEROUS):f.append({"code":"formula_prefix","severity":"high","item":i,"message":f"Row {i}, column {col} begins with a spreadsheet formula prefix."})
 return {"healthy":not f,"items_checked":len(rows),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();path=Path(n.input)
 with path.open(encoding="utf-8",newline="") as h:rows=list(csv.reader(h))
 r=analyze(rows);print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)

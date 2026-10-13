"""Audit generated-answer records for evidence and uncertainty signals."""
import argparse,json
from pathlib import Path
def analyze(items):
    out=[]
    for i,x in enumerate(items,1):
        answer=str(x.get("answer","")).strip()
        if not answer: raise ValueError(f"item {i}.answer is required")
        citations=x.get("citations",[])
        if x.get("requires_sources") and not citations: out.append({"code":"missing_citations","severity":"high","item":i,"message":"Source-dependent answer has no citations."})
        if any(w in answer.lower() for w in ("definitely","guaranteed","always")) and not citations: out.append({"code":"unsupported_certainty","severity":"medium","item":i,"message":"Strong certainty is unsupported."})
        if x.get("confidence") is not None and not 0<=x["confidence"]<=1: out.append({"code":"invalid_confidence","severity":"high","item":i,"message":"Confidence must be between zero and one."})
    return {"healthy":not out,"items_checked":len(items),"findings":out}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)

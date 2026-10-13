"""Check incident timelines for missing evidence and ordering problems."""
import argparse,json
from datetime import datetime
from pathlib import Path
def analyze(events):
    if not isinstance(events,list) or not events: raise ValueError("events must be a non-empty array")
    out=[]; previous=None
    for i,e in enumerate(events,1):
        try: moment=datetime.fromisoformat(str(e.get("timestamp","")).replace("Z","+00:00"))
        except ValueError: raise ValueError(f"event {i}.timestamp must be ISO-8601")
        if previous and moment<previous: out.append({"code":"out_of_order","severity":"high","item":i,"message":"Event occurs before the preceding event."})
        previous=moment
        if not str(e.get("actor","")).strip(): out.append({"code":"missing_actor","severity":"medium","item":i,"message":"Event has no accountable actor."})
        if e.get("type") in {"decision","mitigation"} and not e.get("evidence"): out.append({"code":"missing_evidence","severity":"high","item":i,"message":"Critical event lacks evidence."})
    return {"healthy":not out,"items_checked":len(events),"findings":out}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)

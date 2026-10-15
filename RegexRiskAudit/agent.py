"""Flag common catastrophic-backtracking shapes in regex inventories."""
import argparse,json,re
from pathlib import Path
NESTED=re.compile(r"\([^)]*[+*][^)]*\)[+*]")
AMBIGUOUS=re.compile(r"\([^)]*\|[^)]*\)[+*]")
def analyze(items):
    findings=[]
    for i,x in enumerate(items,1):
        name=str(x.get("name","")).strip(); pattern=x.get("pattern")
        if not name or not isinstance(pattern,str): raise ValueError(f"item {i} requires name and pattern")
        try: re.compile(pattern)
        except re.error as e: findings.append({"code":"invalid_regex","severity":"high","item":i,"message":f"{name} does not compile: {e}"}); continue
        if NESTED.search(pattern): findings.append({"code":"nested_quantifier","severity":"high","item":i,"message":f"{name} contains nested quantifiers."})
        if AMBIGUOUS.search(pattern): findings.append({"code":"ambiguous_repetition","severity":"medium","item":i,"message":f"{name} repeats an alternation."})
        if pattern.startswith(".*") and not pattern.startswith(".*?"): findings.append({"code":"leading_wildcard","severity":"low","item":i,"message":f"{name} starts with a greedy wildcard."})
    return {"healthy":not findings,"items_checked":len(items),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)

from agent import ChangeScribeAgent,build_release,parse_commit

def test_parses_type_scope_and_subject():
 change=parse_commit("feat(api): add cursor pagination")
 assert change.type=="feat" and change.scope=="api" and change.subject=="add cursor pagination"

def test_feature_recommends_minor():
 report=build_release(["feat: add exports","fix: handle empty input"])
 assert report.version_bump=="minor"
 assert "## Features" in report.markdown and "## Fixes" in report.markdown

def test_breaking_change_recommends_major():
 report=build_release(["feat!: remove legacy endpoint"])
 assert report.version_bump=="major"
 assert "## Breaking changes" in report.markdown

def test_nonconventional_messages_are_preserved_as_ignored():
 report=build_release(["Update README","fix: correct typo"])
 assert report.ignored==["Update README"]
 assert report.version_bump=="patch"

def test_agent_works_without_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 assert ChangeScribeAgent().write(["chore: tidy files"]).mode=="local"

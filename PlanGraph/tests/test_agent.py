import pytest
from agent import PlanGraphAgent,build_plan

PLAN=[
 {"id":"design","duration":2},
 {"id":"api","duration":4,"depends_on":["design"]},
 {"id":"ui","duration":3,"depends_on":["design"]},
 {"id":"test","duration":2,"depends_on":["api","ui"]},
]

def test_schedule_and_critical_path():
 report=build_plan(PLAN)
 assert report.project_duration==8
 assert report.critical_path==["design","api","test"]
 schedule={task.id:task for task in report.schedule}
 assert schedule["test"].start==6

def test_parallel_branch_does_not_inflate_duration():
 assert build_plan(PLAN).project_duration==8

def test_missing_dependency_is_rejected():
 with pytest.raises(ValueError,match="Missing dependencies"):
  build_plan([{"id":"ship","duration":1,"depends_on":["build"]}])

def test_cycle_is_rejected():
 with pytest.raises(ValueError,match="Dependency cycle"):
  build_plan([{"id":"a","duration":1,"depends_on":["b"]},{"id":"b","duration":1,"depends_on":["a"]}])

def test_agent_works_without_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 assert PlanGraphAgent().analyze(PLAN).mode=="local"

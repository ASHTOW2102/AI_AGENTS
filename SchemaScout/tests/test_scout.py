import pytest

from scout import SchemaScoutAgent, profile_csv, validate_csv


SAMPLE = """id,active,joined,name
1,true,2026-01-01,Ada
2,false,2026-02-03,Ben
3,true,,Cara
"""


def test_profiles_types_nulls_and_rows():
    report = profile_csv(SAMPLE)
    columns = {column.name: column for column in report.columns}
    assert report.row_count == 3
    assert columns["id"].inferred_type == "integer"
    assert columns["active"].inferred_type == "boolean"
    assert columns["joined"].inferred_type == "date"
    assert columns["joined"].null_count == 1


def test_contract_round_trip_accepts_source():
    report = profile_csv(SAMPLE)
    assert validate_csv(SAMPLE, report.contract()) == []


def test_validation_detects_drift_and_type_error():
    contract = profile_csv(SAMPLE).contract()
    bad = "id,active,joined,extra\noops,true,2026-01-01,x\n"
    violations = validate_csv(bad, contract)
    assert "Missing column: name" in violations
    assert "Unexpected column: extra" in violations
    assert any("expected integer, got string" in item for item in violations)


def test_duplicate_headers_are_rejected():
    with pytest.raises(ValueError, match="unique"):
        profile_csv("id,id\n1,2\n")


def test_agent_works_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert SchemaScoutAgent().profile(SAMPLE).mode == "local"

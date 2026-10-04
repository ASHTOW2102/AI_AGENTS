import pytest

from agent import CoverageCompassAgent, prioritize_coverage


def coverage(total=72.5):
    return {
        "totals": {"percent_covered": total},
        "files": {
            "src/untested.py": {
                "summary": {
                    "covered_lines": 0,
                    "missing_lines": 80,
                    "excluded_lines": 0,
                    "missing_branches": 12,
                }
            },
            "src/partial.py": {
                "summary": {
                    "covered_lines": 70,
                    "missing_lines": 30,
                    "excluded_lines": 0,
                    "missing_branches": 2,
                    "percent_covered": 70,
                }
            },
            "src/good.py": {
                "summary": {
                    "covered_lines": 95,
                    "missing_lines": 5,
                    "excluded_lines": 0,
                    "missing_branches": 0,
                    "percent_covered": 95,
                }
            },
        },
    }


def test_prioritizes_zero_coverage_file_first():
    report = prioritize_coverage(coverage())
    assert report.priorities[0].path == "src/untested.py"
    assert "zero line coverage" in report.priorities[0].reasons


def test_well_covered_file_is_not_a_priority():
    paths = {item.path for item in prioritize_coverage(coverage()).priorities}
    assert "src/good.py" not in paths


def test_top_limit_is_respected():
    assert len(prioritize_coverage(coverage(), top=1).priorities) == 1


def test_clean_report_passes():
    payload = {
        "totals": {"percent_covered": 92},
        "files": {
            "src/good.py": {
                "summary": {
                    "covered_lines": 92,
                    "missing_lines": 8,
                    "excluded_lines": 0,
                    "missing_branches": 0,
                    "percent_covered": 92,
                }
            }
        },
    }
    assert prioritize_coverage(payload).valid


def test_malformed_report_is_rejected():
    with pytest.raises(ValueError, match="files and totals"):
        prioritize_coverage({"totals": {}})


def test_threshold_is_validated():
    with pytest.raises(ValueError, match="threshold"):
        prioritize_coverage(coverage(), threshold=101)


def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert CoverageCompassAgent().inspect(coverage()).mode == "local"

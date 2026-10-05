import pytest

from agent import CacheGuardAgent, audit_cache


def test_safe_public_asset_passes():
    report = audit_cache(
        [{
            "path": "/assets/app.abc123.js",
            "method": "GET",
            "status": 200,
            "cache_control": "public, max-age=31536000, immutable",
            "vary": "Accept-Encoding",
            "static_asset": True,
        }]
    )
    assert report.valid


def test_sensitive_response_requires_no_store():
    report = audit_cache(
        [{
            "path": "/account",
            "status": 200,
            "cache_control": "private, max-age=60",
            "vary": "",
            "sensitive": True,
        }]
    )
    assert "sensitive_response_storable" in {
        item.code for item in report.findings
    }


def test_authenticated_public_cache_is_critical():
    report = audit_cache(
        [{
            "path": "/dashboard",
            "status": 200,
            "cache_control": "public, max-age=60",
            "vary": "Authorization",
            "request_authenticated": True,
        }]
    )
    finding = next(
        item for item in report.findings
        if item.code == "authenticated_shared_cache"
    )
    assert finding.severity == "critical"


def test_cookie_response_cannot_be_public():
    report = audit_cache(
        [{
            "path": "/session",
            "status": 200,
            "cache_control": "public, s-maxage=60",
            "vary": "",
            "response_sets_cookie": True,
        }]
    )
    assert "cookie_response_public" in {
        item.code for item in report.findings
    }


def test_conflicting_directives_are_reported():
    report = audit_cache(
        [{
            "path": "/data",
            "status": 200,
            "cache_control": "no-store, max-age=300",
            "vary": "",
        }]
    )
    assert "conflicting_directives" in {
        item.code for item in report.findings
    }


def test_missing_policy_and_static_ttl_are_reported():
    report = audit_cache(
        [{
            "path": "/assets/logo.svg",
            "status": 200,
            "cache_control": "",
            "vary": "",
            "static_asset": True,
        }]
    )
    codes = {item.code for item in report.findings}
    assert {"missing_cache_control", "static_asset_without_ttl"} <= codes


def test_invalid_path_is_rejected():
    with pytest.raises(ValueError, match="start with"):
        audit_cache(
            [{"path": "relative", "status": 200, "cache_control": "", "vary": ""}]
        )


def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    safe = [{
        "path": "/asset.js",
        "status": 200,
        "cache_control": "public, max-age=60",
        "vary": "",
        "static_asset": True,
    }]
    assert CacheGuardAgent().inspect(safe).mode == "local"

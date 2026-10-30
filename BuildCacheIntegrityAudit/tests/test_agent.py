import unittest
from agent import audit


class BuildCacheIntegrityAuditTests(unittest.TestCase):
    def test_untrusted_cache_writer(self):
        self.assertEqual("critical", audit({"untrusted_pull_requests_write_cache": True})[0]["severity"])

    def test_isolated_cache(self):
        cache = {"shared_between_trust_levels": True, "cache_namespace_isolated": True,
                 "remote_cache_enabled": True, "artifact_integrity_verified": True,
                 "untrusted_pull_requests_write_cache": False, "cache_retention_bounded": True}
        self.assertEqual([], audit(cache))


if __name__ == "__main__":
    unittest.main()

import unittest
from agent import audit


class CacheStampedeAuditTests(unittest.TestCase):
    def test_no_miss_coordination(self):
        self.assertTrue(any("duplicate origin" in f["issue"] for f in audit({"ttl_seconds": 60})))

    def test_protected_cache(self):
        config = {"ttl_seconds": 60, "request_coalescing": True, "refresh_jitter_percent": 10,
                  "stale_fallback_expected": True, "stale_fallback_enabled": True}
        self.assertEqual([], audit(config))


if __name__ == "__main__":
    unittest.main()

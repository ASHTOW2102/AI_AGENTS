import unittest
from agent import audit


class APICacheValidatorAuditTests(unittest.TestCase):
    def test_personalized_shared_cache(self):
        self.assertIn("shared caching", audit({"personalized": True, "shared_cache_enabled": True})[0]["issue"])

    def test_safe_private_cache(self):
        endpoint = {"cacheable": True, "etag_or_last_modified": True, "personalized": True,
                    "shared_cache_enabled": False, "sensitive": False, "stale_while_revalidate_seconds": 0}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()

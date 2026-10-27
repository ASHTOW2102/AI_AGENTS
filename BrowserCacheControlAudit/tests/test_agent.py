import unittest
from agent import audit


class BrowserCacheControlAuditTests(unittest.TestCase):
    def test_sensitive_shared_cache(self):
        self.assertIn("shared cache", audit({"sensitive": True, "shared_cache_allowed": True})[0]["issue"])

    def test_safe_cache_policy(self):
        resource = {"sensitive": True, "shared_cache_allowed": False, "browser_cache_max_age": 0,
                    "max_sensitive_cache_age": 0, "private_response": True, "vary_authorization": True}
        self.assertEqual([], audit(resource))


if __name__ == "__main__":
    unittest.main()

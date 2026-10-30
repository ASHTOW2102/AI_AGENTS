import unittest
from agent import audit


class MobileOfflineDataAuditTests(unittest.TestCase):
    def test_unencrypted_sensitive_cache(self):
        self.assertIn("not encrypted", audit({"sensitive_data_cached_offline": True,
                                             "offline_cache_encrypted": False})[0]["issue"])

    def test_safe_offline_policy(self):
        app = {"sensitive_data_cached_offline": True, "offline_cache_encrypted": True,
               "offline_cache_max_age_hours": 2, "approved_offline_cache_max_age_hours": 24,
               "offline_mutations_enabled": False, "logout_clears_local_data": True}
        self.assertEqual([], audit(app))


if __name__ == "__main__":
    unittest.main()

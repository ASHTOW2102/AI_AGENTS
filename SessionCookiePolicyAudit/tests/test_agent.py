import unittest
from agent import audit


class SessionCookiePolicyAuditTests(unittest.TestCase):
    def test_missing_security_flags(self):
        self.assertEqual(3, len(audit({})))

    def test_hardened_cookie(self):
        self.assertEqual([], audit({"secure": True, "http_only": True, "same_site": "lax",
                                    "max_age_seconds": 3600, "max_allowed_age_seconds": 86400,
                                    "domain_scope": "host"}))


if __name__ == "__main__":
    unittest.main()

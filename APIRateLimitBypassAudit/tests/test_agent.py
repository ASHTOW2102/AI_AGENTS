import unittest
from agent import audit


class APIRateLimitBypassAuditTests(unittest.TestCase):

    def test_bypassable(self):
        self.assertTrue(audit({"rate_limit_key": "ip", "supports_proxy_rotation": True}))

    def test_ok(self):
        self.assertFalse(audit({"rate_limit_key": "user_id", "supports_proxy_rotation": False, "authenticated_rate_limit_key": True}))

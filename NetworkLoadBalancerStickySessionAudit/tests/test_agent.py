import unittest
from agent import audit


class NetworkLoadBalancerStickySessionAuditTests(unittest.TestCase):

    def test_predictable_cookie(self):
        self.assertTrue(audit({"sticky_sessions_enabled": True, "session_cookie_value_predictable": True}))

    def test_ok(self):
        self.assertFalse(audit({"sticky_sessions_enabled": True, "session_cookie_value_predictable": False, "session_cookie_signed": True}))

import unittest
from agent import audit


class LoadBalancerStickySessionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"sticky_sessions_enabled": True, "session_cookie_encrypted": False}))

    def test_ok(self):
        self.assertFalse(audit({"sticky_sessions_enabled": True, "session_cookie_encrypted": True}))

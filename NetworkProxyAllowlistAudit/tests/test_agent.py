import unittest
from agent import audit


class NetworkProxyAllowlistAuditTests(unittest.TestCase):

    def test_wildcard(self):
        self.assertTrue(audit({"allows_wildcard_destination": True}))

    def test_ok(self):
        self.assertFalse(audit({"allows_wildcard_destination": False, "unused_rule_days": 10}))

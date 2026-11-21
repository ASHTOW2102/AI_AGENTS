import unittest
from agent import audit


class NetworkFirewallRuleShadowingAuditTests(unittest.TestCase):

    def test_shadowed_rule(self):
        self.assertTrue(audit({"rules": [{"shadowed_by_earlier_rule": True}]}))

    def test_ok(self):
        self.assertFalse(audit({"rules": [{"shadowed_by_earlier_rule": False}], "rule_order_validated": True}))

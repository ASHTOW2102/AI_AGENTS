import unittest
from agent import audit


class WAFRuleCoverageAuditTests(unittest.TestCase):

    def test_not_blocking(self):
        self.assertTrue(audit({"production": True, "mode": "detect"}))

    def test_ok(self):
        self.assertFalse(audit({"production": True, "mode": "block", "required_rule_sets": ["sqli"], "enabled_rule_sets": ["sqli"]}))

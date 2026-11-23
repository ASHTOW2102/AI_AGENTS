import unittest
from agent import audit


class DataRetentionPolicyAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"contains_pii": True, "retention_policy_defined": False}))

    def test_ok(self):
        self.assertFalse(audit({"contains_pii": True, "retention_policy_defined": True}))

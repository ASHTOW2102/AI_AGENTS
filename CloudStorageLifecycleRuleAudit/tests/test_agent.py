import unittest
from agent import audit


class CloudStorageLifecycleRuleAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"stores_logs": True, "lifecycle_rules_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"stores_logs": True, "lifecycle_rules_configured": True}))

import unittest
from agent import audit


class FeatureFlagAuditLogAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"logs_flag_changes": False}))

    def test_ok(self):
        self.assertFalse(audit({"logs_flag_changes": True}))

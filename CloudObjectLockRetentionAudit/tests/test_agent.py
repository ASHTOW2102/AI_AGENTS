import unittest
from agent import audit


class CloudObjectLockRetentionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"stores_compliance_records": True, "object_lock_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"stores_compliance_records": True, "object_lock_enabled": True}))

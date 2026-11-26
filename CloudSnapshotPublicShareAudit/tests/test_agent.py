import unittest
from agent import audit


class CloudSnapshotPublicShareAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"publicly_shared": True, "contains_sensitive_data": True}))

    def test_ok(self):
        self.assertFalse(audit({"publicly_shared": False}))

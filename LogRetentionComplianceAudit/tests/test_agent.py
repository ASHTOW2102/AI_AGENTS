import unittest
from agent import audit


class LogRetentionComplianceAuditTests(unittest.TestCase):

    def test_too_short(self):
        self.assertTrue(audit({"retention_days": 10, "required_retention_days": 30}))

    def test_ok(self):
        self.assertFalse(audit({"retention_days": 30, "required_retention_days": 30, "deletion_job_verified": True}))

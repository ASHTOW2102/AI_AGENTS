import unittest
from agent import audit


class DataLakeAccessLoggingAuditTests(unittest.TestCase):

    def test_no_logging(self):
        self.assertTrue(audit({"access_logging_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"access_logging_enabled": True, "log_retention_days": 180, "min_required_retention_days": 90}))

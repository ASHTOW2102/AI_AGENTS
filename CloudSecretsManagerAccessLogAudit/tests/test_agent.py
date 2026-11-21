import unittest
from agent import audit


class CloudSecretsManagerAccessLogAuditTests(unittest.TestCase):

    def test_no_logging(self):
        self.assertTrue(audit({"access_logging_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"access_logging_enabled": True, "unusual_access_alerting_enabled": True}))

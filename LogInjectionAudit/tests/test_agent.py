import unittest
from agent import audit


class LogInjectionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"logs_raw_request_body": True, "sanitizes_user_input_before_logging": False}))

    def test_ok(self):
        self.assertFalse(audit({"logs_raw_request_body": True, "sanitizes_user_input_before_logging": True}))

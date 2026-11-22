import unittest
from agent import audit


class LogPIIRedactionAuditTests(unittest.TestCase):

    def test_full_payload_no_redaction(self):
        self.assertTrue(audit({"logs_full_request_response_bodies": True, "redacts_pii_fields": False}))

    def test_ok(self):
        self.assertFalse(audit({"logs_full_request_response_bodies": True, "redacts_pii_fields": True, "has_log_retention_policy": True}))

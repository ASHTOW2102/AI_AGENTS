import unittest
from agent import audit


class DataExportAuditTrailAuditTests(unittest.TestCase):

    def test_no_audit(self):
        self.assertTrue(audit({"audit_log_entry_created": False}))

    def test_ok(self):
        self.assertFalse(audit({"audit_log_entry_created": True, "includes_requesting_identity": True}))

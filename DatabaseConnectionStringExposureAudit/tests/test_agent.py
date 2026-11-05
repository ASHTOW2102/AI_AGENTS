import unittest
from agent import audit


class DatabaseConnectionStringExposureAuditTests(unittest.TestCase):

    def test_in_source_control(self):
        self.assertTrue(audit({"connection_string_in_source_control": True}))

    def test_ok(self):
        self.assertFalse(audit({"connection_string_in_source_control": False, "connection_string_in_logs": False, "stored_in_secret_manager": True, "contains_credentials": True}))

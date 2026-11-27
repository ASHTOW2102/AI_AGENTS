import unittest
from agent import audit


class TLSSessionResumptionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"supports_session_resumption": True, "session_ticket_key_rotation_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"supports_session_resumption": True, "session_ticket_key_rotation_enabled": True}))

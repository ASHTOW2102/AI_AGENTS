import unittest
from agent import audit


class CSRFTokenReuseAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"csrf_protection_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"csrf_protection_enabled": True, "validates_token_against_session": True}))

import unittest
from agent import audit


class OAuthPKCEEnforcementAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"client_type": "public", "enforces_pkce": False}))

    def test_ok(self):
        self.assertFalse(audit({"client_type": "public", "enforces_pkce": True}))

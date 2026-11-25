import unittest
from agent import audit


class OAuthScopeCreepAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"requested_scopes": ["read", "write", "delete"], "actually_used_scopes": ["read"]}))

    def test_ok(self):
        self.assertFalse(audit({"requested_scopes": ["read"], "actually_used_scopes": ["read"]}))

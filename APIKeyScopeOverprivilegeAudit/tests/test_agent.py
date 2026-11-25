import unittest
from agent import audit


class APIKeyScopeOverprivilegeAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"granted_scopes": ["read", "write", "admin"], "minimum_required_scopes": ["read"]}))

    def test_ok(self):
        self.assertFalse(audit({"granted_scopes": ["read"], "minimum_required_scopes": ["read"]}))

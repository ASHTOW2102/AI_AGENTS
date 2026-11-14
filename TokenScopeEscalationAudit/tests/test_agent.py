import unittest
from agent import audit


class TokenScopeEscalationAuditTests(unittest.TestCase):

    def test_escalation(self):
        self.assertTrue(audit({"requested_scopes": ["admin"], "registered_scopes": ["read"]}))

    def test_ok(self):
        self.assertFalse(audit({"requested_scopes": ["read"], "registered_scopes": ["read"], "scope_validated_at_issuance": True}))

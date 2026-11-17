import unittest
from agent import audit


class APIFieldLevelAuthorizationAuditTests(unittest.TestCase):

    def test_exposed_field(self):
        self.assertTrue(audit({"sensitive_fields": ["salary"], "field_level_authorized_fields": []}))

    def test_ok(self):
        self.assertFalse(audit({"sensitive_fields": ["salary"], "field_level_authorized_fields": ["salary"], "object_level_authorized": True, "field_level_authorization_enabled": True}))

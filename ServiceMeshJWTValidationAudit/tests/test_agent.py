import unittest
from agent import audit


class ServiceMeshJWTValidationAuditTests(unittest.TestCase):

    def test_no_issuer_pin(self):
        self.assertTrue(audit({"jwt_validation_enabled": True, "issuer_pinned": False}))

    def test_ok(self):
        self.assertFalse(audit({"jwt_validation_enabled": True, "issuer_pinned": True, "audience_validated": True}))

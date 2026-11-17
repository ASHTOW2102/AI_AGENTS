import unittest
from agent import audit


class MobileAppOTAUpdateIntegrityAuditTests(unittest.TestCase):

    def test_unverified(self):
        self.assertTrue(audit({"supports_ota_updates": True, "ota_bundle_signature_verified": False}))

    def test_ok(self):
        self.assertFalse(audit({"supports_ota_updates": True, "ota_bundle_signature_verified": True, "rollback_on_verification_failure": True}))
